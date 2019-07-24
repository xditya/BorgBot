"""Make / Download Telegram Animated Sticker Packs without installing Third Party applications. Donot reply to stickers as it can break the animated sticker pack. Other commands donot work yet.
Available Commands:
.animticker [Optional Emoji]
from telethon import events
from io import BytesIO
from PIL import Image
import asyncio
import datetime
from collections import defaultdict
import math
import os
import requests
import zipfile
from telethon.errors.rpcerrorlist import StickersetInvalidError
from telethon.errors import MessageNotModifiedError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    InputMediaUploadedDocument,
    InputPeerNotifySettings,
    InputStickerSetID,
    InputStickerSetShortName,
    MessageMediaPhoto
)
from uniborg.util import admin_cmd


@borg.on(admin_cmd("animsticker ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("Reply to a photo to add to my personal animated sticker pack.")
        return
    reply_message = await event.get_reply_message()
    sticker_emoji = "�9�7"
    input_str = event.pattern_match.group(1)
    if input_str:
        sticker_emoji = input_str
    if not is_message_image(reply_message):
        await event.edit("Invalid message type")
        return
    me = borg.me
    userid = event.from_id
    packname = f"{userid}'s @UniBorg Pack"
    packshortname = f"Uni_Borg_{userid}_Anim"  # format: Uni_Borg_userid

    await event.edit("Stealing this Anim sticker. Please Wait!")

    async with borg.conversation("@Stickers") as bot_conv:
        now = datetime.datetime.now()
        dt = now + datetime.timedelta(minutes=1)
        file = await borg.download_file(reply_message.media)
        with BytesIO(file) as mem_file, BytesIO() as sticker:
            resize_image(mem_file, sticker)
            sticker.seek(0)
            uploaded_sticker = await borg.upload_file(sticker, file_name="@UniBorg_Sticker.tgs")
            if not await stickerset_exists(bot_conv, packshortname):
                await silently_send_message(bot_conv, "/cancel")
                response = await silently_send_message(bot_conv, "/newanimated")
                if response.text != "Yay! A new stickers pack. How are we going to call it? Please choose a name for your pack.":
                    await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                    return
                response = await silently_send_message(bot_conv, packname)
                if not response.text.startswith("Alright!"):
                    await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                    return
                await bot_conv.send_file(
                    InputMediaUploadedDocument(
                        file=uploaded_sticker,
                        mime_type='image/png',
                        attributes=[
                            DocumentAttributeFilename(
                                "@UniBorg_Sticker.tgs"
                            )
                        ]
                    ),
                    force_document=True
                )
                await bot_conv.get_response()
                await silently_send_message(bot_conv, sticker_emoji)
                await silently_send_message(bot_conv, "/publish")
                await silently_send_message(bot_conv, "/skip")
                response = await silently_send_message(bot_conv, packshortname)
                if response.text == "Sorry, this short name is already taken.":
                    await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                    return
            else:
                await silently_send_message(bot_conv, "/cancel")
                await silently_send_message(bot_conv, "/addanimated")
                await silently_send_message(bot_conv, packshortname)
                await bot_conv.send_file(
                    InputMediaUploadedDocument(
                        file=uploaded_sticker,
                        mime_type='image/png',
                        attributes=[
                            DocumentAttributeFilename(
                                "@UniBorg_Sticker.tgs"
                            )
                        ]
                    ),
                    force_document=True
                )
                response = await bot_conv.get_response()
                await silently_send_message(bot_conv, response)
                await silently_send_message(bot_conv, sticker_emoji)
                await silently_send_message(bot_conv, "/done")

    await event.edit(f"▕╮╭┻┻╮╭┻┻╮╭▕╮╲\n▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏\n▕╭┻┻┻┛┗┻┻┛   ▄1�7  ╰▏\n▕╰━━━┓┈┈┈╭╮▕╭╮▏\n▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏\n▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏\n\nsticker stolen! Your pack can be found [here](t.me/addstickers/{packshortname})")
"""Emoji

Available Commands:

.wtf"""

from telethon import events

import asyncio
from telethon.tl.types import ChannelParticipantsAdmins

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "wtf":
        await event.edit(input_str)
        animation_chars = [
            "What",
            "What The",
            "What The F",
            "What The F Brah"
            ]
    mentions = "What The F Brah\n https://telegra.ph//file/f3b760e4a99340d331f9b.jpg"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])

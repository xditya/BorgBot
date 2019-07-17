from telethon import events
import random, re
from uniborg.util import admin_cmd
import asyncio



@borg.on(admin_cmd("oof ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ooof = "Oof"
    for j in range(15):
        ooof = ooof[:-1] + "of"
        await event.edit(ooof)
"""Emoji

Available Commands:

.k"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.4
    animation_ttl = range(0, 9)
    input_str = event.pattern_match.group(1)
    if input_str == "k":
        await event.edit(input_str)
        animation_chars = [
            "💠",
            "💠💠\n💠",
            "💠💠💠\n💠\n💠",
            "💠💠💠💠\n💠\n💠\n💠💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠\n💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠\n💠\n💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠\n💠\n💠\n💠"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 9])

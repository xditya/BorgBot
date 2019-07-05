"""Emoji

Available Commands:

.fk"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd





@borg.on(admin_cmd("fk ?(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3
    

    animation_ttl = range(0, 77)

    input_str = event.pattern_match.group(1)

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

            await event.edit(animation_chars[i % 27])

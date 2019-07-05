"""Emoji

Available Commands:

.fk"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5
    

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "fk":

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

            await event.edit(animation_chars[i % 27])

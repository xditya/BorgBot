"""Emoji

Available Commands:

.gangsta"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd





@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "gangsta":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "gAnGsTa",
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ gAnGsTa uNtiL i aRriVe 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)

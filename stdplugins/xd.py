"""
Available Commands
.lul
.muth
Plugin by @Arnab431"""

from telethon import events
import asyncio


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "muth":

        await event.edit(input_str)

        animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "D===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦"

        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3
    animation_ttl = range(0, 30)
    input_str = event.pattern_match.group(1)

    if input_str == "lul":
        await event.edit(input_str)
        animation_chars = [

            "L",
            "LO",
            "LOL"
        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 3])

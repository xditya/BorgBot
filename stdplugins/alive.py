"""Command .alive"""
from telethon import events
import asyncio
import os
import sys

@borg.on(events.NewMessage(pattern=r"\.alive", outgoing=True))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("I am alive u noob ,\nStop Checking (;_;) again and again")      
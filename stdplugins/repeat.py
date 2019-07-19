import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd("repeat ?(.*)"))
async def _(event):
    message = event.text[10:]
    count = int(event.text[8:10])
    repmessage = message * count
    await event.respond(repmessage)
    await event.delete()

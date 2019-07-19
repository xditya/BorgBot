import asyncio
from asyncio import wait
from uniborg.util import admin_cmd


@borg.on(admin_cmd("repeat ?(.*)"))
async def _(event):
    count = int(event.text[10:8])
    message = (event.text[:10])
    repmessage = message * count
    await wait([event.respond(repmessage)for i in range(count)])
    await event.delete()

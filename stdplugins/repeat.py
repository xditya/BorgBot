import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd("repeat ?(.*)"))
async def _(event):
  if event.fwd_from:
    message = event.text[10:]
    count = int(event.text[8:10])
    repmessage = message * count
    await event.edit(repmessage)

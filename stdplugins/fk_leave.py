# For @UniBorg
"""fake leave
.xleave"""

from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
import importlib.util
import asyncio
import random
import importlib.util

@borg.on(events.NewMessage(outgoing=True, pattern='^\.(x?x)leave '))

async def timer_blankx(e):
 txt=e.text[7:] + '\n\n`Processing....` '
 j=7
 k=j
 for j in range(j):
  await e.edit(txt + str(k))
  k=k-1
  await asyncio.sleep(1)
 if e.pattern_match.group(1) == 'x':
  await e.edit("`Legend is leaving this chat.....!` @admin `Goodbye aren't forever..` ")
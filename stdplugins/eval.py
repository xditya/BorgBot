"""Evaluate Python Code inside Telegram
Syntax: .eval PythonCode"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from telethon import events, sync, errors, functions, types
import inspect
import io
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd("eval ?((.|\n)*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    evaluation = eval(cmd)
    await event.delete()
    # https://t.me/telethonofftopic/43873
    # https://t.me/TheUseLessGroup/40472
    try:
        if inspect.isawaitable(evaluation):
            evaluation = await evaluation
    except (Exception) as e:
        evaluation = str(e)
    # https://t.me/telethonofftopic/43873

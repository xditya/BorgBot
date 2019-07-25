"""Available Commands: .hacker"""
from telethon import events 
import asyncio   
from uniborg.util import admin_cmd  
 
@borg.on(admin_cmd("(.*)"))
async def _(event):
  if event.fwd_from: 
    return 
  animation_interval = 0.3
  animation_ttl = range(0, 6) 
  input_str = event.pattern_match.group(1) 
  if input_str == "hacker": 
     await event.edit(input_str)
     animation_chars = [ 
        "ʜᴀᴄᴋɪɴɢ sᴛᴀʀᴛᴇᴅ", 
        "Pʀᴏᴄᴇssɪɴɢ ░░░░░░░░░░ 00%", 
        "Pʀᴏᴄᴇssɪɴɢ ██░░░░░░░░ 22%",
        "Pʀᴏᴄᴇssɪɴɢ █████░░░░░ 54%", 
        "Pʀᴏᴄᴇssɪɴɢ ██████████ 97%",
        "ᴛᴀʀɢᴇᴛ ʜᴀᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ. \n ᴘᴀʏ 69$ ᴛᴏ @arnab431 ᴛᴏ ʀᴇᴍᴏᴠᴇ ʜᴀᴄᴋ" 

 ] 
     for i in animation_ttl:
  	      await asyncio.sleep(animation_interval)    
  	      await event.edit(animation_chars[i %6 ])

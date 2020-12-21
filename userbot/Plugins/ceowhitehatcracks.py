"""Emoji
Available Commands:
.ceowhitehatcracks
Credits to @Leo_parmigiana
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("ceowhitehatcracks"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "ceowhitehatcracks":
    await event.edit("@CeoWhiteHatCracks")
    animation_chars = [
            "@CeoWhiteHatCracks is your dad bitch",
            "@CeoWhiteHatCracks just a Grp Bitch",
            "@Leo_BITCH_USERBOT is AI ultimate.Bitch.",
            "@CeoWhiteHatCracks owner of DAD ",
            "Dont Fuck with me Bitch...@WONKRU_HERE",
            "hows Your Dad",
            "@Leo_BITCH_USERBOT"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

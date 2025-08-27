import asyncio
import requests
import random
import re
import textwrap
import aiofiles
import aiohttp
import os
import sqlite3
import time
import datetime
from pyrogram import Client as client
import json
import redis, re
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from typing import List, Union
from pyrogram import *
import pyromod.listen
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
import aiohttp
from datetime import datetime
from random import choice
from collections import defaultdict
from pyrogram import enums
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from traceback import format_exc
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram.errors import FloodWait
from os import remove
from asyncio import sleep
from pyrogram.types import *
from telegraph import upload_file
from unidecode import unidecode
import sqlite3
from pyrogram import Client, idle
from random import randint
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from asyncio import gather
from io import BytesIO
from pyrogram import Client, filters
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned
from CASERr.CASERr import ch as chh
from bot import OWNER
      
name = f"{OWNER}"

@Client.on_message(filters.text, group=557645456)
async def coderady(client, message):
    if "Code:" in message.text:
        parts = message.text.split("Code:")
        if len(parts) > 1:
            target = parts[1].strip().split()[0]  
            await message.reply_text(f"**`{target}`**")                
      
src = []

@Client.on_message(filters.command(["قفل التسليه","تعطيل التسليه"], ""), group=258073) 
async def fffcaesar(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in src:
         return await message.reply_text("تم التعطيل من قبل🔒")
       src.append(message.chat.id)
       return await message.reply_text("تم تعطيل التسليه بنجاح ✅🔒")
    else:
       return await message.reply_text(f"يجب انت تكون ادمن للقيام بذلك 🎧")

@Client.on_message(filters.command(["فتح التسليه","تفعيل التسليه"], ""), group=7479003) 
async def caesarrf(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if not message.chat.id in src:
         return await message.reply_text("االتسليه مفعل من قبل ✅")
       src.remove(message.chat.id)
       return await message.reply_text("تم فتح التسليه بنجاح ✅🔓")
    else:
       return await message.reply_text(f"يجب انت تكون ادمن للقيام بذلك 🎧")
       
@Client.on_message(filters.command(["قتل","تخ"], ""), group=1025934)
async def ceev(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/a2c9fa6de45e0fc4fc81e.mp4",
          caption=f"• تم قتل هذا الشخص @{name}\n\n※ بواسطة @{CASER}\n\n ان لله وان اليه راجعون ⚰😭",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المقتول ⚰??", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("القاتل 👿🔪", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("اضف البوت الي مجموعتك 🎧", url=f"https://t.me/{bot_username}?startgroup=tru")]]))            
@Client.on_message(filters.command(["تفو","تف"], ""), group=105524)
async def ceev55(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/7f4c6eebf2f23b41dea45.mp4",
          caption=f"• تم التف علي هذا الشخص @{name}\n\n※ بواسطة @{CASER} \n\n اععع اي القرف ده 🤢",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المتفوف عليه😂💔", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("التافف 😂👻", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("اضف البوت الي مجموعتك 🎧", url=f"https://t.me/{bot_username}?startgroup=tru")]]))                                                                          
@Client.on_message(filters.command(["غنيلي","غني","• غنيلي •","غنيي","• اغاني •","اغاني"], ""), group=759363)
async def ih25d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/gukygn/{rl}"
    await client.send_voice(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)
    
@Client.on_message(filters.command(["بوسه","مح"], ""), group=1025554)
async def cee6v(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/f9fca108067895e042f1f.mp4",
          caption=f"••القميل هذا ✨♥ @{CASER}\n\n※ بعتلك بوسه يا 😘♥ @{name} \n\n عيب كده اي المحن ده 😹",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المقبول 👻??", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("القابل 😘🥹", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("اضف البوت الي مجموعتك 🎧", url=f"https://t.me/{bot_username}?startgroup=tru")]]))  

@Client.on_message(filters.command(["صوره","• صوره •","صورهه","صور","• صور •"], ""), group=715703)
async def ihd21(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 100)
    url = f"https://t.me/Caser_Rady_3/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["• متحركه •","متحركه"], ""), group=759033)
async def ih48d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)
    
@Client.on_message(filters.command(["❤️‍🔥انمي","انمي","• انمي •"], ""), group=724903)
async def i15hd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥صور بنات","صور بنات","• صور بنات •"], ""), group=763480)
async def ih467d(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 70)
    url = f"https://t.me/Caser_Rady_1/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["صور شباب","رمزيه","• صور شباب •"], ""), group=759073)
async def i378hd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(2, 70)
    url = f"https://t.me/Caser_Rady_2/{rl}"
    await client.send_photo(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["❤️‍🔥قران","قران","• قران •"], ""), group=758083)
async def ihd97(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(1, 90)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

@Client.on_message(filters.command(["استوري","استوريهات","• استوري •"], ""), group=755853) 
async def i803hd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
        return
    rl = random.randint(1, 50)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id, url, caption=f"➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @z1_1ax ˹🐉˼", parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)
    
    
@Client.on_message(filters.command(["الغاء تثبيت","غ ث"], ""), group=97365) 
async def unpin_message(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id  
        try:
            await client.unpin_chat_message(chat_id, message_id=reply_msg_id) 
            await message.reply_text("تم إلغاء تثبيت الرسالة بنجاح🌿❤️")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء إلغاء تثبيت الرسالة")
    else:
        await message.reply_text(f"بطل لعب يا {message.from_user.mention}\nلازم تكون ادمن🌿❤️ ")



 #..........................................   الردود       ................................................................
rdood = {}

@Client.on_message(filters.command(["قفل الردود","تعطيل الردود","قفل سمسمي","تعطيل سمسمي"], "") & filters.private,group=187637398)
async def abra245g(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
    rdood.setdefault(bot_username, []).append(bot_username)
    await message.reply_text(f"• تم قفل الردود بواسطه ↤︎「 {message.from_user.mention}")
    
@Client.on_message(filters.command(["فتح الردود","تفعيل الردود","فتح سمسمي","تفعيل سمسمي"], "") & filters.private,group=545177)
async def abr54ag(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
    rdood[bot_username].remove(bot_username)
    await message.reply_text(f"• تم فتح الردود بواسطه ↤︎「 {message.from_user.mention}")
       
rdod = []

@Client.on_message(filters.command(["قفل الردود","تعطيل الردود","قفل سمسمي","تعطيل سمسمي"], "") & filters.group, group=76373243) 
async def iddloc25k(client, message):
    bot_username = client.me.username    
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in rdod:
         return await message.reply_text("تم معطل من قبل🔒")
       rdod.append(message.chat.id)
       return await message.reply_text("تم تعطيل الردود بنجاح ✅🔒")
    else:
       return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@Client.on_message(filters.command(["فتح الردود","تفعيل الردود","فتح سمسمي","تفعيل سمسمي"], "") & filters.group, group=7062833) 
async def iddopen(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if not message.chat.id in rdod:
         return await message.reply_text("الردود مفعل من قبل ✅")
       rdod.remove(message.chat.id)
       return await message.reply_text("تم فتح الردود بنجاح ✅🔓")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
names = {} 

@Client.on_message(filters.text, group=57355566)
async def d5548on(client, message):
    if message.from_user is None or message.from_user.is_bot:
        return
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    me = names.get(bot_username) if names.get(bot_username) else f"{name}"
    hhs = client.me.username
    if hhs in rdood.get(hhs, []):
        return
    if message.chat.id in rdod:
        return  
    if any(keyword in message.text for keyword in ["عمري", "قلبي", "قلبى", "حياتي", "روحي", "بعشقك", "روحى", "حياتى", "عمرى", "قلبك", "قلبه", "بحبك", "بحبكم", "حبك", "حبيبكم", "حبيبي", "حبيبتي", "حبيبى", "حبيبتى", "عسل", "لف يو", "لفيو", "love","يقلبي"]):
         responses = ["وانت اكتر ياقلبى", "I love you", "وانا بعشقك بموت فيك", "ياروحي وانا اكتر احبك", "انا احبكم موت", "حبك اكتر ياروحي😍", "وانا بموت فيك🥰", "وانا كمان يقلبي😘", "عمري انت❤️", "عمري كلو ليك🫂", "انت عمري كلو🙈", "قلبي انت🩶", "انت قلبى🫂", "انت حبيب قلبي🖤", "قلبي من جوا❤️", "حياتي انت", "انت حياتي كلها", "حياتي انت", "طلعت روحك", "ونبي انت روحي", "روحي كلها انت", "انت العشق يبني", "انت العشق يقلبي", "أنا بعشقك اكتر", "انت العشق كده كده"]
         selected_response = random.choice(responses)
         await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["مح","بوسه","بوسة","محح","موح","قبله","قبلني","قبلتي","قبلنى","قبلتى","😘"]):
        responses = ["طب هات أنا كمان","لا انا زعلانه وانا وله عشان سيبك يعني","استغفرالله شواذ","بس عيب بتكسف","الحاجات دي مش هنا خليها ما بنا في البف","اي القرف دي اي بوسه دي","بحب المح بتاعتك😉"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["وحشتيني","وحشتوني","وحشني","وحشتونى","وحشنى","وحشتينى","وحشتني","وحشتنى","مفتقدك","افتقدتك","استفقدتك"]):
        responses = ["افتقدتك ي عمري ❤️‍🔥","اكتر ي عمري","وحشتني عيونك","مفتقدك جدا 🥺","انا ايضا افتقدك","وحشني روحك ♥","وحشتني متشفيش الوحش😂♥","وحشني اشتقتلك♥","وحشتني ليك وحشه ❤","وحش ميلهفك 😂😂","وحشني وربنا انت اكتر ❤","وحشني حبيب قلبي ❤","حبيب قلبي الي وحشني 🌚♥","وحشنا يوحش الكون ♥","وحشتني وحش اما يلهفك ❤","وحشتنا يعم❤","وحشنا ي غالي ♥","وحشني ي نبض قلبي 🌚","وحشتني ي عم فينك وفين لياليك💖","وحشني من زمان 💕","وحشتنا ي روحي ❣️","بحبك وحشتيني ♥","حبيبي وحشني ❤","وحشني ي نور عيني 👀"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["سيفي","عرفينا","سى فى","سي في","سيفى","عرفني","مين","سى في","سي فى"]):
        responses = ["ما تبط شقط بقا قرفتني 😂","مرتبطه جوزي قالي مش تقولي لحد","لا عوز تعرفني لي يعني 😎","مش برتبط فاهمك 😏","تدفع كام 😂❤️‍🔥","كفايه شقط سيب حاجه لغيرك 😂🌚","مريم 20 سنه من القاهره وانت عرفني عليك 🌚❤️‍🔥","اسمى: بنت ابويا،\n سني: عايشه من زمان\n سكنه ف بتنا وانت 😂🌚","انا قلبك ي قلبى ♥","هات بوسه وانا اقولك 😂"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["اسم", "اسمك", "اسمي", "نيمك", "نيم", "نيمي", "نيمى", "اسمى", "اسماء", "اسامي", "اسامى"]):
        responses = ["نبض قلب {name} يولا🌚🤍","روح قلب {name} من جوا 👀♥","{name} الحته 🤍🙃وانت",",""قول اسمك انت الاول ي جميل 😂♥","انا {name} الحته ي قلبي ❤🌚","{name} يحته ♥😂","انت مين انا الي ضاع من عمري سنين🙃🌚♥","وربنا اسمي {name} احلفلك باي يوه🤍👀","{name} يجردل😂🌚وانت","{name} الوتكه ي روحي 😌❤وانت اي ي عمري","{name} قلب الاسد ي عنيا 👀♥وانت","{name} الي محدش يقدر يتكلم  معاها ي عمري ♥🌚وانت","{name} يشبشب من لاه 😌😂🌚انت","{name} القلب الجاحد 🌚♥انت"]
        selected_response = random.choice(responses).format(name=me) 
        await message.reply_text(selected_response) 
    elif any(keyword in message.text for keyword in ["صباحو", "صباح","صبح","صبحو","صباحي","صباحى","'صباحك"]):
        responses = ["صباح الخير ي قلبي 😂♥","صباح ااخير علي التفاح ♥♥","صباح الورد والياسمين عليك يجميل 🤍🙃","صباح الخير ي عمري 🫂♥","صباح الخير ي روح قلبي 😂💖","صباح الورد علي الورد 🌺👀","صباح الياسمين علي عيون الجميل 👀😂","صباحك زي وشك 😂😁","صباحك منيل زيك ي منيل 😂🙃😁","اصتبحنا واصتبح الملك لله 😌🌚","اصتبحنا علي وشك يبقا يومنا من معدي 😁♥🌚","جتك نيله صباحك ابيض😁🤍","يسعدك صباحك ي خويا 😒😁😂🤍","صباحك ابيض يشق ♥🌚","صباحك عسل ي روحي ❤","صباح الورد عليك ي زميلي 🌺🌚❤","صباح الخيرات ي حبيب قلب اختك 🌚❤♥"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["مسا", "مساء","مسائو","تصبحو","تصباحو","ليله","ليلة","بليل","مسائى","مسائي","مساكم","مساهم","مساك","مسائها"]):
        responses = ["مسا مسا علي الناس الكويسه♥👀","مساء الخير ي قلبي ❤","مسا مسا عليك ي شق 🌚♥","مساك ابيض  ي زميلي 🤍👀","مساء الخير ي عمري 💖","يسعدك مساك ي خويا♥🌚","مساك مسا منيل 😁😌","كان نقصنا مساك واللهي 😂🙄","من غير مساك كنا نموت 🙄😒😂","مساء الفل 🌼","مساء النور علي لمبت حياتي 😂👀","مسا مسا علي الناس الي مش سالكه بربع جني 😂🌚🌚","مساك زي وشك👀♥♥","مساء الزفت علي دماغك 😂😁❤","مساء منيل بستين نيله 🙃♥","مساء مسا الرمان علي الرمان ❤🥂","مسا مسا علي الناس الي مش كويسه 😁😂😂♥"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)   
    elif any(keyword in message.text for keyword in ["سنك", "عمرك","سنه","عمركم","سنها","سنين","سنهم","عمر","عمرها","عمري"]):
        responses = ["عايشه من زمان اوي وانت😚","عندي 20 ياحب وانت 🩶","عندي 20 وانت ❤️","عارف بقالي سنين كتير اوي عايشه وانت☺️","قول انت كام الاول🙂","عندي 20 وانت برضو وله اكبر😇","عمري 20 ياعمري وانت😘","محدش بيسال السوال ده لي بت😒","أنا 20 وانت يا عمري😙","تعرف تعد لحد كام 😜","تعلا بف اقولك عندي كام🤭","بص يسطا السوال ده عيب لي اي بت","انت مالك😐","انت هتصحبني🥸","20 يامكنه وانت😉","20 يا قلب اختك وانت😍","20 يقلبي وانت😊","مش مهم مش دي الي هتحللك مشكلك😁","بص هو 20 وانا بقول 25 بس مشيها22👀😁","تعلا خاص وانا اقولك😉☺️"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)  
    elif any(keyword in message.text for keyword in ["منين","فينك","مكانك","مكان","وينك","من وين","من فين","مصر","القاهره","مدينه","مدينة","دوله","دولة","دولتي","مدينتي","مدينتى","دولتى"]):
        responses = ["من القاهره ي عمري وانت ❤🌚","من مصر ام الدنيا انت ♥👀","من قلب القاهره وانت 👤♥","منور القاهره واللهي🙂🤍","القاهره نورت بيك 😂♥","القاهره وانت 🙃💜","نورت القاهره ي شقي 🌚♥","انا القاهره انت😌❤","من القاهره يروحي وانت منين ❤","بلدي القاهره وانت 🙂♥","القاهره من غيرك ملهاش طعم انت منين بقا👀🌚♥","مصر منوره بيك وبيا 😌😂♥","من اجمد ناس القاهره انت بقا🙃♥","محافظه القاهره انت ❤","من مزز القاهره 😂♥انت","عايشه في شوارع مصر انت 😂🙃♥"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)       
    elif any(keyword in message.text for keyword in ["جيت","نورت","فينكم","هاي","هاى","اهلا","هلا","مرحبا","مرحب","مرحبآ","اهلاً","هلو","هايات"]):
        responses = ["نورت البيت ❤","منور 🌚","نورتنا ي غالي ♥","سمعني صوت عيارك💣","قوم فز افتح الباب 😂","يا مرحب بالغالي👀","اهلا وسهلا 🙂","تع تاني 🙃","ادخل واقفل الباب وراك😌","منورني والله 🤍","لو جبنا في سيره ربع جنيه مكنش جي ♥🌚😂","علي بالي جيت قولت اما اسال عليك ازيك 😂❤","سمعنا زغروطه بقا 😂🤍","شوف رايح فين بقا 🙄😂","كنت فين من بدري 🙃❤","اتصدق كنت علي بالي 😂💖","منورنا الوحش الي مبيرحمش 😂🌚","يادي النور يادي النور 😁❤"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["بخ", "عوو","رعب","خاف","اخاف","خوفت","رعبتني","رعبتنى","خضيتني","خفت","بخخ","عو"]):
        responses = ["يما خضيتني🔪😒","رعبتني يسطا🥸","خليت شعر ايدي يقف من الخضه😂","هو أنا المفرود كده اخاف واعيط😒","يخرابي رعبتني😂","بس لعب يا شاطر😁","يمامي خوفت 👍☺️","اعملها تاني واعمل نفسي هتخطيت😂","شغل الاطفال بقا هيقلي بخ وعو🙄","يمامي الحقيني خوفت🥸"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)       
    elif any(keyword in message.text for keyword in ["ريب", "نو ريب","توجيه","متبعتش","توجية"]):
        responses = ["هو أنا هعمل ريب علي الوزيره☺️","يبنتي انتي تطولي اصلا اعمل عليكي ريب😂","فوقي يا بت غيرك يتمنا مني الريب ده😂","انتي الي عامله ريب اصلا فوقي يقلبي😂","لا ونبي نفسي اعمل عليكي ريب يا بت😂","مش هعمل عليكي ريب يا ننسي عجرم😂","اهون مش اعمل عليكي ريب 😂😂","وغلاوت امي عملت فيا جميله😂","والنعمه أنا لو بكلم وزير الداخلية مش هيقولي كده😂"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)       
    elif any(keyword in message.text for keyword in ["ضحك","ضحكت","ههه","هههه","😂","🤣","😹","فصلت","فصلا","ضحكك","ضحكتي","ضحكتى","ضحكتك","😸","😁"]):
        responses = ["ضحك القمر 🌚","ضحكتك حلوه 😊","ضحكت يبقاا قلبها مال ☺️","ضحكتك عسل 😅😍","يخرابي ع الضحكه 😚","هو ده بجد 😳","أخيراً 😑","هي دي سنانك ولأ عقد لولي 😑😁","اقفلي بؤقك ليدخلك حاجه 😂","ساهله 😏","اتلمي 🔪","خفي ضحك 😒","بطلي توزعي ابتسامات علي الناس 🙂😡","هو إحنا هنا في كباريه ضحكتك واصله لآخر البار 🙂","عجبتني ضحكتك🌚♥","يدوم الضحك ي عمري❤👀","ضحكتك حلوه ي قلبي ♥","فصلا ضحك وربنا ❤😂","ضحكتك عسل ي روحي 🔥","احلي صوت سمعته صوت ضحكتك🫣♥","انا بصراحه فصلت ضحك مش قادره امسك نفسي من سعتها😂🌚♥","ضحك السنين بجد 😁??","فصلت فين الفيشه 🙃👀♥","يرب ضحكه عالطول 👀😂♥","اضحك بدل الهم الي الواحد في 😂❤","ايوا كدا فك مش تبوز ♥🌚","اضحك كدا متبقاش نكدي 💖😂","جتك نيله بتضحك علي خبتك 🙂♥","اضحك محدش واخد منها حاجه 🙃♥"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["بنات", "بنوته","بنوتة","بنت","بنوتي","بنوتى","بناتي","بناتى","بتت","بت"]):
        responses = ["بنت الاصول ي عمري ❤","بنت الاكابر ي قلبي ❤👏","بنات بس بميت راجل 😂😌","انا اجمل بنوته وربي 😂😌","احلي بنوته يخلاسي🙃♥","طول عمري بنت امي😂😁♥","بنات الجيه ي شق 🙃😂💖","البنات الطف الكائنات 😂💗","مفيش بنت احلي مني🤫💖♥","بنت الناس ي اتش🙄♥","انا بنوته مقطقطه ❤😂","بنت قلبي ي اخينه😂😌♥","وربي من غير البت دي الدنيا كانت اتقلبت😁♥","بنوته مسكره اوي 💗🌚","لقد وقعت في حب هذه البنات 🌚❤"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["توف", "تف","اتفو","تفه","تفة","تفاف","مقرف","معفن","القرف","عفن","زباله","زبالة","زفت","خرا","خره","معفنين"]):
        responses = ["تف علي وشك 😂","جتك الارف 😁👀","علي وشك ي حيوان 😂😁","جتك نيله عالم متختشيش😂🙃","يخرب بيت قرفك 😂💗","عالم مقرفه واللهي 😂","عليك ي معفن😂🌚💖","عيل مقرف جتك نيله 🙄😂","يععععع اي القرف دا 😒😁","في بوقك😁😂","علي شكلك يبعيد😂🙄","عليك ي جربان ي معفن😒♥😂","بعيد مش علينا غرقتنا جتك الارف😂😂😒","جتك الارف في شكلك😁❤🙄","عليك جتك نيله في شكلك الهباب😒♥😌😁"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)              
    elif any(keyword in message.text for keyword in ["اسكت","ويت","شششش","استني","استنى","اسكتي","اسكتى","اسكتو","سكته","شش","هوش"]):
        responses = ["محدش يسكتني اسكت براحتي","طب تمام تع واسكت معايه","غبي الملوك يتحدثون والغنم أمثالكم يسكتون.","لي كنت بتكلم من لسانك؟","شوف مين بيتكلم عن السكوت","طلعلك خس وبقيت تتكلم😏","ربي خلق لي لسان علشان أرد على أمثالك","حضرتك مش بتهش دبان","هشش دي لما نهش الكلاب الي زيك","ويت الله يرحم امك وابوك"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["بموت","متت","هموت","موت","موتي","موتى","موته","😵","⚰️","هموتت"]):
        responses = ["موت برا البار مش ناقصين مصيبه","يارب تموت ونخلص","امين","يسمع من بقك ربنا","يلا عشان نخلص","يارب تموت براحه","بعد الشر عليكي ياروحي","مع السلامه هنقرالك الفتحه"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["عياط","عياطي","عيط","دموع","😭","😥","😿","دموعى","دموعي","عيطي","عيطى","عياطى","دمعه","دمعتي","دمعتى","بكاء"]):
        responses = ["متعيطش 🥺","دموعك غاليه عليا 🥹","يلهوي القمر زعلان 😟","مين مات 🤨","مين ضربك 🧐","يلهوي عيون القمر بتعيط 😩","مين زعلك 🤨","اولع 😏","معاك للصبح 😒","متفرقش دموعك معايا 😒","في دموع تاني ولا خلاص خلصت 😒😟","امم أي كمان 😕","المفروض اعمل أي دلوقتي 😒","مليش في شغل المحن ده 🙂","تعيش وتعيط ي قمر 😅😁","أنت بدأت 😮‍💨🙄","اوووف بدأ القرف 🫨😬"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response)
    elif any(keyword in message.text for keyword in ["سلام","باى","باي","ماشي","ماشى","سلامات","بيباي","بيباى","🚶‍♀","🚶","🚶‍♂","🚶‍♀‍➡️","🚶‍➡️","🚶‍♂‍➡️","👩‍🦯","🧑‍🦯","👨‍🦯","👩‍🦯‍➡️","🧑‍🦯‍➡️","👨‍🦯‍➡️","🏃‍♀","🏃🏃‍♂","🏃‍♀‍➡️","🏃‍➡️","🏃‍♂‍➡️"]):
        responses = ["باي من غير سلام ❤😂","متسبنيش مقدرش من غيرك اعيش 😁❤","رايح فين 🌚🙃","خليك معانا♥","واللهي الدنيا وحشه من غيرك😂♥","متجيش تاني 😂","هتوحشنا يا غالي واللهي🙃♥","مشش في ركبك 😂🤍","غور في ستين داهيه 😁❤","ماشي ولا قاعد 👀😂","تمشي علي ضهرك 😁💖","يشلولك علي نقاله يبعيد 😂😌","هتمشي وتسبني 🙃❤","هتسبني طب لي 🥺❤","سلاموز بالموز حبايبي اللوز💜🌺","خد يلا هنا رايح فين 😂♥🌚"]     
        selected_response = random.choice(responses)
        await message.reply_text(selected_response) 
    elif any(keyword in message.text for keyword in ["بكرهك","مخصمك","خاصم","خصام","بكرهو","كرهك","كرهتك","مخصمكم","مبحبكش","مش بحبك","احبكش","قطوعه"]):
        responses = ["محدش طلب حبك في ناس احسن بتحبني 😋😀","اكبر دليل علي حب ربنا ليا انك بتكرهني 🥹","من امتي الخدم بيحبو اسيادهم 🙃😌","وانا اكتر ي عيوني 😉🤣","معروف الشياطين بتكره الملائكة 😌😚","حد قلك هموت من بعدك يعني 🤨😒","شايفني هموت عليك🙂‍↕️😏","نفس الاحساس🤩🤓","ومين قال اني بحبك🤗","انت بالزات لو حبتني هزعل😳🫨","مش محتاج لحبك 🥴🥱","حبك ميشرفنيش 😪","معلش معنديش وقت ابكي عليك 🤠","ميهمنيش حبك😮‍💨","كلما زاد عدد الكارهين قل عدد المنافقين من حياتي 🙄😬","وانا اكتر 😊","اخر همي انك تحبني اثلا🤓","كل واحد بيكره إللي كاسر عينك 😏🙄","فكرني هموت من بعدك ي محور الكون 🙀😼👩‍🎓","مش فارق معايا ☺️","علي الأقل مشتركين في نفس الشعور😏"]
        selected_response = random.choice(responses)
        await message.reply_text(selected_response) 
 #..........................................   الردود       ................................................................
 #..........................................   الردود   الثبته    ................................................................
@Client.on_message(filters.text & filters.group, group=54785566)
async def rady648on(client, message):
   bot_username = client.me.username
   soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
   if message.text in ["العاب","لعبه","لعبة","الالعاب"]:
       await message.reply_text(f" الالعاب 🕹: \n\n• لعبه `البنك`← لعرض اوامر لعبه البنك ارسل `البنك`\n\n• لعبه `اكس او` ←لبدا اللعبه ارسل `اكس او`\n\n• لعبه `حجرة` `ورقة` `مقص` ← لبدا العبه ارسل `حجرة` او `ورقه` او `مقص`\n\nلعبه `الجاسوس` ← لبدا العبه ارسل `الجاسوس`\n\nالغاز 🤔: \n← `ممثلين` ،  `مغنين` ،  `لاعبين` ،  `مشاهير` ،  `اعلام` ،  `افلام`\n← `مختلف` ،  `لغز`")
   elif message.text in ["الاجبار","الاشتراك الاجبار","الاشتراك"]:
       await message.reply_text(f"• الاشتراك الاجبار ✋← لا يمكن لاى شخص ان يكتب اى رساله دون ان يشترك ف القناه او الجروب المضافه ف الاشتراك الاجبار \n\n• ل `تفعيل الاشتراك `←يجب رفع البوت مشرف ف القناه او الجروب المطوب وضعه ف الاشتراك \n\n←ثم ارسال `تفعيل الاشتراك ` + رابط القناه او الجروب \n\n←مثلا: \n`تفعيل الاشتراك` {soesh}\n\n• لحذف قناه او جروب من الاشتراك\n\n←ارسل `تعطيل الاشتراك ` + رابط القناه او الجروب \n\n← مثلا: \n`تعطيل الاشتراك` {soesh}\n\nلعرض الاشتركات المضافه \n←ارسل `قنوات الاشتراك`")
   elif message.text in ["الرفع للترفيه","الرفع"]:
       await message.reply_text(f"الرفع: \n←`رفع اخ` ، `رفع اخت` ، `رفع بنتي` ، `رفع مراتي` ، `رفع زوجي` ، `رفع جدع` ، `رفع ابني` ، `رفع غبي` ، `رفع اهبل` \n← `رفع نمله`  ، `رفع صرصار` ، `رفع قرد` ، `رفع حمار` ، `رفع خنزير` ، `رفع عجل` ، `رفع كلب` ، `رفع خروف` ، `رفع جاموسه`\n← `رفع خول` ، `رفع متناك` ، `رفع عرص` ، `رفع نجس` ، `رفع ديوث` ،  `رفع شاذ`")       
   elif message.text in ["التنزيل للترفيه","التنزيل"]:
       await message.reply_text(f"التنزيل: \n←`تنزيل اخ` ، `تنزيل اخت` ، `تنزيل بنتي` ، `تنزيل مراتي` ، `تنزيل زوجي` ، `تنزيل جدع` ، `تنزيل ابني` ، `تنزيل غبي` ، `تنزيل اهبل` \n← `تنزيل نمله`  ، `تنزيل صرصار` ، `تنزيل قرد` ، `تنزيل حمار` ، `تنزيل خنزير` ، `تنزيل عجل` ، `تنزيل كلب` ، `تنزيل خروف` ، `تنزيل جاموسه` \n← `تنزيل خول` ، `تنزيل متناك` ، `تنزيل عرص` ، `تنزيل نجس` ، `تنزيل ديوث` ،  `تنزيل شاذ`")       
   elif message.text in ["مرفوعين","المرفوعين","لمرفوعين"]:
       await message.reply_text(f"المرفوعين: \n←`اخواتي` ، `اخوتي` ، `بناتي` ، `مراتاتي` ، `ازواجي` ، `ابنائي` ، `اغبياء` ، `الهبل` \n← `النمل` ، `الصارصير` ، `القرود` ، `الحمير` ، `الخنازير` ، `العجول` ، `الكلاب` ، `الخرفان` ، `الجواميس` \n← `الخولات` ، `المتناكين` ، `المعرصين` ، `النجسين` ، `الديوثين` ، `الشاذين`")       
   elif message.text in ["رمز","رموز","الرموز","الرمز"]:
       await message.reply_text("""
•𓃠 .𓅿 . 𓃠 . 𓃒 . 𓅰 . 𓃱∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿   ⎔ ⎕ ⎖ ⎗ ⎘ ⎙ ⎚ ⎛ ⎜ ⎝ ⎞  ⏞ ⏟ ⏠ ⏡ ⏢ ⏣ ⏤ ⏥ ⏦ ␋ ␢ ▫️ ▬ ▭ ▮ ▯ ▰ ▱ ▲ △ ▴ ▵ ▷ ▸ ▹ ► ▻ ▼ ▽ ▾ ▿  ◁ ◂ ◃ ◄ ◅ ◆ ◇ ◈ ◉ ◊ ○ ◌ ◍ ◎ ● ◐ ◑ ◒ ◓ ◔ ◔ʊ ◕  ◬ ◭ ◮ ◯ ◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷ ◸ ◹ ◺  ☓☠️ ☡☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟ ♠️ ♡ ♢  ♩ ♪ ♫ ♬ ♭ ♮ ♯ ♰ ♱ ♻️ ♼ ♽ ⚆ ⚇ ⚈ ⚉ ⚊ ⚋ ⚌ ⚍ ⚎ ⚏ ⚐ ⚑ ✐ ✑ ✒️ ✓ ✔️ ✕ ✖️ ✗ ✘ ✙ ✚ ✛ ✜  ✞ ✟ ✠ ✢ ✣ ✤ ✥ ✦ ✧ ✧♱ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰
 ✱ ✲  ✵ ✶ ✷ ✸ ✹ ✺  ❍ ❏ ❐ ❑ ❒ ❖  ❘ ❙ ❚ ❛ ❜ ❝ ❞ ❡ ❢  ❥ ❦ ❧ ❨ ❩ ❪ ❫ ❬ ❭ ❮ ❯ ❰ ❱ ❲ ❳ ❴ ❵ ➔ ➘  ➾ ⟀ ⟁ ⟂ ⟃ ⟄ ⟇ ⟈ ⟉ ⟊ ⟐ ⟑ ⟒ ⟓ ⟔ ⟕ ⟖ ⟗ ⟘ ⟙ ⟚ ⟛ ⟜ ⟝ ⟞ ⟟ ⟠ ⟡ ⟢ ⟣ ⟤ ⟥ ⟦ ⟧ ⟨ ⟩ ⟪ ⟫ ⟰ ⟱ ⟲ ⟳ ⟴ ⟵ ⟶ ⟷ ⟸ ⟹ ⟺ ⟻ ⟼ ⟽ ⟾ ⟿ ⤀ ⤦ ⤧ ⤨ ⤩ ⤪ ⤫ ⤬ ⤭ ⤮ ⤯ ⤰ ⤱ ⤲ ⤳ ⤶ ⤷ ⤸ ⤹ ⤺ ⤻ ⤼ ⤽ ⤾ ⤿ ⥀ ⥁ ⥂ ⥃ ⥄ ⥅ ⥆ ⥇ ⥈ ⥉ ⥊ ⥋ ⥌ ⥍ ⥎ ⥏ ⥐ ⥑ ⥒ ⥓ ⥔ ⥕ ⥖ ⥗ ⥘ ⥙ ⥚ ⥛ ⥜ ⥝ ⥞ ⥟ ⥠ ⥡ ⥢ ⥣ ⥤ ⥥ ⥦ ⥧ ⥨ ⥩ ⥪ ⥫ ⥬ ⥭ ⥮ ⥯ ⥰ ⥱ ⥲ ⥳ ⥴ ⥵ ⥶ ⥷ ⥸ ⥹ ⥺ ⥻ ⥼ ⥽ ⥾ ⥿ ⦀ ⦁ ⦂ ⦃ ⦄ ⦅ ⦆ ⦇ ⦈ ⦉ ⦊ ⦋ ⦌ ⦍ ⦎ ⦏ ⦐ ⦑ ⦒ ⦓ ⦔ ⦕ ⦖ ⦗ ⦘ ⦙ ⦚ ⦛ ⦜ ⦝ ⦞ ⦟ ⦠ ⦡ ⦢ ⦣ ⦤ ⦥ ⦦ ⦧ ⦨ ⦩ ⦪ ⦫ ⦬ ⦭ ⦮ ⦯ ⦰ ⦱ ⦲ ⦳ ⦴ ⦵ ⦶ ⦷ ⦸ ⦹ ⦺ ⦻ ⦼ ⦽ ⦾ ⦿ ⧀ ⧁ ⧂ ⧃ ⧄ ⧅ ⧆ ⧇ ⧈ ⧉ ⧊ ⧋ ⧌ ⧍ ⧎ ⧏ ⧐ ⧑ ⧒ ⧓ ⧔ ⧕ ⧖ ⧗ ⧘ ⧙ ⧚ ⧛ ⧜ ⧝ ⧞ ⧟ ⧡ ⧢ ⧣ ⧤ ⧥ ⧦ ⧧ ⧨ ⧩ ⧪ ⧫ ⧬ ⧭ ⧮ ⧯ ⧰ ⧱ ⧲ ⧳ ⧴ ⧵ ⧶ ⧷ ⧸ ⧹ ⧺ɷ""")
       await message.reply_text("""ᾋ ᾌ ᾍ ᾎ ᾏ ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ ᾰ ᾱ ᾲ ᾳ ᾴ ᾶ ᾷ Ᾰ Ᾱ Ὰ Ά ᾼ ᾽ ι ᾿ ῀ ῁ ῂ ῃ ῄ ῆ ῇ Ὲ Έ Ὴ Ή ῌ ῍ ῎ ῏ ῐ ῑ ῒ ΐ ῖ ῗ Ῐ Ῑ Ὶ Ί ῝ ῞ ῟ ῠ ῡ ῢ ΰ ῤ ῥ ῦ ῧ Ῠ Ῡ Ὺ Ύ Ῥ ῭ ΅ ` ῲ ῳ ῴ ῶ ῷ Ὸ Ό Ὼ Ώ ῼ ´ ῾ ῿ ‐ ‑ ‒ – — ― ‖ ‗ ‘ ’ ‚ ‛ “ ” „ ‟ † ‡ • ‣ ․ ‥ … ‧       ‰ ‱ ′ ″ ‴ ‵ ‶ ‷ ‸ ‹ › ※ ‼️ ‽ ‾ ‿ ⁀ ⁁ ⁂ ⁃ ⁄ ⁅ ⁆ ⁇ ⁈ ⁉️ ⁊ ⁋ ⁌ ⁍ ⁎ ⁏ ⁐ ⁑ ⁒ ⁓ ⁔ ⁕ ⁖ ⁗ ⁘ ⁙ ⁚ ⁛ ⁜ ⁝ ⁞ ⁮ ⁯ ⁰ ⁱ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁿ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₐ ₑ ₒ ₓ ₕ ₖ ₗ ₘ ₙ ₚ ₛ ₜ ₝ ₞ ₟ ₠ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ € ₭ ₮ ₯ ₰ ₱ ₲ ₳ ₴ ₵ ℀ ℁ ℂ ℃ ℄ ℅ ℆ ℇ ℈ ℉ ℊ ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ ℔ ℕ № ℗ ℘ ℙ ℚ ℛ ℜ ℝ ℞ ℟ ℠ ℡ ™ ℣ ℤ ℥ Ω ℧ ℨ ℩ K Å ℬ ℭ ℮ ℯ ℰ ℱ Ⅎ ℳ ℴ ℵ ℶ ℷ ℸ ℹ️ ℺ ℻ ℼ ℽ ℾ ℿ ⅀ ⅁ ⅂ ⅃ ⅄ ⅅ ⅆ ⅇ ⅈ ⅉ ⅊ ⅋ ⅌ ⅍ ⅎ ⅏ ⅐ ⅑ ⅒ ⅓ ⅔ ⅕ ⅖ ⅗ ⅘ ⅙ ⅚ ⅛ ⅜ ⅝ ⅞ ↀ ↁ ↂ Ↄ ↉ ↊ ↋ ← ↑ → ↓ ↔️ ↕️ ↖️ ↗️ ↘️ ↙️ ↚ ↛ ↜ ↝ ↞ ↟ ↠ ↡ ↢ ↣ ↤ ↥ ↦ ↧ ↨ ↩️ ↪️ ↫ ↬ ↭ ↮ ↯ ↰ ↱ ↲ ↳ ↴ ↵ ↶ ↷ ↸ ↹ ↺ ↻ ↼ ↽ ↾ ↿ ⇀ ⇁ ⇂ ⇃ ⇄ ⇅ ⇆ ⇇ ⇈ ⇉ ⇊ ⇋ ⇌ ⇍ ⇎ ⇏ ⇐ ⇑ ⇒ ⇓ ⇔ ⇕ ⇖ ⇗ ⇘ ⇙ ⇚ ⇛ ⇜ ⇝ ⇞ ⇟ ⇠ ⇡ ⇢ ⇣ ⇤ ⇥ ⇦ ⇧ ⇨ ⇩ ⇪ ⇫ ⇬ ⇭ ⇮ ⇯ ⇰ ⇱ ⇲ ⇳ ⇴ ⇵ ⇶ ⇷ ⇸ ⇹ ⇺ ⇻ ⇼ ⇽ ⇾ ⇿ ∀ ∁ ∂ ∃ ∄ ∅ ∆ ∇ ∈ ∉ ∊ ∋ ∌ ∍ ∎ ∏ ∐ ∑ − ∓ ∔ ∕ ∖ ∗ ∘ ∙ √ ∛ ∜ ∝ ∞ ∟ ∠ ∡ ∢ ∣ ∤ ∥ ∦ ∧ ∨ ∩ ∪ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿ ⋀ ⋁ ⋂ ⋃ ⋄ ⋅ ⋆ ⋇ ⋈ ⋉ ⋊ ⋋ ⋌ ⋍ ⋎ ⋏ ⋐ ⋑ ⋒ ⋓ ⋔ ⋕ ⋖ ⋗ ⋘ ⋙ ⋚ ⋛ ⋜ ⋝ ⋞ ⋟ ⋠ ⋡ ⋢ ⋣ ⋤ ⋥ ⋦ ⋧ ⋨ ⋩ ⋪ ⋫ ⋬ ⋭ ⋮ ⋯ ⋰ ⋱ ⋲ ⋳ ⋴ ⋵ ⋶ ⋷ ⋸ ⋹ ⋺ ⋻ ⋼ ⋽ ⋾ ⋿ ⌀ ⌁ ⌂ ⌃ ⌄ ⌅ ⌆ ⌇ ⌈ ⌉ ⌊ ⌋ ⌌ ⌍ ⌎ ⌏ ⌐ ⌑ ⌒ ⌓ ⌔ ⌕ ⌖ ⌗ ⌘ ⌙ ⌚️ ⌛️ ⌜ ⌝ ⌞ ⌟ ⌠ ⌡ ⌢ ⌣ ⌤ ⌥ ⌦ ⌧ ⌨️ 〈 〉 ⌫ ⌬ ⌭ ⌮ ⌯ ⌰ ⌱ ⌲ ⌳ ⌴ ⌵ ⌶ ⌷ ⌸ ⌹ ⌺ ⌻ ⌼ ⌽ ⌾ ⌿ ⍀ ⍁ ⍂ ⍃ ⍄ ⍅ ⍆ ⍇ ⍈ ⍉ ⍊ ⍋ ⍌ ⍍ ⍎ ⍏ ⍐ ⍑ ⍒ ⍓ ⍔ ⍕ ⍖ ⍗ ⍘ ⍙ ⍚ ⍛ ⍜ ⍝ ⍞ ⍟ ⍠ ⍡ ⍢ ⍣ ⍤ ⍥ ⍦ ⍧ ⍨ ⍩ ⍪ ⍫ ⍬ ⍭ ⍮ ⍯ ⍰ ⍱ ⍲ ⍳ ⍴ ⍵ ⍶ ⍷ ⍸ ⍹ ⍺ ⍻ ⍼ ⍽ ⍾ ⍿ ⎀ ⎁ ⎂ ⎃ ⎄ ⎅ ⎆ ⎇ ⎈ ⎉ ⎊ ⎋ ⎌ ⎍ ⎎ ⎏ ⎐ ⎑ ⎒ ⎓ ⎔ ⎕ ⎖ ⎗ ⎘ ⎙ ⎚ ⎛ ⎜ ⎝ ⎞ ⎟ ⎠ ⎡ ⎢ ⎣ ⎤ ⎥ ⎦ ⎧ ⎨ ⎩ ⎪ ⎫ ⎬ ⎭ ⎮ ⎯ ⎰ ⎱ ⎲ ⎳ ⎴ ⎵ ⎶ ⎷ ⎸ ⎹ ⎺ ⎻ ⎼ ⎽ ⎾ ⎿ ⏀ ⏁ ⏂ ⏃ ⏄ ⏅ ⏆ ⏇ ⏈ ⏉ ⏋ ⏌ ⏍ ⏎ ⏏️ ⏐ ⏑ ⏒ ⏓ ⏔ ⏕ ⏖ ⏗ ⏘ ⏙ ⏚ ⏛ ⏜ ⏝ ⏞ ⏟ ⏠ ⏡ ⏢ ⏣ ⏤ ⏥ ⏦ ␋ ␢ ␣ 
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼ ⑽ ⑾ ⑿ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙ ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵ Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ️ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ ⓪ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴ ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽ ⓾ ⓿ ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏ ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟ ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯ ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿ ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏ ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ ╬﹌ ╭ ╮ ╯ ╰ ╰☆╮ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿ ▀ ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ ▊ ▋ ▌ ▍ ▎ ▏ ▐ ░ ▒ ▓ ▔ ▕ ▖ ▗ ▘ ▙ ▚ ▛ ▜ ▝ ▞ ▟ ■ □ ▢ ▣ ▤ ▥ ▦ ▧ ▨ ▩ ▪️ ▫️ ▬ ▭ ▮ ▯ ▰ ▱ ▲ △ ▴ ▵ ▷ ▸ ▹ ► ▻ ▼ ▽ ▾ ▿  ◁ ◂ ◃ ◄ ◅ ◆ ◇ ◈ ◉ ◊ ○ ◌ ◍ ◎ ● ◐ ◑ ◒ ◓ ◔ ◔ʊ ◕ ◖ ◗ ◘ ◙ ◚ ◛ ◜ ◝ ◞ ◟ ◠ ◡ ◢ ◣ ◤ ◥ ◦ ◧ ◨ ◩ ◪ ◫ ◬ ◭ ◮ ◯ ◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷ ◸ ◹ ◺  ☓☠️ ☡☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟ ♠️ ♡ ♢  ♩ ♪ ♫ ♬ ♭ ♮ ♯ ♰ ♱ ♻️ ♼ ♽ ⚆ ⚇ ⚈ ⚉ ⚊ ⚋ ⚌ ⚍ ⚎ ⚏ ⚐ ⚑ ✐ ✑ ✒️ ✓ ✔️ ✕ ✖️ ✗ ✘ ✙ ✚ ✛ ✜  ✞ ✟ ✠ ✢ ✣ ✤ ✥ ✦ ✧ ✧♱ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰ ✱ ✲  ✵ ✶ ✷ ✸ ✹ ✺ ✻ ✼ ✽ ✾ ✿ ❀ ❁ ❂ ❃ ❄️ ❅ ❆ ❈ ❉ ❊ ❋ ❍ ❏ ❐ ❑ ❒ ❖ ❗️ ❘ ❙ ❚ ❛ ❜ ❝ ❞ ❡ ❢ ❣️ ❤️ ❥ ❦ ❧ ❨ ❩ ❪ ❫ ❬ ❭ ❮ ❯ ❰ ❱ ❲ ❳ ❴ ❵ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿ ➀ ➁ ➂ ➃ ➄ ➅ ➆ ➇ ➈ ➉ ➊ ➋ ➌ ➍ ➎ ➏ ➐➑ ➒ ➓ ➔ ➘ ➙ ➚ ➛ ➜ ➝ ➞ ➟ ➠  ➢ ➣ ➤ ➥ ➦ ➧ ➨ ➩ ➪ ➫ ➬ ➭ ➮ ➯ ➱ ➲ ➳ ➴ ➵ ➶ ➷ ➸ ➹ ➺ ➻ ➼ ➽ ➾ ⟀ ⟁ ⟂ ⟃ ⟄ ⟇ ⟈ ⟉ ⟊ ⟐ ⟑ ⟒ ⟓ ⟔ ⟕ ⟖ ⟗ ⟘ ⟙ ⟚ ⟛ ⟜ ⟝ ⟞ ⟟ ⟠ ⟡ ⟢ ⟣ ⟤ ⟥ ⟦ ⟧ ⟨ ⟩ ⟪ ⟫ ⟰ ⟱ ⟲ ⟳ ⟴ ⟵ ⟶ ⟷ ⟸ ⟹ ⟺ ⟻ ⟼ ⟽ ⟾ ⟿ ⤀ ⤁ ⤂ ⤃ ⤄ ⤅ ⤆ ⤇ ⤈ ⤉ ⤊ ⤋ ⤌ ⤍ ⤎ ⤏ ⤐ ⤑ ⤒ ⤓ ⤔ ⤕ ⤖ ⤗ ⤘ ⤙ ⤚ ⤛ ⤜ ⤝ ⤞ ⤟ ⤠ ⤡ ⤢ ⤣ ⤤ ⤥ ⤦ ⤧ ⤨ ⤩ ⤪ ⤫ ⤬ ⤭ ⤮ ⤯ ⤰ ⤱ ⤲ ⤳ ⤶ ⤷ ⤸ ⤹ ⤺ ⤻ ⤼ ⤽ ⤾ ⤿ ⥀ ⥁ ⥂ ⥃ ⥄ ⥅ ⥆ ⥇ ⥈ ⥉ ⥊ ⥋ ⥌ ⥍ ⥎ ⥏ ⥐ ⥑ ⥒ ⥓ ⥔ ⥕ ⥖ ⥗ ⥘ ⥙ ⥚ ⥛ ⥜ ⥝ ⥞ ⥟ ⥠ ⥡ ⥢ ⥣ ⥤ ⥥ ⥦ ⥧ ⥨ ⥩ ⥪ ⥫ ⥬ ⥭ ⥮ ⥯ ⥰ ⥱ ⥲ ⥳ ⥴ ⥵ ⥶ ⥷ ⥸ ⥹ ⥺ ⥻ ⥼ ⥽ ⥾ ⥿ ⦀ ⦁ ⦂ ⦃ ⦄ ⦅ ⦆ ⦇ ⦈ ⦉ ⦊ ⦋ ⦌ ⦍ ⦎ ⦏ ⦐ ⦑ ⦒ ⦓ ⦔ ⦕ ⦖ ⦗ ⦘ ⦙ ⦚
 ⦛ ⦜ ⦝ ⦞ ⦟ ⦠ ⦡ ⦢ ⦣ ⦤ ⦥ ⦦ ⦧ ⦨ ⦩ ⦪ ⦫ ⦬ ⦭ ⦮ ⦯ ⦰ ⦱ ⦲ ⦳ ⦴ ⦵ ⦶ ⦷ ⦸ ⦹ ⦺ ⦻ ⦼ ⦽ ⦾ ⦿ ⧀ ⧁ ⧂ ⧃ ⧄ ⧅ ⧆ ⧇ ⧈ ⧉ ⧊ ⧋ ⧌ ⧍ ⧎ ⧏ ⧐ ⧑ ⧒ ⧓ ⧔ ⧕ ⧖ ⧗ ⧘ ⧙ ⧚ ⧛ ⧜ ⧝ ⧞ ⧟ ⧡ ⧢ ⧣ ⧤ ⧥ ⧦ ⧧ ⧨ ⧩ ⧪ ⧫ ⧬ ⧭ ⧮ ⧯ ⧰ ⧱ ⧲ ⧳ ⧴ ⧵ ⧶ ⧷ ⧸ ⧹ ⧺ɷ""")
   elif message.text in ["تحميل","نزل","يوتيوب","حمل","تنزل","تنزيل"]:
       await message.reply_text(f"ادخل البوت واكتب `تحميل` او `تنزيل` @{bot_username}")        
#..........................................   الردود   الثبته    ................................................................


@Client.on_message(filters.command(["تثبيت", "ث"], ""), group=97354) 
async def pin_message(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id
        try:
            await client.pin_chat_message(chat_id, reply_msg_id)
            await message.reply_text("تم تثبيت الرسالة بنجاح🌿❤️")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء تثبيت الرسالة.")
    else:
        await message.reply_text(f"بطل لعب يا {message.from_user.mention}\nلازم تكون ادمن🌿❤️")

lkk = [
"لو خيروك |  بين الذهاب إلى الماضي والعيش مع جدك أو بين الذهاب إلى المستقبل والعيش مع أحفادك؟",
"لو خيروك |  بين الاستماع إلى الأخبار الجيدة أولًا أو الاستماع إلى الأخبار السيئة أولًا؟",
"تذبح نفسك او تاكل عشره كأس صاص  حااااااار",
"لو خيروك بين نشر 25 رقم من سجل مكالماتك وبين نشر آخر 25 صورة قمت بالتقاطها.",
"يكون عندك سرعة الفهد او ذكاء الثعلب",
"لو خيروك |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟",
"لو خيروك |  بين أن تمتلك زر إيقاف موقت للوقت أو أن تمتلك أزرار للعودة والذهاب عبر الوقت؟",
"لو خيروك |  بين القفز بمظلة من طائرة أو الغوص في أعماق البحر؟",
"لو خيروك |  بين خسارة حبيبك/حبيبتك أو خسارة أخيك/أختك؟",
"لو خيروك |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟",
"ترقص في سطح البيت او تغني بصوت عالي من الشباك",
"لو خيروك بين القدرة على كشف كذب الجميع أو القدرة على الكذب بدون أن يتم كشف كذبتك أبدًا.،",
"لو خيروك |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟",
"لو خيروك |  بين أن تكون رئيس لشركة فاشلة أو أن تكون موظف في شركة ناجحة؟",
"لو خيروك |  بين تناول البيتزا وبين الايس كريم وذلك بشكل دائم؟",
"لو خيروك |  بين الخروج بالمكياج بشكل مستمر وبين الحصول على بشرة صحية ولكن لا يمكن لك تطبيق أي نوع من المكياج؟",
"لو خيروك بين الصداقة والحب",
"تزور المستقبل او تزور الماضي",
"لو خيروك |  بين قص شعرك بشكل قصير جدًا أو صبغه باللون الوردي؟",
"لو خيروك |  بين استمرار فصل الشتاء دائمًا أو بقاء فصل الصيف؟",
"لو خيروك |  بين تلوين شعرك كل خصلة بلون وبين ارتداء ملابس غير متناسقة لمدة أسبوع؟",
"تدرس الحاجة اللي بتحبها بس مش هتلاقي وظيفة او تدرس حاجة مبتحبهاش بس يكون عندك وظيفة بمرتب كبير",
"لو خيروك بين تناول الخضار والفاكهة طوال حياتك أو تناول اللحوم.",
"لو خيروك |  بين أن تكون اللاعب الأفضل في فريق كرة فاشل أو أن تكون لاعب عادي في فريق كرة ناجح؟",
"لو خيروك |  بين قول الحقيقة والصراحة الكاملة مدة 24 ساعة أو الكذب بشكل كامل مدة 3 أيام؟",
"كتابة 50 صفحة كاملة او حل 10 مسائل رياضيات",
"لو خيروك |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟",
"لو خيروك بين إنقاذ نفسك أو إنقاذ شخص وقد يعرضك ذلك للأذى.",
"لو خيروك |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟",
"لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟",
"لو خيروك |  بين امتلاك قطة أو كلب؟",
"لو خيروك بين القدرة على سماع أفكار الناس أو القدرة على العودة في الزمن للخلف."
"لو خيروك |  بين العيش في دراما قد سبق وشاهدتها ماذا تختارين بين الكوميديا والتاريخي؟",
"لو خيروك |  بين زوجتك وابنك/ابنتك؟",
"لو خيروك |  بين التحدث عن كل شيء يدور في عقلك وبين عدم التحدث إطلاقًا؟",
"لو خيروك |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟",
"لو خيروك |  بين مشاهدة كرة القدم أو متابعة الأخبار؟",
"لو كنت شخص اخر هل تفضل البقاء معك أم أنك ستبتعد عن نفسك؟",
"لو خيروك |  بين خسارة حبيبك/حبيبتك أو خسارة أخيك/أختك؟",
"لو خيروك |  بين اللعب مع الأطفال لمدة 7 ساعات أو الجلوس دون فعل أي شيء لمدة 24 ساعة؟",
"القدرة على التحكم في الوقت او القدرة على التحكم في الماء",
"لو خيروك بين امتلاك سرعة الفهد أو دهاء الثعلب.",
"تروح مكان بتحبه مع شخص بتكرهه او تروح مكان مش بتحبه مع شخص بتحبه",
"لو خيروك |  بين الخروج بالمكياج بشكل مستمر وبين الحصول على بشرة صحية ولكن لا يمكن لك تطبيق أي نوع من المكياج؟",
"لو خيروك |  بين القفز بمظلة من طائرة أو الغوص في أعماق البحر؟",
"لو خيروك |  بين طباخ أو خياط؟",
"لو خيروك |  بين أن تتعطل سيارتك في نصف الطريق أو ألا تتمكنين من ركنها بطريقة صحيحة؟",
"لو خيروك بين القدرة على الاختفاء أو القدرة على الطيران.",
"لو خيروك |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟",
"لو خيروك |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟",
"لو خيروك بين القدرة على الاختفاء أو القدرة على الطيران.",
"لو خيروك |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟",
"لو خيروك |  بين إمكانية تواجدك في الفضاء وبين إمكانية تواجدك في البحر؟",
"لو خيروك |  بين أن تضع الكثير من الملح على كل الطعام بدون علم أحد، أو أن تقوم بتناول شطيرة معجون أسنان؟",
"لو خيروك |  بين مصور فوتوغرافي جيد وبين مصور سيء ولكنه عبقري فوتوشوب؟", 
"نت مجاني او اكل مجاني",
"لو خيروك |  بين امتلاك كل عين لون وبين امتلاك نمش على خديك؟",
"لو خيروك |  بين إجراء المكالمات الهاتفية فقط أو إرسال الرسائل النصية فقط؟",
"لو خيروك |  بين تغيير وظيفتك كل سنة أو البقاء بوظيفة واحدة طوال حياتك؟",
"لو خيروك |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟",
"لو خيروك |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟",
"لو خيروك |  بين القفز بمظلة من طائرة أو الغوص في أعماق البحر؟",
"لو خيروك |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟",
"لو خيروك بين أن تعيش في القرن الرابع عشر أو القرن الحالي.",
"لو خيروك |  بين أن يكون طولك 150 سنتي متر أو أن يكون 190 سنتي متر؟",
"لو خيروك |  بين أن يكون لديك جيران صاخبون أو أن يكون لديك جيران فضوليون؟",
"لو خيروك بين القدرة على كشف كذب الجميع أو القدرة على الكذب بدون أن يتم كشف كذبتك أبدًا.",
"فلوس لا محدودة او وقت لا محدود",
"زيارة الأهرامات او زيارة برج ايفل", 
"تقول اي حاجة تيجي في بالك او متتكلمش طول عمرك؟",
"لو خيروك |  بين أن تتكلم بالهمس فقط طوال الوقت أو أن تصرخ فقط طوال الوقت؟",
"لو خيروك |  بين تزيين طبق السلطة بالبرتقال وبين إضافة البطاطا لطبق الفاكهة؟", 
"لو خيروك |  بين العمل الذي تحلم به أو بين إيجاد شريك حياتك وحبك الحقيقي؟",
"لو خيروك |  بين أن تكون كل ملابس بمقاس واحد كبير الحجم أو أن تكون جميعها باللون الأصفر؟",
"لو خيروك |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟",
"لو خيروك |  بين القفز بمظلة من طائرة أو الغوص في أعماق البحر؟",
"لو خيروك |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟",
"تعتذر على غلطة معملتهاش مقابل استمرار علاقتك مع حد بتحبه او متعتذرش وتخسر الشخص دا؟",
"لو خيروك بين الصداقة والحب",
"لو خيروك |  بين رجل أعمال أو أمير؟",
"لو خيروك |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟",
"لو خيروك |  يبن صديقك البعيد وبين زميلك القريب؟",
"لو خيروك |  بين أن تكون غني وتعيش قبل 500 سنة، أو أن تكون فقير وتعيش في عصرنا الحالي؟",
"تحط لبانة في شعرك او تاكل لبانة كانت ف بؤق حد غيرك",
"لو خيروك بين امتلاك سرعة الفهد أو دهاء الثعلب.",
"لو خيروك |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟",
"لو خيروك |  بين أن تعيش بدون موسيقى أبدًا أو أن تعيش بدون تلفاز أبدًا؟",
"لو خيروك |  بين نفسك وأمك؟",
"لو خيروك بين نشر 25 رقم من سجل مكالماتك وبين نشر آخر 25 صورة قمت بالتقاطها.",
"تعمل 100 ضغط او تجري 3 كيلومتر",
"لو خيروك |  بين جدك أو جدتك؟",
"لو خيروك |  بين زوجتك وابنك/ابنتك؟",
"تضرب بالقلم كل يوم او تاكل بيضة نية كل يوم",
"لو خيروك بين العيش بجانب الجبال والحدائق والأشجار أو العيش بجانب البحر.",
"لو خيروك |  بين أخيك البعيد أو جارك القريب؟",
"لو خيروك |  بين تناول مياه غازية مجمدة وبين تناولها ساخنة؟",
"لو خيروك |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟",
"لو خيروك |  بين أن تكون كل ملابس بمقاس واحد كبير الحجم أو أن تكون جميعها باللون الأصفر؟",
"تكون اكثر شخص ذكي في العالم او تكون اكثر شخص محظوظ في العالم؟",
"لو خيروك بين الجمال أو الذكاء.",
"لو خيروك |  بين أن تكون كل ملابس بمقاس واحد كبير الحجم أو أن تكون جميعها باللون الأصفر؟",
"لو خيروك |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟",
"لو خيروك |  بين مشاهدة فيلم بمفردك أو الذهاب إلى مطعم وتناول العشاء بمفردك؟",
"لو خيروك |  بأن لا يحضر أحد إما لحفل زفافك أو إلى جنازتك؟",
"لو خيروك بين رؤية الأشباح فقط أو سماع صوتها فقط.",
"تصرخ في الشارع بصوت عالي او تضرب اول حد تشوفه بالقلم",
"لو خيروك |  بين زميل ناجح وحده أو زميل يعمل كفريق؟",
"لو خيروك |  بين إنهاء الحروب في العالم أو إنهاء الجوع في العالم؟",
"لو خيروك بين تناول الخضار والفاكهة طوال حياتك أو تناول اللحوم.",
"لو خيروك |  بين أن تضع الكثير من الملح على كل الطعام بدون علم أحد، أو أن تقوم بتناول شطيرة معجون أسنان؟",
"لو خيروك |  بين مصور فوتوغرافي جيد وبين مصور سيء ولكنه عبقري فوتوشوب؟",
"رحلة ف الفضاء او رحلة حول العالم؟",
"لو خيروك بين أن تكون أقوى شخص في العالم أو أذكى شخص في العالم.",
"لو خيروك |  بين طباخ أو خياط؟",
"لو خيروك |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟",
"لو خيروك |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟",
"تكون سريع او تكون قوي؟",
"لو خيروك بين القدرة على الاختفاء أو القدرة على الطيران.",
"لو خيروك |  بين أن تكون اللاعب الأفضل في فريق كرة فاشل أو أن تكون لاعب عادي في فريق كرة ناجح؟",
"تشتري عربية شكلها مش جميل بس سريعة او عربية جميلة بس بطيئة",
"لو خيروك بين تناول الخضار والفاكهة طوال حياتك أو تناول اللحوم.",
"تذبح نفسك او تاكل عشره كأس صاص  حااااااار",
"لو خيروك |  بين أن تتعطل سيارتك في نصف الطريق أو ألا تتمكنين من ركنها بطريقة صحيحة؟",
"لو خيروك |  بين البكاء والحزن وبين اكتساب الوزن؟",
"لو خيروك بين الاعتذار عن خطأ اقترفته أو أن يقدم لك شخص أخطأ في حقق اعتذار.",
"لو خيروك |  بين امتلاك قدرة التحدث بكل لغات العالم أو التحدث إلى الحيوانات؟",
"لو خيروك |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟",
"الاهلي أو الزمالك؟",
"لو خيروك بين المال أو الصحة.",
"لو خيروك |  بين العيش في القارة القطبية أو العيش في الصحراء؟",
"تكون في منصب كبير او تلاقي الحب الحقيقي؟",
"لو خيروك |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟",
"لو خيروك |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟",
"لو خيروك |  بين قول الحقيقة والصراحة الكاملة مدة 24 ساعة أو الكذب بشكل كامل مدة 3 أيام؟", 
"لو خيروك |  بين أن تعيش بدون موسيقى أبدًا أو أن تعيش بدون تلفاز أبدًا؟",
"تقول الحقيقة ويحصلك مشاكل او تكدب وتاخد فلوس؟",
"لو خيروك بين نشر 25 رقم من سجل مكالماتك وبين نشر آخر 25 صورة قمت بالتقاطها.",
"لو خيروك |  يبن صديقك البعيد وبين زميلك القريب؟",
"لو خيروك |  بين أخيك البعيد أو جارك القريب؟",
"لو خيروك |  بين امتلاك قطة أو كلب؟",
"لو خيروك |  بين امتلاك قطة أو كلب؟",
"تكمل في علاقة مع حد بتحبه بس قدامكم عقبات كتير او مع حد مش بتحبه بس من غير عقبات في طريقكم؟",
"لو خيروك بين الصداقة والحب؟",
"لو خيروك |  بين أن تصبحي عارضة أزياء وبين ميك اب أرتيست؟",
"لو خيروك |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟",
"لو خيروك |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟",
"لو خيروك |  بين مشاهدة فيلم بمفردك أو الذهاب إلى مطعم وتناول العشاء بمفردك؟",
"لو خيروك |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟",
"لو خيروك |  بين قص شعرك بشكل قصير جدًا أو صبغه باللون الوردي؟",
"لو خيروك بين الذكاء أو الصحة.",
"تكون صاحب عمل حر او تشتغل في وظيفة مرموقة؟",
"لو خيروك |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟",
"لو خيروك |  بين إلغاء رحلتك تمامًا أو بقائها ولكن فقدان الأمتعة والأشياء الخاص بك خلالها؟",
"لو خيروك |  بين نجار أو حداد؟",
"لو خيروك |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟",
"لو خيروك |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟",
"لو خيروك |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟",
"لو خيروك |  بين العمل لأيام أقل في الأسبوع مع زيادة ساعات العمل أو العمل لساعات أقل في اليوم مع أيام أكثر؟",
"لو خيروك بين أن تعيش 5 دقائق في الماضي أو أن تعيشها في المستقبل.",
"لو خيروك |  بين مشاهدة فيلم بمفردك أو الذهاب إلى مطعم وتناول العشاء بمفردك؟",
"لو خيروك |  بين أن تكون اللاعب الأفضل في فريق كرة فاشل أو أن تكون لاعب عادي في فريق كرة ناجح؟",
"لو خيروك |  بين امتلاك أفضل وأجمل منزل ولكن في حي سيء أو امتلاك أسوأ منزل ولكن في حي جيد وجميل؟",
"تكون لاعب كرة قدم او ممثل؟",
"لو خيروك |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟",
"لو خيروك بين القدرة على سماع أفكار الناس أو القدرة على العودة في الزمن للخلف.",
"لو خيروك |  بين مشاهدة فيلم بمفردك أو الذهاب إلى مطعم وتناول العشاء بمفردك؟",
"لو خيروك |  بين صديق قام بغدرك وعدوك؟",
"لو خيروك |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟",
"لو خيروك |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟",
"لو خيروك |  بين امتلاك أفضل وأجمل منزل ولكن في حي سيء أو امتلاك أسوأ منزل ولكن في حي جيد وجميل؟",
"لو خيروك |  بين لاعب كرة قدم مشهور أو موسيقي مفضل بالنسبة لك؟",
"لو خيروك |  بين أخيك البعيد أو جارك القريب؟",
"تتجوز حد وحش بس ذكي او حد جميل بس غبي؟",
"لو خيروك بين النوم في غابة مظلمة أو على ظهر سفينة في يوم عاصف.",
"لو خيروك |  بين أن تكون شخص مشغول دائمًا أو أن تكون شخص يشعر بالملل دائمًا؟",
"يكون معاك 10 مليون دولار او 10 مليون لحظة صادقة وحقيقية من السعادة؟",
"لو خيروك |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟",
"لو خيروك |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟",
"تذبح نفسك او تاكل عشره كأس صاص  حااااااار؟",
"لو خيروك بين أن تعيش 5 دقائق في الماضي أو أن تعيشها في المستقبل.",
"لو خيروك |  بين صديق قام بغدرك وعدوك؟",
"لو خيروك |  بين الخروج بالمكياج بشكل مستمر وبين الحصول على بشرة صحية ولكن لا يمكن لك تطبيق أي نوع من المكياج؟",
"لو خيروك |  بين مصور فوتوغرافي جيد وبين مصور سيء ولكنه عبقري فوتوشوب؟",
"لو خيروك |  بين موت شخصية بطل الدراما التي تتابعينها أو أن يبقى ولكن يكون العمل الدرامي سيء جدًا؟",
"لو خيروك |  بين أن تعيش بدون موسيقى أبدًا أو أن تعيش بدون تلفاز أبدًا؟",
"لو خيروك |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟",
"القدرة على حل اي مشكلة مالية تواجهك او القدرة على حل اي مشكلة عاطفية تواجهك",
"لو خيروك بين امتلاك قطة أو كلب.",
"لو خيروك |  بين تناول البيتزا وبين الايس كريم وذلك بشكل دائم؟",
"لو خيروك |  بين زوجتك وابنك/ابنتك؟",
"لو خيروك بين أن تعيش في القرن الرابع عشر أو القرن الحالي.",
"يكون عندك شركة كبيرة فيها ناس مبتحبهاش او شركة صغيرة فيها ناس بتحبها",
"لو خيروك |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟",
"لو خيروك |  بين التحدث عن كل شيء يدور في عقلك وبين عدم التحدث إطلاقًا؟",
"لو خيروك |  بين مصور فوتوغرافي جيد وبين مصور سيء ولكنه عبقري فوتوشوب؟",
"تكون شرطي فاسد او مجرم",
"لو خيروك بين المال أو الصحة.",
"لو خيروك |  بين أختك وأخيك؟",
"لو خيروك |  بين أن يكون طولك 150 سنتي متر أو أن يكون 190 سنتي متر؟",
"لو خيروك |  بين العمل لأيام أقل في الأسبوع مع زيادة ساعات العمل أو العمل لساعات أقل في اليوم مع أيام أكثر؟",
"لو خيروك |  بين شرب كوب من الحليب أو شرب كوب من شراب عرق السوس؟",
"تغسل ايدك مرة في الشهر او تغسل ايدك كل خمس دقايق",
"لو خيروك بين إنقاذ نفسك أو إنقاذ شخص وقد يعرضك ذلك للأذى.",
"لو خيروك |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟",
"لو خيروك |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟",
"تلاقي اي حاجة تضيع منك او تفتكر كل حاجة تنساها",
"لو خيروك بين أن تعيش 5 دقائق في الماضي أو أن تعيشها في المستقبل.",
"لو خيروك |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟",
"لو خيروك بين المال أو الجمال.",
"تمشي في الغابة او تمشي في شارع زحمة",
"لو خيروك |  بين امتلاك أفضل وأجمل منزل ولكن في حي سيء أو امتلاك أسوأ منزل ولكن في حي جيد وجميل؟",
"لو خيروك |  بين أن تعيش بدون موسيقى أبدًا أو أن تعيش بدون تلفاز أبدًا؟",
"تخسر كرامتك وتكسب الحب او تكسب الحب وتخسر كرامتك",
"لــو خــيروك بــين الــقــدرة عــلــى ســمــاع أفــكار الــنــاس أو الــقــدرة عــلــى الــعــودة فــي الــزمــن لــلــخــلــفــ.",
"لو خيروك |  بين أن تكون الشخص الأكثر شعبية في العمل أو المدرسة وبين أن تكون الشخص الأكثر ذكاءً؟",
"لو خيروك بين فقدان ذاكرتك والعيش مع أصدقائك وأقربائك أو بقاء ذاكرتك ولكن العيش وحيد.",
"تمثل انك مجنون ليوم كامل او توقف حد ف الشارع وتطلب منه جنيه",
"لو خيروك |  بين وضع أحمر الشفاه على وجهك ما عدا شفتين أو وضع ماسكارا على شفتين فقط؟",
"لو خيروك |  أن تعيش قصة فيلم هل تختار الأكشن أو الكوميديا؟",
"لو خيروك بين أن تعيش في القرن الرابع عشر أو القرن الحالي.",
"تكمل مع حد بتحبه بس مبيخلفش او تكون مع حد مش بتحبه بس بيخلف",
"لو خيروك |  بين أن تعرف متى سوف تموت أو أن تعرف كيف سوف تموت؟",
"لو خيروك |  بين امتلاك قطة أو كلب؟",
"لو خيروك |  بين معاركة دب أو بين مصارعة تمساح؟",
"لو خيروك |  بين أن تكون اللاعب الأفضل في فريق كرة فاشل أو أن تكون لاعب عادي في فريق كرة ناجح؟",
"لو خيروك |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟",
"لو خيروك |  بين العمل الذي تحلم به أو بين إيجاد شريك حياتك وحبك الحقيقي؟",
"لو خيروك |  بين أن تتعطل سيارتك في نصف الطريق أو ألا تتمكنين من ركنها بطريقة صحيحة؟",
"لو خيروك |  بين العمل الذي تحلم به أو بين إيجاد شريك حياتك وحبك الحقيقي؟" 
             ]
      
@Client.on_message(filters.command(["خيروك","خيرني","❤️‍🔥خيرني","لو خيروك","خيرنى","خيروك","• لو خيروك •"], ""), group=67656461)
async def krok(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(lkk)
    await message.reply(f"[{a}]")
    
msl = [
"ضربني وبكى سبقني واشتكى",
"البحر يحب الزيادة",
"↢ أكمل المثل ↢ { اضحك للدنيا ...؟ }",
"ضربني وبكى سبقني واشتكى",
"البحر يحب الزيادة",
"عشمني بالحلق خرمت انا وداني",
"ملقوش العيش ياكلوه جابو لهم عبد يلطشوه",
"ضرب الحبيب زي اكل الزبيب",
"اللي يحبه ربه يحبب فيه خلقه",
"عاكس القطة تخربشك",
"⌔︙اسرع واحد يكمل المثل ~ {مع من قلةشدو على الچلاب سروج يا}",
"من عاشر القوم اربعين يوما ياصار منهم ياصارو منه",
"كثرة المتاعب تفرق الاحباب",
"ضرب الحبيب زي اكل الزبيب",
"اجري جري الوحوش غير رزقك لن تحوش",
"↢ أكمل المثل ↢ { الخبر اللي النهاردة بفلوس ...؟ }",
"كثرة المتاعب تفرق الاحباب",
"تروح فين الشمس من على قفا الفلاح",
"سكتنا له دخل بحماره",
"يعمل من الحبة قبة",
"لاقيني ولا تغديني",
"عصفور في اليد ولا عشرة على الشجرة",
"ان دبلت الوردة ريحتها فيها",
"ضربني وبكى سبقني واشتكى",
"↢ أكمل المثل ↢ { اذا فات الفوت ماينفع ...؟ }",
"جحر ديب يساع مية حبيب",
"⌔︙اسرع واحد يكمل المثل ~ {بالحصاد}",
"عاكس القطة تخربشك",
"خالف تُعرف",
"↢ أكمل المثل ↢ { اذا فات الفوت ماينفع ...؟ }",
"أعمى ويقول شفت بعيني",
"امشي عدل يحتار عدوك فيك",
"↢ أكمل المثل ↢ { مصائب قوم عند قوم ...؟ }*",
"جحر ديب يساع مية حبيب",
"علمناهم الشحاتة سبقونا ع الابواب",
"اللي يكرهه ربنا يسلط عليه لسانه",
"خالف تُعرف",
"↢ أكمل المثل ↢ { تحت السواهي ...؟ }",
"↢ أكمل المثل ↢ { الوقت كالسيف ان لم تقطعه ...؟ }",
"البقرة لما تقع تكتر سكاكينها",
"↢ أكمل المثل ↢ { الخبر اللي النهاردة بفلوس ...؟ }*",
"↢ أكمل المثل ↢ { الخبر اللي النهاردة بفلوس ...؟ }*",
"⌔︙اسرع واحد يكمل المثل ~ {امشيولا تعبر نهر}",
"↢ أكمل المثل ↢ { رب أخ لي لم تلده أمي ينفي الأذى عني ويجلو ..؟ }",
"البيت بيت ابونا ويجو الغرب يطردونا",
"↢ أكمل المثل ↢ { تحت السواهي ...؟ }",
"↢ أكمل المثل ↢ { من عاشر حكيمًا مات ...؟ }",
"اصرف مافي الجيب يأتيك مافي الغيب",
"كل تأخيرة وفيها خيرة",
"↢ أكمل المثل ↢ { إن المعارف في أهل النهى ...؟ }",
"اللي يحبه ربه يحبب فيه خلقه",
"↢ أكمل المثل ↢ { مصائب قوم عند قوم ...؟ }*",
"من جاور الحداد انكوى بناره",
"كثرة المتاعب تفرق الاحباب",
"حرص ولا تخون*",
"الخسارة تعلم الشطارة",
"↢ أكمل المثل ↢ { إن المعارف في أهل النهى ...؟ }",
"جت الحزينة تفرح مالقتلهاش مطرح",
"↢ أكمل المثل ↢ { كرامة العبد من كرامة ...؟ }",
"↢ أكمل المثل ↢ { كرامة العبد من كرامة ...؟ }",
"ضرب الحبيب زي اكل الزبيب",
"اللي يربط في رقبته حبل الف من يسحبه",
"↢ أكمل المثل ↢ { إن المعارف في أهل النهى ...؟ }",
"كثرة المتاعب تفرق الاحباب",
"⌔︙اسرع واحد يكمل المثل ~ {ينطيللماعده سنون}",
"العبد في التفكير والرب في التدبير",
"امشي عدل يحتار عدوك فيك",
"↢ أكمل المثل ↢ { من دق الباب سمع ...؟ }",
"اللي ميشوفش من الغربال يبقا اعمى",
"الرجل تدب مطرح ماتحب",
"اتصالحت المقشة مع البلاعة والاتنين بقو جماعة",
"البقرة لما تقع تكتر سكاكينها",
"ضربني وبكى سبقني واشتكى",
"↢ أكمل المثل ↢ { الخبر اللي النهاردة بفلوس ...؟ }*",
"↢ أكمل المثل ↢ { إذا ضربت فأوجع فإن الملامة ...؟ }",
"قل له في وشه ولا تغشه",
"اصرف مافي الجيب يأتيك مافي الغيب",
"العبد في التفكير والرب في التدبير",
"يعمل من الحبة قبة",
"اللي بيته من قزاز ميحدفش الناس بالطوب",
"اللي يحبه ربه يحبب فيه خلقه",
"متخافش من الهبلة خاف من خلفتها",
"عاكس القطة تخربشك",
"متخافش من الهبلة خاف من خلفتها",
"جحر ديب يساع مية حبيب",
"⌔︙اسرع واحد يكمل المثل ~ {يامن تعب يامنيا من على الحاضر لكة}",
"طول البال يعد الجبال",
"اصرف مافي الجيب يأتيك مافي الغيب",
"⌔︙اسرع واحد يكمل المثل ~ {يامن تعب يامنيا من على الحاضر لكة}",
"مش كل مرة تسلم الجرة",
"اتصالحت المقشة مع البلاعة والاتنين بقو جماعة",
"ادي العيش لخبازه ولو اكل نصه",
"↢ أكمل المثل ↢ { الوقت كالسيف ان لم تقطعه ...؟ }",
"↢ أكمل المثل ↢ { كرامة العبد من كرامة ...؟ }",
"طول البال يعد الجبال",
"كل واحد ينام على الجنب اللي يريحه",
"ملقوش العيش ياكلوه جابو لهم عبد يلطشوه",
"↢ أكمل المثل ↢ { كرامة العبد من كرامة ...؟ }",
"عشمني بالحلق خرمت انا وداني",
"اجري جري الوحوش غير رزقك لن تحوش",
"ايد لوحدها متسقفش",
"الدنيا مرايه وريها توريك",
"⌔︙اسرع واحد يكمل المثل ~ {يامن تعب يامنيا من على الحاضر لكة}",
"ياما جاب الغراب لامه",
"اتقل عالرز يستوي",
"البقرة لما تقع تكتر سكاكينها",
"↢ أكمل المثل ↢ { اذا ماطاعك الزمن ...؟ }",
"↢ أكمل المثل ↢ { اذا كبر إبنك ...؟ }",
"لاقيني ولا تغديني",
"↢ أكمل المثل ↢ { العين بصيره واليد ...؟ }",
"↢ أكمل المثل ↢ { اذا ماطاعك الزمن ...؟ }",
"ضرب الحبيب زي اكل الزبيب",
"↢ أكمل المثل ↢ { اذا فات الفوت ماينفع ...؟ }",
"ضربني وبكى سبقني واشتكى",
"⌔︙اسرع واحد يكمل المثل ~ {قرد}",
"اتصالحت المقشة مع البلاعة والاتنين بقو جماعة",
"ان كنتم نسيتو اللي جرى هاتو الدفاتر تنقرا",
"↢ أكمل المثل ↢ { اضحك للدنيا ...؟ }",
"من عاشر القوم اربعين يوما ياصار منهم ياصارو منه",
"خنفسة شافت ولادها عالحيط قالت دا لولي وملضوم في خيط",
"طول البال يعد الجبال",
"البقرة لما تقع تكتر سكاكينها",
"⌔︙اسرع واحد يكمل المثل ~ {ينطيللماعده سنون}",
"البقرة لما تقع تكتر سكاكينها",
"↢ أكمل المثل ↢ { الخبر اللي النهاردة بفلوس ...؟ }", 
"↢ أكمل المثل ↢ { الوقت كالسيف ان لم تقطعه ...؟ }",
"العبد في التفكير والرب في التدبير",
"اللي بيته من قزاز ميحدفش الناس بالطوب",
"ان كنتم نسيتو اللي جرى هاتو الدفاتر تنقرا",
"يقتل القتيل ويمشي في جنازته",
"من عاشر القوم اربعين يوما ياصار منهم ياصارو منه",
"مش كل مرة تسلم الجرة",
"خنفسة شافت ولادها عالحيط قالت دا لولي وملضوم في خيط",
"من غربل الناس نخلوه",
"يقتل القتيل ويمشي في جنازته",
"من جاور الحداد انكوى بناره",
"البقرة لما تقع تكتر سكاكينها",
"↢ أكمل المثل ↢ { إذا ضربت فأوجع فإن الملامة ...؟ }",
"جحر ديب يساع مية حبيب",
"امشي عدل يحتار عدوك فيك",
"كل اللي يعجبك والبس اللي يعجب الناس",
"اللي يكرهه ربنا يسلط عليه لسانه",
"البحر يحب الزيادة",
"عاكس القطة تخربشك",
"لاقيني ولا تغديني",
"اللي ميشوفش من الغربال يبقا اعمى",
"كل واحد ينام على الجنب اللي يريحه",
"ايش ياخد الريح من البلاط",
"ادي العيش لخبازه ولو اكل نصه",
"ملقوش العيش ياكلوه جابو لهم عبد يلطشوه",
"↢ أكمل المثل ↢ { مصائب قوم عند قوم ...؟ }*",
"اللي يحبه ربه يحبب فيه خلقه",
"↢ أكمل المثل ↢ { القرد بعين امه ...؟ }",
"↢ أكمل المثل ↢ { دق الحديد وهو ...؟ }",
"قد النملة ويعمل عملة*",
"تروح فين الشمس من على قفا الفلاح",
"اسد عليا وفي الحروب نعامة",
"⌔︙اسرع واحد يكمل المثل ~ {قرد}",
"كل تأخيرة وفيها خيرة",
"↢ أكمل المثل ↢ { كرامة العبد من كرامة ...؟ }",
"جحر ديب يساع مية حبيب",
"↢ أكمل المثل ↢ { كرامة العبد من كرامة ...؟ }",
"↢ أكمل المثل ↢ { تحت السواهي ...؟ }",
"↢ أكمل المثل ↢ { اذا فات الفوت ماينفع ...؟ }",
"البقرة لما تقع تكتر سكاكينها",
"اللي يحبه ربه يحبب فيه خلقه",
"↢ أكمل المثل ↢ { رب أخ لي لم تلده أمي ينفي الأذى عني ويجلو ..؟ }"
            ]
      
@Client.on_message(filters.command(["مثل","امثله","امثلة","• امثله •"], ""), group=67547861)
async def amsla(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(msl)
    await message.reply(f"[{a}]")
    
txt = [
"عامل الناس بأخلاقك ولا بأخلاقهم", 
"الجمال يلفت الأنظار لكن الطيبه تلفت القلوب ", 
"الاعتذار عن الأخطاء لا يجرح كرامتك بل يجعلك كبير في نظر الناس ",
"لا ترجي السماحه من بخيل.. فما في البار لظمان ماء",
"لا تحقرون صغيره إن الجبال من الحصي",
"لا تستحي من إعطاء فإن الحرمان أقل منه ", 
"لا تظلم حتى لا تتظلم ",
"لا تقف قصاد الريح ولا تمشي معها ",
"لا تكسب موده التحكم الا بالتعقل",
"لا تمد عينك في يد غيرك ",
"لا تملح الا لمن يستحقاها ويحافظ عليها",
"لا حياه للإنسان بلا نبات",
"لا حياه في الرزق.. ولا شفاعه في الموت",
"كما تدين تدان",
"لا دين لمن لا عهد له ",
"لا سلطان على الدوق فيما يحب أو بكره",
"لا مروه لمن لادين له ",
"لا يدخل الجنه من لايأمن من جازه بوائقه",
"يسروا ولا تعسروا... ويشورا ولا تنفروا",
"يدهم الصدر ما يبني العقل الواسع ",
"أثقل ما يوضع في الميزان يوم القيامة حسن الخلق ",
"أجهل الناس من ترك يقين ما عنده لظن ما عند الناس ",
"أحياناً.. ويصبح الوهم حقيقه ",
"مينفعش تعاتب حد مبيعملش حساب لزعلك عشان متزعلش مرتين . ",
"السفر ومشاهده اماكن مختلفه وجديده ",
"عدم تضيع الفرص واسثمارها لحظه مجبئها ",
" اعطاء الاخرين اكثر من ما يتوقعون",
"معامله الناس بلطف ولكن عدم السماح لاحد بستغالال ذالك ",
"تكوين صدقات جديده مع الحفظ بلاصدقاء القودامي ",
"تعلم اصول المهنه بدلا من تضيع الوقت ف تعلم حيل المهنه ",
"مدح ع الاقل ثلاث اشخاص يوميا ",
"النظر ف عيون الشخاص عند مخاطبتهم ",
"التحلي بلسماح مع الاخرين او النفس ",
"الاكثار من قول كلمه شكرا ",
" مصافحه الاخرين بثبات وقوة ",
"الابتعاد عن المناطق السيئه السمعه لتجنب الاحداث السئه ",
" ادخار 10٪ع الاقل من الدخل",
" تجنب المخاوف من خلال التعلم من تجارب مختلفه",
" الحفاظ ع السمعه لانها اغلي ما يملك الانسان",
" تحويل الاعداء الي اصدقاء من خلال القيام بعمل جيد",
"لا تصدق كل ما تسمعع. ولا تنفق كل ما تمتلك . ولا تنم قدر ما ترغب ",
" اعتني بسمعتك جيدا فستثبت للك الايام انها اغلي ما تملك",
"حين تقول والدتك ستندم ع فعل ذالك ستندم عليه غالبا.. ",
" لا تخش العقبات الكبيره فخلفها تقع الفرص العظيمه",
"قد لا يتطلب الامر اكثر من شخص واحد لقلب حياتك رأس ع عقب ",
"اختر رفيقه حياتك بحرص فهو قرار سيشكل 90٪من سعادتك او بؤسك ",
" اقلب اداءك الاصدقاء بفعل شي جميل ومفجائ لهم",
"حين تدق الفرصه ع باباك ادعوها للبيت ",
"تعلم القواعد جيدا ثن اكسر بعدها ",
"احكم ع نجاحك من خلال قدرتك ع العطاء وليس الاخذ ",
" لا تتجاهل الشيطان مهما بدل ثيابه",
"ركز ع جعل الاشياء افضل وليس اكبر او اعظم ",
"كن سعيد  بما تمتلك واعمل لامتلاك ما تريد ",
"اعط الناس اكثر من ما يتوقعون ",
" لا تكن منشغل لدرجه عدم التعرف ع اصدقاء جدد",
"استحمه يوم العيد يمعفن🐰",
"مش تحب اي حد يقرب منك ",
" خليك مع البت راجل خليك تقيل",
" انصح نفسك بنفسك بمت😂",
" كنت نصحت نفسي ياخويا🗿", 
        ]
      
@Client.on_message(filters.command(["انصحني","❤️‍🔥انصحني","نصيحه","انصحنى","• انصحني •"], ""), group=6736961)
async def anshny(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(txt)
    await message.reply(f"[{a}]")
        
tt = [
" اسم ولد بحرف ⇦ أ  ",
"  اسم بنت بحرف ⇦ أ  ",
"  جماد بحرف ⇦ أ  ",
" نبات بحرف ⇦ أ  ",
" حيوان بحرف ⇦ أ  ",
"مدينة او بلد بحرف ⇦ أ  ",
" اسم ولد بحرف ⇦ ب  ",
"  اسم بنت بحرف ⇦ ب  ",
"  جماد بحرف ⇦ ب  ",
" نبات بحرف ⇦ ب ",
" حيوان بحرف ⇦ ب ",
"مدينة بحرف ⇦ ب ",
" اسم ولد بحرف ⇦ ت  ",
"  اسم بنت بحرف ⇦ ت  ",
"  جماد بحرف ⇦ ت  ",
" نبات بحرف ⇦ ت ",
" حيوان بحرف ⇦ ت",
"مدينة بحرف ⇦ ت ",
" اسم ولد بحرف ⇦ ث  ",
"  اسم بنت بحرف ⇦ ث ",
"  جماد بحرف ⇦ ث ",
" نبات بحرف ⇦ ث  ",
" حيوان بحرف ⇦ ث ",
"مدينة او بلد بحرف ⇦ ث ",
" اسم ولد بحرف ⇦ ج  ",
"  اسم بنت بحرف ⇦ ج  ",
"  جماد بحرف ⇦ ج  ",
" نبات بحرف ⇦ ج  ",
" حيوان بحرف ⇦ ج ",
"مدينة او بلد بحرف ⇦ ج  ",
" اسم ولد بحرف ⇦ ح ",
"  اسم بنت بحرف ⇦ ح  ",
"  جماد بحرف ⇦ ح  ",
" نبات بحرف ⇦ ح  ",
" حيوان بحرف ⇦ ح ",
"مدينة او بلد بحرف ⇦ ح ",
" اسم ولد بحرف ⇦ خ ",
"  اسم بنت بحرف ⇦ خ  ",
"  جماد بحرف ⇦ خ  ",
" نبات بحرف ⇦ خ ",
" حيوان بحرف ⇦ خ ",
"مدينة او بلد بحرف ⇦ خ  ",
" اسم ولد بحرف ⇦ د  ",
"  اسم بنت بحرف ⇦ د ",
"  جماد بحرف ⇦ د  ",
" نبات بحرف ⇦ د ",
" حيوان بحرف ⇦ د  ",
"مدينة او بلد بحرف ⇦ د  ",
" اسم ولد بحرف ⇦ ذ  ",
"  اسم بنت بحرف ⇦ ذ  ",
"  جماد بحرف ⇦ ذ ",
" نبات بحرف ⇦ ذ ",
" حيوان بحرف ⇦ ذ ",
"مدينة او بلد بحرف ⇦ ذ  ", 
" اسم ولد بحرف ⇦ ر  ",
"  اسم بنت بحرف ⇦ ر ",
"  جماد بحرف ⇦ ر  ",
" نبات بحرف ⇦ ر ",
" حيوان بحرف ⇦ ر  ",
"مدينة او بلد بحرف ⇦ ر ",
" اسم ولد بحرف ⇦ ز ",
"  اسم بنت بحرف ⇦ ز ",
"  جماد بحرف ⇦ ز  ",
" نبات بحرف ⇦ ز  ",
" حيوان بحرف ⇦ ز  ",
"مدينة او بلد بحرف ⇦ ز  ",
" اسم ولد بحرف ⇦ س ",
"  اسم بنت بحرف ⇦ س  ",
"  جماد بحرف ⇦ س  ",
" نبات بحرف ⇦ س  ",
" حيوان بحرف ⇦ س  ",
"مدينة او بلد بحرف ⇦ س  ",
" اسم ولد بحرف ⇦ ش  ",
"  اسم بنت بحرف ⇦ ش  ",
"  جماد بحرف ⇦ ش  ",
" نبات بحرف ⇦ ش  ",
" حيوان بحرف ⇦ ش  ",
"مدينة او بلد بحرف ⇦ ش  ",
" اسم ولد بحرف ⇦ ص  ",
"  اسم بنت بحرف ⇦ ص  ",
"  جماد بحرف ⇦ ص  ",
" نبات بحرف ⇦ ص  ",
" حيوان بحرف ⇦ ص  ",
"مدينة او بلد بحرف ⇦ ص  ",
" اسم ولد بحرف ⇦ ض  ",
"  اسم بنت بحرف ⇦ ض  ",
"  جماد بحرف ⇦ ض  ",
" نبات بحرف ⇦ ض  ",
" حيوان بحرف ⇦ ض  ",
"مدينة او بلد بحرف ⇦ ض  ", 
" اسم ولد بحرف ⇦ ط  ",
"  اسم بنت بحرف ⇦ ط  ",
"  جماد بحرف ⇦ ط  ",
" نبات بحرف ⇦ ط  ",
" حيوان بحرف ⇦ ط  ",
"مدينة او بلد بحرف ⇦ ط  ",
" اسم ولد بحرف ⇦ ظ  ",
"  اسم بنت بحرف ⇦ ظ  ",
"  جماد بحرف ⇦ ظ  ",
" نبات بحرف ⇦ ظ  ",
" حيوان بحرف ⇦ ظ  ",
"مدينة او بلد بحرف ⇦ ظ  ",
" اسم ولد بحرف ⇦ ع ",
"  اسم بنت بحرف ⇦ ع  ",
"  جماد بحرف ⇦ ع  ",
" نبات بحرف ⇦ ع  ",
" حيوان بحرف ⇦ ع  ",
"مدينة او بلد بحرف ⇦ ع  ",
" اسم ولد بحرف ⇦ غ. ",
"  اسم بنت بحرف ⇦ غ  ",
"  جماد بحرف ⇦ غ  ",
" نبات بحرف ⇦ غ  ",
" حيوان بحرف ⇦ غ  ",
"مدينة او بلد بحرف ⇦ غ  ",
" اسم ولد بحرف ⇦ ف  ",
"  اسم بنت بحرف ⇦ ف  ",
"  جماد بحرف ⇦ ف  ",
" نبات بحرف ⇦ ف  ",
" حيوان بحرف ⇦ ف  ",
"مدينة او بلد بحرف ⇦ ف  ",
" اسم ولد بحرف ⇦ ق  ",
"  اسم بنت بحرف ⇦ ق  ",
"  جماد بحرف ⇦ ق  ",
" نبات بحرف ⇦ ق  ",
" حيوان بحرف ⇦ ق  ",
"مدينة او بلد بحرف ⇦ ق  ",
" اسم ولد بحرف ⇦ ك  ",
"  اسم بنت بحرف ⇦ ك  ",
"  جماد بحرف ⇦ ك ",
" نبات بحرف ⇦ ك ",
" حيوان بحرف ⇦ ك  ",
"مدينة او بلد بحرف ⇦ ك  ",
" اسم ولد بحرف ⇦ ل  ",
"  اسم بنت بحرف ⇦ ل  ",
"  جماد بحرف ⇦ ل  ",
" نبات بحرف ⇦ ل  ",
" حيوان بحرف ⇦ ل  ",
"مدينة او بلد بحرف ⇦ ل  ", 
" اسم ولد بحرف ⇦ م  ",
"  اسم بنت بحرف ⇦ م  ",
"  جماد بحرف ⇦ م  ",
" نبات بحرف ⇦ م  ",
" حيوان بحرف ⇦ م  ",
"مدينة او بلد بحرف ⇦ م  ",
" اسم ولد بحرف ⇦ ن  ",
"  اسم بنت بحرف ⇦ ن ",
"  جماد بحرف ⇦ ن  ",
" نبات بحرف ⇦ ن  ",
" حيوان بحرف ⇦ ن  ",
"مدينة او بلد بحرف ⇦ ن  ",
" اسم ولد بحرف ⇦ ه  ",
"  اسم بنت بحرف ⇦ ه ",
"  جماد بحرف ⇦ ه  ",
" نبات بحرف ⇦ ه  ",
" حيوان بحرف ⇦ ه  ",
"مدينة او بلد بحرف ⇦ ه  ",
" اسم ولد بحرف ⇦ و  ",
"  اسم بنت بحرف ⇦ و  ",
"  جماد بحرف ⇦ و  ",
" نبات بحرف ⇦ و  ",
" حيوان بحرف ⇦ و  ",
"مدينة او بلد بحرف ⇦ و  ",
" اسم ولد بحرف ⇦ ي ",
"  اسم بنت بحرف ⇦ ي  ",
"  جماد بحرف ⇦ ي  ",
" نبات بحرف ⇦ ي  ",
" حيوان بحرف ⇦ ي  ",
"مدينة او بلد بحرف ⇦ ي  "
        ]
@Client.on_message(filters.command(["حروف","❤️‍🔥حروف","حرف","اتوبيس كومبليت","• حروف •"], ""), group=158007) 
async def ahrof(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(tt)
    await message.reply(f"[{a}]")

xt = ["لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
"اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
"استغفر الله العظيم وأتوبُ إليه 🌹",
"حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
"ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
"ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
"أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
"سبحان الله وبحمده سبحان الله العظيم🌸",
"أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
"اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
"استغفر الله العظيم وأتوبُ إليه 🌹",
"لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
"قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
"يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
"﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
"‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
"‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
"ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
"‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
"رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
"اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
"استغفر الله العظيم وأتوبُ إليه.",
"‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
" أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
"ماتستغفر ربنا كده🥺❤️",
"فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
"ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
"يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
"قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
"اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
"- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
"- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
"أصبحنا وأصبح الملك لله ولا اله الا الله.",
"‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
"‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
"يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
"- اللهم القبول الذي لا يزول ❤️🍀.",
"- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
"سبحان الله وبحمده ،سبحان الله العظيم.",
"لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
" عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
"- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
"بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
"- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
"- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
"‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
"يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
"‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
"صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
"اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت ??💜.",
"- وبك أصبحنا يا عظيم الشأن ??❤️.",
"اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
"‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
"- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
"صلي على النبي بنيه الفرج❤️",
"استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
"اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
"لا اله الا الله سيدنا محمد رسول الله🌿💜",
"قول معايا - استغفر الله استفر الله استغفر الله -",
"مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
"أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
"صلي على محمد❤️",
"ماتيجو نقرء الفاتحه سوا🥺"]

@Client.on_message(filters.command(["ازكار","الازكار","❤️‍🔥ازكار","دينى","اسلامى","• ازكار •"], ""), group=694771) 
async def azkar(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(xt)
    await message.reply(f"[{a}]")
        
txkt = [

"‏من علامات جمال المرأة .. بختها المايل ! ",
"‏ انك الجميع و كل من احتل قلبي🫀🤍",
"‏ ‏ لقد تْعَمقتُ بكَ كَثيراً والمِيمُ لام .♥️",
"‏ ‏ممكن اكون اختارت غلط بس والله حبيت بجد🖇️",
"‏ علينا إحياء زَمن الرّسائل الورقيّة وسط هذه الفوضى الالكترونية العَارمة. ℘︙ 💜",
"‏ يجي اي الصاروخ الصيني ده جمب الصاروخ المصري لما بيلبس العبايه السوده.🤩♥️",
"‏ كُنت أرقّ من أن أتحمّل كُل تلك القَسوة من عَينيك .🍍",
"‏أَكَان عَلَيَّ أَنْ أغْرَس انيابي فِي قَلْبِك لتشعر بِي ؟.",
"‏ : كُلما أتبع قلبي يدلني إليك .",
"‏ : أيا ليت من تَهواه العينُ تلقاهُ .",
"‏ ‏: رغبتي في مُعانقتك عميقة جداً .??",
"ويُرهقني أنّي مليء بما لا أستطيع قوله.✨",
"‏ من مراتب التعاسه إطالة الندم ع شيء إنتهى. ℘︙ ",
"‏ ‏كل العالم يهون بس الدنيا بينا تصفي 💙",
"‏ بعض الاِعتذارات يجب أن تُرفَضّ.",
"‏ ‏تبدأ حياتك محاولاً فهم كل شيء، وتنهيها محاولاً النجاة من كل ما فهمت.",
"‏ إن الأمر ينتهي بِنا إلى أعتياد أي شيء.",
"‏ هل كانت كل الطرق تؤدي إليكِ، أم أنني كنتُ أجعلها كذلك.",
"‏ ‏هَتفضل تواسيهُم واحد ورا التاني لكن أنتَ هتتنسي ومحدِش هَيواسيك.",
"‏ جَبَرَ الله قلوبِكُم ، وقَلبِي .🍫",
"‏ بس لما أنا ببقى فايق، ببقى أبكم له ودان.💖",
"‏ ‏مقدرش عالنسيان ولو طال الزمن 🖤",
"‏ أنا لستُ لأحد ولا احد لي ، أنا إنسان غريب أساعد من يحتاجني واختفي.",
"‏ ‏أحببتك وأنا منطفئ، فما بالك وأنا في كامل توهجي ؟",
"‏ لا تعودني على دفء شمسك، إذا كان في نيتك الغروب .َ",
"‏ وانتهت صداقة الخمس سنوات بموقف.",
"‏ ‏لا تحب أحداً لِدرجة أن تتقبّل أذاه.",
"‏ إنعدام الرّغبة أمام الشّيء الّذي أدمنته ، انتصار.",
"‏مش جايز , ده اكيد التأخير وارهاق القلب ده وراه عوضاً عظيماً !?? ",
" مش جايز , ده اكيد التأخير وارهاق القلب ده وراه عوضاً عظيماً !💙",
"فـ بالله صبر  وبالله يسر وبالله عون وبالله كل شيئ ♥️. ",
"أنا بعتز بنفسي جداً كصاحب وشايف اللي بيخسرني ، بيخسر أنضف وأجدع شخص ممكن يشوفه . ",
"فجأه جاتلى قافله ‏خلتنى مستعد أخسر أي حد من غير ما أندم عليه . ",
"‏اللهُم قوني بك حين يقِل صبري... ",
"‏يارب سهِل لنا كُل حاجة شايلين هَمها 💙‏ ",
"انا محتاج ايام حلوه بقي عشان مش نافع كدا ! ",
"المشكله مش اني باخد قررات غلط المشكله اني بفكر كويس فيها قبل ما اخدها .. ",
"تخيل وانت قاعد مخنوق كدا بتفكر فالمزاكره اللي مزكرتهاش تلاقي قرار الغاء الدراسه .. ",
" مكانوش يستحقوا المعافرة بأمانه.",
"‏جمل فترة في حياتي، كانت مع اكثر الناس الذين أذتني نفسيًا. ",
" ‏إحنا ليه مبنتحبش يعني فينا اي وحش!",
"أيام مُمله ومستقبل مجهول ونومٌ غير منتظموالأيامُ تمرُ ولا شيَ يتغير ", 
"عندما تهب ريح المصلحه سوف ياتي الجميع رتكدون تحت قدمك ❤️. ",
"عادي مهما تعادي اختك قد الدنيا ف عادي ❤. ",
"بقيت لوحدي بمعنا اي انا اصلا من زمان لوحدي.❤️ ",
"- ‏تجري حياتنا بما لاتشتهي أحلامنا ! ",
"تحملين كل هذا الجمال، ‏ألا تتعبين؟",
"البدايات للكل ، والثبات للصادقين ",
"مُؤخرًا اقتنعت بالجملة دي جدا : Private life always wins. ",
" الافراط في التسامح بيخللي الناس تستهين بيك🍍",
"مهما كنت كويس فـَ إنت معرض لـِ الاستبدال.. ",
"فخوره بنفسي جدًا رغم اني معملتش حاجه فـ حياتي تستحق الذكر والله . ",
"‏إسمها ليلة القدر لأنها تُغير الأقدار ,اللهُمَّ غير قدري لحالٍ تُحبه وعوضني خير .. ",
"فى احتمال كبير انها ليلة القدر ادعوا لنفسكم كتير وأدعو ربنا يشفى كل مريض. 💙 ",
"أنِر ظُلمتي، وامحُ خطيئتي، واقبل توبتي وأعتِق رقبتي يا اللّٰه. إنكَ عفوٌّ تُحِبُّ العفوَ؛ فاعفُ عني 💛 "
        ]
        
@Client.on_message(filters.command(["كتبات","حكمه","❤️‍🔥حكمه","• اقتباسات •","اقتباسات","مقوله","معلومات","❤️‍🔥اقتباسات","اقتباس","تويت","تويته","• تويت •"], ""), group=7397473) 
async def ktbat(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(txkt)
    await message.reply(f"[{a}]")
        
thdhbxt = [
"هل تخربني اسم والدتك ما هو.",
"ليك اسم شهره بتحبو ؟",
"ممكن تعمل اي في حياتك",                        
"انت راضي عن حياتك",            
"اسم حببتك الاوله ايه",           
"ما هو هدفك في الحياه",
"كم مجموعك الدراسي",                      
"ما هو الاكل المفضل لك",            
"هل تحب سماع القران الكريم",           
"هل تامن بالحب",
"ماهو اخطر سر اليك",                    
"هل تامن بالارتباط السوشيال",                       
"متي ستتزوج",                        
"هل تحب الفتيات ام الصبيان",                        
"ماهو قولك عندما تره ما تحب",          
"مانوع هاتفك الجوال",            
"ماذا تفعل في الشتاء",                        
"هل تحب والديك ام خوتك",                       
"هل لك اسم شهره",                        
"سبق و فعلت شي ندمان علي فعله",           
"ما هو هدفك في الوقت الحالي",                        
"ما اسم فلمك المفضل",                        
"هل تحب الصراحه ام الكذب",                        
"• أوصف نفسك بكلمة؟",                        
"ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",           
"تاريخ ميلادك ايه?",                        
"مرتبط ولا سنجل ؟",          
"انت بخير حاليا ؟",           
"اسمك ايه",                        
"منين داهيه",                        
"عندك صحاب بنات",                        
"عندك صحاب ولاد",                       
"لونك المفضل",                       
"جربت حاجه نجحت واي هي ؟",                        
"رايك في البار",                        
"مين اكتر حد بتحبه هنا",                      
"هات رقمك",                        
"بتحب المغامره",              
"احسن حاجه حصلتلك الفتره دي",            
"بتصلي",                        
"كم فرد في الاسلام",                       
"ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",                        
"كم ركعه في صلاه العصر",                      
"ما هيا اليلله التي خير من الف شهر",                        
"سرقت قبل كدا",            
"هل تحب الموسيقى",           
"هل تحب مصر",            
"لو الحمه غلت تاكل ايه",           
"ايه رايك فيا كابوت موز",            
"بتحب مين من الفنانين",                        
"امك حلوه",                        
"عندك كم اخ",                        
"تقدر تنصح غيرك",                       
"عاوز تعمل نصيبه امتي",                        
"لابس ايه دلوقتي",                        
"لابسه ايه دلوقتي",                        
"حد باسك قبل كدا",                        
"بوست حد قبل كدا",                        
"بتحب الفلوس",                        
"بتحب الكشري",                        
"نفسك تسافر فيه",                        
"عالطلاق انت كحيااان",                        
"بتعرف ترقص",                       
"بتعرف تغني",                        
"بتحب المدرسه",                        
"ارتبط من المدرسه قبل كدا",                        
"اكتر اتنين بتحب تخرج معاهم",                        
"بتحب الفصح",                     
"بتحب المناسبات",                        
"بتحب الفول",                        
"عاوز تخرج فين",                        
"جربت تموت من الجوع قبل كدا",                        
"بتحب تربي القطط",                        
"مامتك عايشه",                        
"ايه رايك في تليجرام",                        
"ايه رايك في بت اللي فكول دي",                        
"ايه رايك في اسعار في البلد",                       
"ناوي تغير فونك امتي",                       
"تعرف تشتم حد بتحبو",                        
"بتحب الصعيد",                        
"بتحب اسكندريه",                       
"متابع ايه في مسلسلات التركي",                        
"عندك واتساب",                        
"ايه رايك في الشتاء",                       
"ايه رايك في الصيف",                       
"ايه رايك في الخريف",                       
"كم فصل في سنه",                        
"قاعد فين دلوقتي",                        
"شربت حشيش قبل كدا",                       
"بتشرب سجاير",                        
"بتشربي سجاير",                        
"عيط علي حاجه قبل كدا",           
"بتنام امتي",                        
"شغال ايه",                        
"شغاله ايه",                        
"بتحب شغالك",                        
"نفسك تبقي غني",                        
"بتعرف تخبي مشعارك",            
"لون عيونك ايه",            
"لون شعرك ايه",
"حبيت كام مره 💏",             
"اتعاكست كام مره☹️☹️",                
"خونت كام مره 😈",                
"موقف محرج حصلك😳",                
"اكتر شخص حبيته وكسرك💔",                
"شايف نفسك فين  بعد 5 سنين🤑",                
"لو بقيت بنت ليوم اول حاجه هتعملها ايه والعكس لو بقيتي ولد ليوم اول حاجه هتعمليها ايه🤐🤐",                
"اغرب موقف حصلك🤨",                
"اقرب انسان لقلبك 💑",                
"قولي اغلي 5 اشخاص في حياتك 👨‍👩‍👦‍👦",                
"اوصف نفسك في كلمتين👼",                
"لو ليك 3 امنيات هيبقوا ايه 🧚‍♂️🧚‍♀️",                
"اكتر شخص بتحبه هنا مين😍",                
"اوصف صاحب ليك في 3 كلمات😌",                
"عاكست قبل كده وكان مين😘",                
"اتخانت قبل كده ؟🤣",                
"لو اتجبرت علي جواز صالونات هتوافق 👰🤵",                
"لو هترتبط بحد في الروم هيبقي مين ??",                
"اهلك بيدلعوك بيقولولك ايه 😁😁",               
"صوتك حلو؟",                
"لقيت الناس اللي بوشين؟",                
"شيء وكنت تحقق اللسان؟",                
"أنا شخص ضعيف عندما؟",                
"هل ترغب في إظهار حبك ومرفق لشخص أو رؤية هذا الضعف؟",
"هل الكذب يكون ضروري وقتا ما؟",                
"أتشعر بالوحدة على الرغم انه يحاط بك الكثير من البشر؟",                
"كيفية الكشف عن من يكمن عليك؟",               
"إذا حاول شخص ما أن يكرهه أن يقترب منك ويهتم بك تعطيه فرصة؟",                
"أشجع حاجه حلوه ف حياتك؟",                
"طريقة جيدة يقنع حتى لو كانت الفكرة خاطئة"                 
"كيف تتصرف مع من يسيئون فهمك ويأخذ على ذهنه ثم ينتظر أن يرفض؟",                
"التغيير العادي عندما يكون الشخص الذي يحبه؟",               
"المواقف الصعبة تضعف لك ولا ترفع؟",                
"نظرة و يفسد الصداقة؟",                
"‏‏لو حد قالك كلام سئ في الغالب اي رد فعلك؟",                
"شخص معاك بالحلوه والمُره؟",                
"‏هل تحب إظهار حبك وتعلقك بالشخص أم ترى ذلك ضعف؟",                
"تاخد بكلام اللي ينصحك وماتعملش اللي انت عاوزة؟",               
"اي تتمني الناس تعرفه عليك؟",                
"ابيع المجرة عشان؟",                
"أحيانا بحس ان الناس ، كمل؟",                
"صدفة العمر الحلوة هي اني؟",             
"الكُره العظيم دايم يجي بعد حُب قوي "
"صفة تحبها في نفسك؟",               
"‏الفقر فقر العقول ليس الجيوب "                
"تصلي صلواتك الخمس كلها؟",                
"‏تجامل أحد على راحتك؟",                
"اشجع شيء عملته ف حياتك؟",                
"ناوي تعمل اي النهارده؟",                
"اي بيكون شعورك لما بتشوف المطر؟",
"غيرتك هاديه ومابتعملش مشاكل؟",
"اي اكتر حاجه ندمت عليها؟",
"اي الدول اللي تتمنى تزورها؟",
"اخره مره بكيت امتي؟",
"تقييم حظك ؟ من عشره؟",
"هل تعتقد ان حظك سيئ؟",
"شـخــص تتمنــي الإنتقــام منـــه؟",
"كلمة تود سماعها كل يوم؟",
"**هل تُتقن عملك أم تشعر بالممل؟",
"هل قمت بانتحال أحد الشخصيات لتكذب على من حولك؟",
"متى آخر مرة قمت بعمل مُشكلة كبيرة وتسببت في خسائر؟",
"ما هو اسوأ خبر سمعته بحياتك؟",                
"‏ هل جرحت شخص تحبه من قبل ؟",               
"ما هي العادة التي تُحب أن تبتعد عنها؟",
"‏هل تحب عائلتك ام تكرههم؟",
"‏من هو الشخص الذي يأتي في قلبك بعد الله – سبحانه وتعالى- ورسوله الكريم – صلى الله عليه وسلم؟",
"‏هل خجلت من نفسك من قبل؟",                
"‏ما هو ا الحلم الذي لم تستطيع ان تحققه؟",                
"‏ما هو الشخص الذي تحلم به كل ليلة؟",              
"‏هل تعرضت إلى موقف مُحرج جعلك تكره صاحبهُ؟",
"‏هل قمت بالبكاء أمام من تُحب؟",              
"‏ماذا تختار حبيبك أم صديقك؟",               
"‏ هل حياتك سعيدة أم حزينة؟",                
"ما هي أجمل سنة عشتها بحياتك؟",                
"‏ما هو عمرك الحقيقي؟",                
"ما هي أمنياتك المُستقبلية؟"
        ]
       
@Client.on_message(filters.command(["صراحه","اسال","سوال","س","• اسال •","كت","❤️‍🔥كت","• كت •","• صراحه •"], ""), group=7558523)
async def c5455utt(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(thdhbxt)
    await message.reply(f"[{a}]")
        

tjgkgjhjxt = [
"واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",
"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",
"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية ??😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة صعيدية جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل ??😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو جابوا  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹 "
        ]

@Client.on_message(filters.command(["نكته","❤️‍🔥نكته","نكت","• نكته •","ضحك"], ""), group=73837730)
async def nokt(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(tjgkgjhjxt)
    await message.reply(f"[{a}]")

txjfjvkbkvt = [
" اتحداك تقول سر محدش يعرفو", 
" تحداك تطلع تغني ف الكول،🤡", 
" اتحداك تقفل الكول🤡🌟", 
" اتحداك تقول حاجه محدش يعرفها عن صاحب البار،🤡", 
" اتحداك تقلد صوت حيوان😂♥", 
" اتحداك تتصل بمطعم وتقوله عايز بيبرونة😂♥🤡", 
" اتحداك تخرج من كل الجروبات ال عندك 😂♥️", 
" اتحداك تقول اخر مره اتضربت امتا🤡🤡", 
" اتحداك تحكي شويه عن شخصيتك 🤡🌟", 
" اتحداك تجيب اسكرين من سيرش جوجل بتاعك😂♥", 
" اتحداك تغير صورة البروفايل زي بتاعتي", 
" اتحداك تقولي امك اسمها اي 😹♥️", 
" اتحداك تقطع 10 جنيه دلوقتي😂♥", 
" اتحداك تقفل الكول🤡🌟", 
" اتحداك تقلد صوت حيوان😂♥", 
" اتحداك تبعت اخر سكرين شوت عندك 😹♥", 
" اتحداك تقولي امك اسمها اي 😹♥️", 
" اتحداك تقول لحد دا امك اسمها اي", 
" اتحداك تقول اكتر اكله بتحبها🤡😹", 
" اتحداك تقول اسم البيست فريند❤️😹", 
" اعمل منشن لوحده وقولها هاتي رقمك 😂♥️", 
" اتحداك تمنشن لواحد كلاون 🤡", 
" اتحداك تدخل الكول وتقولهم بصوت عالي انا حامل 😂♥️", 
" اتحداك تجيب سكرين شوت ل شات اكتر حد بتضحك معاه 😂♥️", 
" اتحداك تقول لحد دا امك اسمها اي", 
" اتحداك تغني في ريكورد وتبعتو", 
" اتحداك تقول اخر مره اتضربت امتا🤡🤡", 
" لو راجل قولي انت مرتبط بكام وحده دلوقتي 😂♥️", 
" اتحداك تبعتلي صوره حبيبتك 😂♥️", 
" غنيلي اغنيه ل حمو بيكا 😂♥️", 
" اتحداك تمنشن لحد وتقوله انت حكاك❤️😹", 
" اتحداك تمنشن اطيب واحد هنا🤡??", 
" اتحداك تقول مين الي انت بتكراش عليها هنا ♥️😹", 
" اتحداك تقول اسم حبيبتك", 
" اتحداك تقول اخر رساله جاتلك من مين", 
" اتحداك تبعت رقمك 😂♥️", 
" اتحداك تقول اسم حبيبتك", 
" اتحداك تقفل الكول 😂♥️", 
" اتحداك تقوم تصلي دلوقتي ♥️", 
" اتحداك تمنشن لحد وتقوله انت حكاك❤️😹", 
" اتحداك تقول لحد امك رقاصه", 
" اتحداك تجيب سكرين شوت ل شات اكتر حد بتضحك معاه 😂♥️", 
" اتحداك تمنشن لواحده وتقولها تيجي نتجوز ❤️😹", 
" اتحداك تقول اخر مره اتضربت امتا🤡🤡", 
" اتحداك تجيب اسكرين من سيرش جوجل بتاعك😂♥", 
" اتحداك تقول اسم اغلي صاحب بتحبه❤️😹", 
" اتحداك تمنشن اكتر واحد شايفه م محترم😹🤡", 
" اتحداك تحذف تلي دلوقتي 😂♥️", 
" اتحداك تقول بحبك لخمس منشن😂😉", 
" اتحداك تقفل الكول 😂♥️", 
" اتحداك تغني لحسن شاكوش❤️😹", 
" اتحداك تقول رايك عن السوشيال ميديا 🤡", 
"ا تحداك تتكلم بلهجة مختلفة لمدة دقيق😂♥", 
" اتحداك تعمل منشن لحد وتقول نكته سخيفة😂♥", 
" اتحداك تصور نفسك دلوقتي وتبعتها", 
" اتحداك تقول لاي حد بحبك", 
" اتحداك تنزل واقع وتقابلني 😂❤️", 
" اتحداك تقطع الهاند بتاعتك دلوقتي😂♥", 
" اتحداك تقول اخر رساله جاتلك من مين", 
" اتحداك تفتح كام وتقول كبسو كبسو🤡😹", 
" اتحداك تقوم تصلي دلوقتي ♥️", 
" اتحداك تقول انا م راجل 😹🤡", 
" اتحداك تقول مواصفات فتاة احلامك😹🩶", 
" اتحداك تطلع الكول ترقص عقباوي 😂♥️", 
" اتحداك تمنشن لواحده وتقولها امك حماتي❤️😹", 
" اتحداك تقول للقيصر بحبك 😹♥", 
" اتحداك ترمي نفسك من البلكونة 😂♥", 
" اتحداك تقولي عندك كام اكس ف حياتك 😹♥️", 
" اتحداك تقول ع عاده بتحب تعملها❤️😹", 
" اتحداك تقطع الهاند بتاعتك دلوقتي😂♥", 
" اتحداك تمنشن لواحده وتقولها امك حماتي❤️😹", 
" اتحداك تبعت اسكرين لشات اكتر واحد بتكلمه❤️😹", 
" اتحداك تقول اسم بنت معرفتش تشقطها ♥️😹", 
" اتحداك تقول مين اخر حد بعتلك رساله", 
" اتحداك تمنشن اكتر واحد شايفه م محترم😹🤡", 
" صلي على النبي وتبسم ♥️✨", 
" اتحداك تقول اسم كراش الطفوله ♥️😹", 
" اتحداك تمنشن لحد وتقوله ارقلصي😂♥", 
" اتحداك تمنشن لحد وتقوله ارقلصي😂♥", 
" اتحداك تغني لحسن شاكوش❤️😹", 
" اتحداك تقول اسم كراش الطفوله ♥️😹", 
" اتحداك تقول اسم كراش الطفوله ♥️😹", 
" اتحداك تعمل منشن لحد وتقول نكته سخيفة😂♥", 
" اتحداك تبعت رقم امك😂♥", 
" اتحداك تقلد صوت حيوان😂♥", 
" اتحداك تعمل منشن لواحد وتقولو تعال نرتبط 😂♥️", 
" اتحداك تقول بتعمل اي ف اوقات فراغك🤡😹", 
" اتحداك تقول موقف حصلك ومش قادر تنساه ♥️😹", 
" اتحداك تحط البايو بحبك الى مغلبنى 10 دقايق ??", 
" اتحداك تسال صحبك رأيه ف شخصيتك وتصرفاتك🤡🌟",
        ]
@Client.on_message(filters.command(["تحدي","• احكام •","حكم","تحدى","• تحدي •","احكام"], ""), group=756363543)
async def caes253ar(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in src:
      return
    a = random.choice(txjfjvkbkvt)
    await message.reply(f"[{a}]")    

points = {}  
c0aesar = {}              
u0sers = {}        

ph0otos = [
    {"name": "محمد سعد", "photo": "https://envs.sh/wl8.jpg"},
    {"name": "نرمين الفقي", "photo": "https://envs.sh/wlJ.jpg"},
    {"name": "عبله كامل", "photo": "https://envs.sh/wlr.jpg"},
    {"name": "دينا الشربيني", "photo": "https://envs.sh/wls.jpg"},
    {"name": "ليلي احمد زاهر", "photo": "https://envs.sh/wl9.jpg"},
    {"name": "روبي", "photo": "https://envs.sh/wlv.jpg"},
    {"name": "غاده عادل", "photo": "https://envs.sh/wlN.jpg"},
    {"name": "ياسمين عبد العزيز", "photo": "https://envs.sh/wlH.jpg"},
    {"name": "اسماء جلال", "photo": "https://envs.sh/wlg.jpg"},
    {"name": "امينه خليل", "photo": "https://envs.sh/wla.jpg"},
    {"name": "احمد فهمي", "photo": "https://envs.sh/PHf.jpg"},
    {"name": "رنا رئيس", "photo": "https://envs.sh/wlM.jpg"},
    {"name": "باسم سمره", "photo": "https://envs.sh/wlX.jpg"},
    {"name": "محمد سلام", "photo": "https://envs.sh/wly.jpg"},
    {"name": "ميرنا نور الدين", "photo": "https://envs.sh/wlV.jpg"},
    {"name": "رشدي اباظه", "photo": "https://envs.sh/wlx.jpg"},
    {"name": "كريم عبد العزيز", "photo": "https://envs.sh/PgJ.jpg"},
    {"name": "ملك قوره", "photo": "https://envs.sh/wkE.jpg"},
    {"name": "هدي المفتي", "photo": "https://envs.sh/wkD.jpg"},
    {"name": "اسماء ابو اليزيد", "photo": "https://envs.sh/wkQ.jpg"},
    {"name": "عمرو عبد الجليل", "photo": "https://envs.sh/wkd.jpg"},
    {"name": "محمد هنيدي", "photo": "https://envs.sh/wkF.jpg"},
    {"name": "حسين فهمي", "photo": "https://envs.sh/wkb.jpg"},
    {"name": "ماجد الكدواني", "photo": "https://envs.sh/wki.jpg"},
    {"name": "مصطفي خاطر", "photo": "https://envs.sh/wkw.jpg"},
    {"name": "اثر ياسين", "photo": "https://envs.sh/wkq.jpg"},
    {"name": "كارولين عزمي", "photo": "https://envs.sh/wk0.jpg"},
    {"name": "احمد ذكي", "photo": "https://envs.sh/wkS.jpg"},
    {"name": "رانيا يوسف", "photo": "https://envs.sh/wkB.jpg"},
    {"name": "ريهام عبد الغفور", "photo": "https://envs.sh/wkT.jpg"},
    {"name": "هاجر احمد", "photo": "https://envs.sh/wkn.jpg"}, 
    {"name": "زينه", "photo": "https://envs.sh/wkp.jpg"},
    {"name": "ريهام حجاج", "photo": "https://envs.sh/wkA.jpg"},
    {"name": "يسرا اللوزي", "photo": "https://envs.sh/wk_.jpg"},
    {"name": "هنا الزاهد", "photo": "https://envs.sh/wkL.jpg"},
    {"name": "رحاب الجمل", "photo": "https://envs.sh/wk5.jpg"},
    {"name": "مي الغيطي", "photo": "https://envs.sh/wkY.jpg"},
    {"name": "مني ذكي", "photo": "https://envs.sh/wkC.jpg"},
    {"name": "مروه انور", "photo": "https://envs.sh/wkR.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/wk1.jpg"},
    {"name": "شريف منير", "photo": "https://envs.sh/wk4.jpg"},
    {"name": "شيري عادل", "photo": "https://envs.sh/PHg.jpg"},
    {"name": "شيماء سيف", "photo": "https://envs.sh/wkU.jpg"},
    {"name": "هاني سلامه", "photo": "https://envs.sh/wk8.jpg"},
    {"name": "كريم فهمي", "photo": "https://envs.sh/wko.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/PHa.jpg"},
    {"name": "شيرين رضا", "photo": "https://envs.sh/PHO.jpg"},
    {"name": "هنا شيحه", "photo": "https://envs.sh/wkf.jpg"},
    {"name": "احمد عز", "photo": "https://envs.sh/wkm.jpg"},
    {"name": "داليا البحيري", "photo": "https://envs.sh/wkX.jpg"},
    {"name": "نور ايهاب", "photo": "https://envs.sh/wky.jpg"},
    {"name": "هاني رمزي", "photo": "https://envs.sh/wkx.jpg"},
    {"name": "امير كراره", "photo": "https://envs.sh/w8h.jpg"},
    {"name": "ايه سماحه", "photo": "https://envs.sh/w82.jpg"},
    {"name": "خالد الصاوي", "photo": "https://envs.sh/w8u.jpg"},
    {"name": "عادل امام", "photo": "https://envs.sh/w8F.jpg"},
    {"name": "نيلي كريم", "photo": "https://envs.sh/w8I.jpg"},
    {"name": "ياسمين صبري", "photo": "https://envs.sh/Pgd.jpg"},
    {"name": "احمد السقا", "photo": "https://envs.sh/w8p.jpg"},
    {"name": "سيد رجب", "photo": "https://envs.sh/w8_.jpg"},
    {"name": "حنان مطاوع", "photo": "https://envs.sh/w8s.jpg"},
    {"name": "عمر يوسف", "photo": "https://envs.sh/w8a.jpg"},
    {"name": "عمرو واكد", "photo": "https://envs.sh/w8O.jpg"},
    {"name": "سلمي ابو ضيف", "photo": "https://envs.sh/w8m.jpg"},
    {"name": "اكرم حسني", "photo": "https://envs.sh/w8X.jpg"},
    {"name": "ساره الشامي", "photo": "https://envs.sh/w8y.jpg"},
    {"name": "نور", "photo": "https://envs.sh/w86.jpg"},
    {"name": "احمد خاتم", "photo": "https://envs.sh/w8x.jpg"}
]

@Client.on_message(filters.command(["ممثل", "ممثلين","• ممثلين •"], ""), group=1024682131)
async def dhjfyuh(client, message):
    actor = random.choice(ph0otos)
    bot_username = client.me.username
    user_id = message.from_user.id
    c0aesar[user_id] = actor['name']
    u0sers[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الممثل...؟ ")

@Client.on_message(filters.text & filters.group, group=10790430)
async def yfugry(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in u0sers:
        correct_actor = c0aesar.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del c0aesar[user_id]
            del u0sers[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del c0aesar[user_id]
                del u0sers[user_id]

caesar1 = {}              
users1 = {}        

potss = [
    {"name": "بهاء سلطان", "photo": "https://envs.sh/wvE.jpg"},
    {"name": "محمد فؤاد", "photo": "https://envs.sh/wvh.jpg"},
    {"name":"شرين", "photo": "https://envs.sh/w9R.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/w9v.jpg"},
    {"name": "عمرو دياب", "photo": "https://envs.sh/wvF.jpg"},
    {"name": "اصاله", "photo": "https://envs.sh/PMT.jpg"},
    {"name": "عامر منيب", "photo": "https://envs.sh/wve.jpg"},
    {"name": "تامر حسني", "photo": "https://envs.sh/wNj.jpg"},
    {"name": "مدحت صالح", "photo": "https://envs.sh/wNL.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/wNG.jpg"},
    {"name": "محمد سعيد", "photo": "https://envs.sh/wNz.jpg"},
    {"name": "مصطفى قمر", "photo": "https://envs.sh/wNY.jpg"},
    {"name": "المغيني", "photo": "https://envs.sh/wHt.jpg"},
    {"name": "حكيم", "photo": "https://envs.sh/wHe.jpg"},
    {"name": "كاظم الساهر", "photo": "https://envs.sh/wHi.jpg"},
    {"name": "تامر عاشور", "photo": "https://envs.sh/wHw.jpg"},
    {"name": "هاني شاكر", "photo": "https://envs.sh/wHS.jpg"},
    {"name": "حسين الجسمي", "photo": "https://envs.sh/wHI.jpg"},
    {"name": "محمد منير", "photo": "https://envs.sh/PMi.jpg"},
    {"name": "رامي صبري", "photo": "https://envs.sh/wHn.jpg"},
    {"name": "ويجز", "photo": "https://envs.sh/Pf2.jpg"},
    {"name": "رامي جمال", "photo": "https://envs.sh/wHT.jpg"},
    {"name": "احمد شيبه", "photo": "https://envs.sh/PgX.jpg"},
    {"name": "نانسي عجرم", "photo": "https://envs.sh/wHp.jpg"},
    {"name": "راغب علامه", "photo": "https://envs.sh/wH_.jpg"},
    {"name": "عبد الحليم حافظ", "photo": "https://envs.sh/PfF.jpg"},
    {"name": "امال ماهر", "photo": "https://envs.sh/wHj.jpg"},
    {"name": "عبدالرحمن محمد", "photo": "https://envs.sh/Pga.jpg"},
    {"name": "احمد سعد", "photo": "https://envs.sh/wHZ.jpg"},
    {"name": "كارول سماحه", "photo": "https://envs.sh/wHL.jpg"},
    {"name": "ادهم نابلسي", "photo": "https://envs.sh/Pfi.jpg"},
    {"name": "محمود العسيلي", "photo": "https://envs.sh/Pg9.jpg"},
    {"name": "انغام", "photo": "https://envs.sh/wHG.jpg"},
    {"name": "كارمن سليمان", "photo": "https://envs.sh/wHz.jpg"},
    {"name": "سعد المجرد", "photo": "https://envs.sh/wHC.jpg"},
    {"name": "فيروز", "photo": "https://envs.sh/Pgm.jpg"},
    {"name": "ام كلثوم", "photo": "https://envs.sh/wH4.jpg"},
    {"name": "حماده هلال", "photo": "https://envs.sh/PMn.jpg"},
    {"name": "كايروكي", "photo": "https://envs.sh/wHk.jpg"},
    {"name": "لؤي", "photo": "https://envs.sh/wH8.jpg"},
    {"name": "ارسينك", "photo": "https://envs.sh/wH7.jpg"},
    {"name": "عاصي الحلاني", "photo": "https://envs.sh/PMB.jpg"},
    {"name": "احلام", "photo": "https://envs.sh/wHJ.jpg"},
    {"name": "اليسا", "photo": "https://envs.sh/wvB.jpg"},
    {"name": "محمد حماقي", "photo": "https://envs.sh/wHo.jpg"},
    {"name": "احمد مكي", "photo": "https://envs.sh/wHr.jpg"},
    {"name": "ابو الانوار", "photo": "https://envs.sh/PMb.jpg"}
]

@Client.on_message(filters.command(["مغنين", "مغاني","• مغنين •"], ""), group=107082131)
async def moganen(client, message):
    actor = random.choice(potss)
    bot_username = client.me.username
    user_id = message.from_user.id
    caesar1[user_id] = actor['name']
    users1[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا المغني...؟ ")

@Client.on_message(filters.text & filters.group, group=10126430)
async def mogany(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in users1:
        correct_actor = caesar1.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del caesar1[user_id]
            del users1[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del caesar1[user_id]
                del users1[user_id]

cpaesr2 = {}              
upsrs2 = {}        

patos = [
    {"name": "ماليزيا", "photo": "https://envs.sh/wfz.jpg"},
    {"name": "الاردن", "photo": "https://envs.sh/wfl.jpg"},
    {"name": "الفاتيكان", "photo": "https://envs.sh/wfJ.jpg"},
    {"name": "الصين", "photo": "https://envs.sh/wfs.jpg"},
    {"name": "النيجر", "photo": "https://envs.sh/wf9.jpg"},
    {"name": "مصر", "photo": "https://envs.sh/wfN.jpg"},
    {"name": "سويسرا", "photo": "https://envs.sh/wfM.jpg"},
    {"name": "جزر الباهاما", "photo": "https://envs.sh/wfX.jpg"},
    {"name": "تشاد", "photo": "https://envs.sh/wf6.jpg"},
    {"name": "استونيا", "photo": "https://envs.sh/wfx.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "انجلترا", "photo": "https://envs.sh/waE.jpg"},
    {"name": "البرازيل", "photo": "https://envs.sh/wah.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wau.jpg"},
    {"name": "تونس", "photo": "https://envs.sh/wab.jpg"},
    {"name": "ليبيريا", "photo": "https://envs.sh/waP.jpg"},
    {"name": "مالي", "photo": "https://envs.sh/waw.jpg"},
    {"name": "الكونغو", "photo": "https://envs.sh/wa0.jpg"},
    {"name": "العراق", "photo": "https://envs.sh/waS.jpg"},
    {"name": "ارمينيا", "photo": "https://envs.sh/waI.jpg"},
    {"name": "اسبانيا", "photo": "https://envs.sh/waA.jpg"},
    {"name": "السنغال", "photo": "https://envs.sh/waj.jpg"},
    {"name": "البرتغال", "photo": "https://envs.sh/wac.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "لوكسمبورغ", "photo": "https://envs.sh/waZ.jpg"},
    {"name": "البوسنه", "photo": "https://envs.sh/waL.jpg"},
    {"name": "فلسطين", "photo": "https://envs.sh/wa5.jpg"},
    {"name": "كينيا", "photo": "https://envs.sh/waK.jpg"},
    {"name": "سان مارينو", "photo": "https://envs.sh/waz.jpg"},
    {"name": "الفلبين", "photo": "https://envs.sh/wa-.jpg"},
    {"name": "المكسيك", "photo": "https://envs.sh/wOE.jpg"},
    {"name": "لاوس", "photo": "https://envs.sh/wOQ.jpg"},
    {"name": "باكستان", "photo": "https://envs.sh/wOh.jpg"},
    {"name": "الجبل الاسود", "photo": "https://envs.sh/wO2.jpg"},
    {"name": "موزمبيق", "photo": "https://envs.sh/wOi.jpg"},
    {"name": "روسيا", "photo": "https://envs.sh/wOw.jpg"},
    {"name": "افغانستان", "photo": "https://envs.sh/wap.jpg"},
    {"name": "البرتغال", "photo": "https://envs.sh/wac.jpg"},
    {"name": "اندونيسيا", "photo": "https://envs.sh/wO0.jpg"},
    {"name": "الرأس الاخضر", "photo": "https://envs.sh/wOS.jpg"},
    {"name": "هولندا", "photo": "https://envs.sh/wOI.jpg"},
    {"name": "اندونسيا", "photo": "https://envs.sh/wO0.jpg"},
    {"name": "فنلندا", "photo": "https://envs.sh/wmu.jpg"},
    {"name": "الكونغو الديموقراطية", "photo": "https://envs.sh/wmt.jpg"},
    {"name": "النمسا", "photo": "https://envs.sh/wmP.jpg"},
    {"name": "ايطاليا", "photo": "https://envs.sh/wmq.jpg"},
    {"name": "لوكسمبورغ", "photo": "https://envs.sh/waZ.jpg"},
    {"name": "السعوديه", "photo": "https://envs.sh/wmS.jpg"},
    {"name": "كولومبيا", "photo": "https://envs.sh/wmW.jpg"},
    {"name": "نيجريا", "photo": "https://envs.sh/wmB.jpg"},
    {"name": "نيبال", "photo": "https://envs.sh/wmI.jpg"},
    {"name": "الاردن", "photo": "https://envs.sh/wfl.jpg"},
    {"name": "السويد", "photo": "https://envs.sh/wmA.jpg"},
    {"name": "ليبيريا", "photo": "https://envs.sh/waP.jpg"},
    {"name": "انغولا", "photo": "https://envs.sh/wmc.jpg"},
    {"name": "جيبوتي", "photo": "https://envs.sh/wmZ.jpg"},
    {"name": "المجر", "photo": "https://envs.sh/wfv.jpg"},
    {"name": "سوريا", "photo": "https://envs.sh/wmL.jpg"},
    {"name": "ايرلندا", "photo": "https://envs.sh/wm5.jpg"},
    {"name": "كازاخستان", "photo": "https://envs.sh/wmz.jpg"},
    {"name": "بنين", "photo": "https://envs.sh/wan.jpg"},
    {"name": "بنغلاديش", "photo": "https://envs.sh/wOt.jpg"},
    {"name": "قبرص", "photo": "https://envs.sh/wmk.jpg"},
    {"name": "تنزانيا", "photo": "https://envs.sh/wm8.jpg"},
    {"name": "افريقيا الوسطى", "photo": "https://envs.sh/wm7.jpg"},
    {"name": "مقدونيا", "photo": "https://envs.sh/PgC.jpg"},
    {"name": "موريتانيا", "photo": "https://envs.sh/wmr.jpg"},
    {"name": "غنيا الاستوائية", "photo": "https://envs.sh/wms.jpg"},
    {"name": "فرنسا", "photo": "https://envs.sh/wMF.jpg"},
    {"name": "اليابان", "photo": "https://envs.sh/wMt.jpg"},
    {"name": "فيتنام", "photo": "https://envs.sh/wMi.jpg"},
    {"name": "مالطا", "photo": "https://envs.sh/wMP.jpg"},
    {"name": "تايوان", "photo": "https://envs.sh/wM0.jpg"},
    {"name": "بوروندي", "photo": "https://envs.sh/wMB.jpg"},
    {"name": "مالاوي", "photo": "https://envs.sh/wMT.jpg"},
    {"name": "اثيوبيا", "photo": "https://envs.sh/wMp.jpg"},
    {"name": "لبنان", "photo": "https://envs.sh/wM_.jpg"},
    {"name": "البانيا", "photo": "https://envs.sh/wMj.jpg"},
    {"name": "تايلاند", "photo": "https://envs.sh/wMc.jpg"},
    {"name": "جنوب افريقيا", "photo": "https://envs.sh/wMZ.jpg"},
    {"name": "طاجيكستان", "photo": "https://envs.sh/wfk.jpg"},
    {"name": "تونس", "photo": "https://envs.sh/wab.jpg"},
    {"name": "استراليا", "photo": "https://envs.sh/wMK.jpg"},
    {"name": "السودان", "photo": "https://envs.sh/wM3.jpg"},
    {"name": "غانا", "photo": "https://envs.sh/wMC.jpg"},
    {"name": "الفاتيكان", "photo": "https://envs.sh/wfJ.jpg"},
    {"name": "قطر", "photo": "https://envs.sh/wM4.jpg"},
    {"name": "الجزائر", "photo": "https://envs.sh/wMU.jpg"},
    {"name": "جزر القمر", "photo": "https://envs.sh/wMk.jpg"},
    {"name": "البوسنه", "photo": "https://envs.sh/waL.jpg"},
    {"name": "الدنمارك", "photo": "https://envs.sh/wfm.jpg"},
    {"name": "صربيا", "photo": "https://envs.sh/wM8.jpg"},
    {"name": "البحرين", "photo": "https://envs.sh/wOu.jpg"},
    {"name": "سنغافورة", "photo": "https://envs.sh/wMo.jpg"},
    {"name": "ايران", "photo": "https://envs.sh/wMr.jpg"},
    {"name": "جيبوتي", "photo": "https://envs.sh/wmZ.jpg"},
    {"name": "أذربيجاني", "photo": "https://envs.sh/wMN.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wau.jpg"},
    {"name": "اوغندا", "photo": "https://envs.sh/wfo.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wmB.jpg"},
    {"name": "بلجيكا", "photo": "https://envs.sh/wMa.jpg"},
    {"name": "ايسلندا", "photo": "https://envs.sh/wMO.jpg"},
    {"name": "تشاد", "photo": "https://envs.sh/wf6.jpg"},
    {"name": "اريتريا", "photo": "https://envs.sh/wMy.jpg"},
    {"name": "سيشل", "photo": "https://envs.sh/wMx.jpg"},
    {"name": "لاوس", "photo": "https://envs.sh/wOQ.jpg"},
    {"name": "الامارات", "photo": "https://envs.sh/wXD.jpg"},
    {"name": "النرويج", "photo": "https://envs.sh/wXE.jpg"},
    {"name": "زامبيا", "photo": "https://envs.sh/wXh.jpg"},
    {"name": "ماليزيا", "photo": "https://envs.sh/wfz.jpg"},
    {"name": "المانيا", "photo": "https://envs.sh/wXd.jpg"},
    {"name": "السنغال", "photo": "https://envs.sh/waj.jpg"},
    {"name": "اوكرانيا", "photo": "https://envs.sh/wXu.jpg"},
    {"name": "الصومال", "photo": "https://envs.sh/wXt.jpg"},
    {"name": "بوركينافاسو", "photo": "https://envs.sh/wXb.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "سلوفينيا", "photo": "https://envs.sh/wVY.jpg"},
    {"name": "ليبيا", "photo": "https://envs.sh/wVJ.jpg"},
    {"name": "جزر المالديف", "photo": "https://envs.sh/wVo.jpg"},
    {"name": "كندا", "photo": "https://envs.sh/wVs.jpg"},
    {"name": "روسيا", "photo": "https://envs.sh/wOw.jpg"},
    {"name": "اليونان", "photo": "https://envs.sh/wVH.jpg"}
]

@Client.on_message(filters.command(["اعلام", "علم","• اعلام •"], ""), group=101237782131)
async def aalame(client, message):
    actor = random.choice(patos)
    bot_username = client.me.username
    user_id = message.from_user.id
    cpaesr2[user_id] = actor['name']
    upsrs2[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا العلم...؟ ")

@Client.on_message(filters.text & filters.group, group=11026439870)
async def alamy(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in upsrs2:
        correct_actor = cpaesr2.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del cpaesr2[user_id]
            del upsrs2[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del cpaesr2[user_id]
                del upsrs2[user_id]
                
caesar3 = {}              
users3 = {}        

photn = [
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "حسين الشحات", "photo": "https://envs.sh/wHM.jpg"},
    {"name": "كهربا", "photo": "https://envs.sh/wHX.jpg"},
    {"name": "هاري كين", "photo": "https://envs.sh/PmT.jpg"},
    {"name": "رياض محرز", "photo": "https://envs.sh/wHy.jpg"},
    {"name": "حمدي فتحي", "photo": "https://envs.sh/wH6.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "داني الفيس", "photo": "https://envs.sh/wg2.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "فابينيو", "photo": "https://envs.sh/wgF.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "طاهر محمد", "photo": "https://envs.sh/POa.jpg"},
    {"name": "مارسيلو", "photo": "https://envs.sh/wge.jpg"},
    {"name": "أفشة", "photo": "https://envs.sh/PyU.jpg"},
    {"name": "سيرجيو بوسكيتس", "photo": "https://envs.sh/wDP.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "انطونيو جريزمان", "photo": "https://envs.sh/wgw.jpg"},
    {"name": "احمد حسام ميدو", "photo": "https://envs.sh/Py9.jpg"},
    {"name": "أدريان رابيو", "photo": "https://envs.sh/PyR.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "مانويل نوير", "photo": "https://envs.sh/Py1.jpg"},
    {"name": "رافاييل فاران", "photo": "https://envs.sh/PmW.jpg"},
    {"name": "توني كروس", "photo": "https://envs.sh/wgB.jpg"},
    {"name": "جاريث بيل", "photo": "https://envs.sh/Pyo.jpg"},
    {"name": "نيمار", "photo": "https://envs.sh/wgT.jpg"},
    {"name": "كارفاخال", "photo": "https://envs.sh/Pmm.jpg"},
    {"name": "دي ماريا", "photo": "https://envs.sh/Py0.jpg"},
    {"name": "زين الدين زيدان", "photo": "https://envs.sh/Py4.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "حكيم زياش", "photo": "https://envs.sh/wgZ.jpg"},
    {"name": "جونزالو هيجواين", "photo": "https://envs.sh/wgL.jpg"},
    {"name": "جوردي ألبا", "photo": "https://envs.sh/wgG.jpg"},
    {"name": "باولو ديبالا", "photo": "https://envs.sh/wgK.jpg"},
    {"name": "دييجو كوستا", "photo": "https://envs.sh/Pys.jpg"},
    {"name": "بيليه", "photo": "https://envs.sh/Pme.jpg"},
    {"name": "هالاند", "photo": "https://envs.sh/PmO.jpg"},
    {"name": "بول بوجبا", "photo": "https://envs.sh/wgz.jpg"},
    {"name": "إدين هازارد", "photo": "https://envs.sh/wg3.jpg"},
    {"name": "نجولو كانتي", "photo": "https://envs.sh/PmV.jpg"},
    {"name": "عصام الحضري", "photo": "https://envs.sh/wgY.jpg"},
    {"name": "لوكاكو", "photo": "https://envs.sh/POg.jpg"},
    {"name": "إنييستا", "photo": "https://envs.sh/wgC.jpg"},
    {"name": "اسماعيل بن ناصر", "photo": "https://envs.sh/wgR.jpg"},
    {"name": "ساديو ماني", "photo": "https://envs.sh/wg1.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ريفالدو", "photo": "https://envs.sh/Pyk.jpg"},
    {"name": "لورينزو إنسيني", "photo": "https://envs.sh/Pyw.jpg"},
    {"name": "جابرييل جيسوس", "photo": "https://envs.sh/Pmc.jpg"},
    {"name": "أرتورو فيدال", "photo": "https://envs.sh/wgU.jpg"},
    {"name": "ماتس هاملز", "photo": "https://envs.sh/wgl.jpg"},
    {"name": "تيو كورتوا", "photo": "https://envs.sh/wgk.jpg"},
    {"name": "ماركو اسينسيو", "photo": "https://envs.sh/wg8.jpg"},
    {"name": "محمد النيني", "photo": "https://envs.sh/Pyr.jpg"},
    {"name": "محمد صلاح", "photo": "https://envs.sh/POO.jpg"},
    {"name": "فيليب كوتينيو", "photo": "https://envs.sh/wgJ.jpg"},
    {"name": "مسعود اوزيل", "photo": "https://envs.sh/PyI.jpg"},
    {"name": "ماركوس راشفورد", "photo": "https://envs.sh/wgo.jpg"},
    {"name": "بونو", "photo": "https://envs.sh/wgr.jpg"},
    {"name": "لوكا مودريتش", "photo": "https://envs.sh/wg9.jpg"},
    {"name": "نيمانيا ماتيتش", "photo": "https://envs.sh/PmP.jpg"},
    {"name": "سيرجيو أجويرو", "photo": "https://envs.sh/wgv.jpg"},
    {"name": "إيفان راكيتيتش", "photo": "https://envs.sh/wgN.jpg"},
    {"name": "ميسي", "photo": "https://envs.sh/wgH.jpg"},
    {"name": "بيكيه", "photo": "https://envs.sh/Pgg.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "كرويف", "photo": "https://envs.sh/wgg.jpg"},
    {"name": "رادجا ناينجولان", "photo": "https://envs.sh/Px6.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "كاسيميرو", "photo": "https://envs.sh/wgm.jpg"},
    {"name": "جيمي فاردي", "photo": "https://envs.sh/wgX.jpg"},
    {"name": "ليروي ساني", "photo": "https://envs.sh/wgy.jpg"},
    {"name": "آلابا", "photo": "https://envs.sh/wgx.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ديلي آلي", "photo": "https://envs.sh/Pyb.jpg"},
    {"name": "جوتا", "photo": "https://envs.sh/wfD.jpg"},
    {"name": "علي معلول", "photo": "https://envs.sh/wfE.jpg"},
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "مارادونا", "photo": "https://envs.sh/Py_.jpg"},
    {"name": "جورجيو كيليني", "photo": "https://envs.sh/Pyu.jpg"},
    {"name": "سيرجيو راموس", "photo": "https://envs.sh/PME.jpg"},
    {"name": "صامويل أومتيتي", "photo": "https://envs.sh/PmX.jpg"},
    {"name": "زلاتان", "photo": "https://envs.sh/Pyt.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "اشرف حكيمي", "photo": "https://envs.sh/wfh.jpg"},
    {"name": "نايف اكرد", "photo": "https://envs.sh/Pmt.jpg"},
    {"name": "ماورو إيكاردي", "photo": "https://envs.sh/PyW.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "فودين", "photo": "https://envs.sh/Py8.jpg"},
    {"name": "لويس سواريز", "photo": "https://envs.sh/wf2.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "كريستيانو رونالدو", "photo": "https://envs.sh/PO6.jpg"},
    {"name": "كفين دي بروين", "photo": "https://envs.sh/Pmx.jpg"},
    {"name": "آريين روبن", "photo": "https://envs.sh/wfe.jpg"}
]

@Client.on_message(filters.command(["لاعبين", "لاعب","• لاعبين •"], ""), group=9827065)
async def laaban(client, message):
    actor = random.choice(photn)
    bot_username = client.me.username
    user_id = message.from_user.id
    caesar3[user_id] = actor['name']
    users3[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الاعب..؟ ")

@Client.on_message(filters.text & filters.group, group=458678)
async def alaeb(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in users3:
        correct_actor = caesar3.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del caesar3[user_id]
            del users3[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del caesar3[user_id]
                del users3[user_id]

cesar4 = {}              
urers4 = {}        

soraa = [
    {"name": "بهاء سلطان", "photo": "https://envs.sh/wvE.jpg"},
    {"name": "محمد فؤاد", "photo": "https://envs.sh/wvh.jpg"},
    {"name":"شرين", "photo": "https://envs.sh/w9R.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/w9v.jpg"},
    {"name": "عمرو دياب", "photo": "https://envs.sh/wvF.jpg"},
    {"name": "اصاله", "photo": "https://envs.sh/PMT.jpg"},
    {"name": "عامر منيب", "photo": "https://envs.sh/wve.jpg"},
    {"name": "تامر حسني", "photo": "https://envs.sh/wNj.jpg"},
    {"name": "مدحت صالح", "photo": "https://envs.sh/wNL.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/wNG.jpg"},
    {"name": "محمد سعيد", "photo": "https://envs.sh/wNz.jpg"},
    {"name": "مصطفى قمر", "photo": "https://envs.sh/wNY.jpg"},
    {"name": "المغيني", "photo": "https://envs.sh/wHt.jpg"},
    {"name": "حكيم", "photo": "https://envs.sh/wHe.jpg"},
    {"name": "كاظم الساهر", "photo": "https://envs.sh/wHi.jpg"},
    {"name": "تامر عاشور", "photo": "https://envs.sh/wHw.jpg"},
    {"name": "هاني شاكر", "photo": "https://envs.sh/wHS.jpg"},
    {"name": "حسين الجسمي", "photo": "https://envs.sh/wHI.jpg"},
    {"name": "محمد منير", "photo": "https://envs.sh/PMi.jpg"},
    {"name": "رامي صبري", "photo": "https://envs.sh/wHn.jpg"},
    {"name": "ويجز", "photo": "https://envs.sh/Pf2.jpg"},
    {"name": "رامي جمال", "photo": "https://envs.sh/wHT.jpg"},
    {"name": "احمد شيبه", "photo": "https://envs.sh/PgX.jpg"},
    {"name": "نانسي عجرم", "photo": "https://envs.sh/wHp.jpg"},
    {"name": "راغب علامه", "photo": "https://envs.sh/wH_.jpg"},
    {"name": "عبد الحليم حافظ", "photo": "https://envs.sh/PfF.jpg"},
    {"name": "امال ماهر", "photo": "https://envs.sh/wHj.jpg"},
    {"name": "عبدالرحمن محمد", "photo": "https://envs.sh/Pga.jpg"},
    {"name": "احمد سعد", "photo": "https://envs.sh/wHZ.jpg"},
    {"name": "كارول سماحه", "photo": "https://envs.sh/wHL.jpg"},
    {"name": "ادهم نابلسي", "photo": "https://envs.sh/Pfi.jpg"},
    {"name": "محمود العسيلي", "photo": "https://envs.sh/Pg9.jpg"},
    {"name": "انغام", "photo": "https://envs.sh/wHG.jpg"},
    {"name": "كارمن سليمان", "photo": "https://envs.sh/wHz.jpg"},
    {"name": "سعد المجرد", "photo": "https://envs.sh/wHC.jpg"},
    {"name": "فيروز", "photo": "https://envs.sh/Pgm.jpg"},
    {"name": "ام كلثوم", "photo": "https://envs.sh/wH4.jpg"},
    {"name": "حماده هلال", "photo": "https://envs.sh/PMn.jpg"},
    {"name": "كايروكي", "photo": "https://envs.sh/wHk.jpg"},
    {"name": "لؤي", "photo": "https://envs.sh/wH8.jpg"},
    {"name": "ارسينك", "photo": "https://envs.sh/wH7.jpg"},
    {"name": "عاصي الحلاني", "photo": "https://envs.sh/PMB.jpg"},
    {"name": "احلام", "photo": "https://envs.sh/wHJ.jpg"},
    {"name": "اليسا", "photo": "https://envs.sh/wvB.jpg"},
    {"name": "محمد حماقي", "photo": "https://envs.sh/wHo.jpg"},
    {"name": "احمد مكي", "photo": "https://envs.sh/wHr.jpg"},
    {"name": "ابو الانوار", "photo": "https://envs.sh/PMb.jpg"}, 
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "حسين الشحات", "photo": "https://envs.sh/wHM.jpg"},
    {"name": "كهربا", "photo": "https://envs.sh/wHX.jpg"},
    {"name": "هاري كين", "photo": "https://envs.sh/PmT.jpg"},
    {"name": "رياض محرز", "photo": "https://envs.sh/wHy.jpg"},
    {"name": "حمدي فتحي", "photo": "https://envs.sh/wH6.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "داني الفيس", "photo": "https://envs.sh/wg2.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "فابينيو", "photo": "https://envs.sh/wgF.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "طاهر محمد", "photo": "https://envs.sh/POa.jpg"},
    {"name": "مارسيلو", "photo": "https://envs.sh/wge.jpg"},
    {"name": "أفشة", "photo": "https://envs.sh/PyU.jpg"},
    {"name": "سيرجيو بوسكيتس", "photo": "https://envs.sh/wDP.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "انطونيو جريزمان", "photo": "https://envs.sh/wgw.jpg"},
    {"name": "احمد حسام ميدو", "photo": "https://envs.sh/Py9.jpg"},
    {"name": "أدريان رابيو", "photo": "https://envs.sh/PyR.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "مانويل نوير", "photo": "https://envs.sh/Py1.jpg"},
    {"name": "رافاييل فاران", "photo": "https://envs.sh/PmW.jpg"},
    {"name": "توني كروس", "photo": "https://envs.sh/wgB.jpg"},
    {"name": "جاريث بيل", "photo": "https://envs.sh/Pyo.jpg"},
    {"name": "نيمار", "photo": "https://envs.sh/wgT.jpg"},
    {"name": "كارفاخال", "photo": "https://envs.sh/Pmm.jpg"},
    {"name": "دي ماريا", "photo": "https://envs.sh/Py0.jpg"},
    {"name": "زين الدين زيدان", "photo": "https://envs.sh/Py4.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "حكيم زياش", "photo": "https://envs.sh/wgZ.jpg"},
    {"name": "جونزالو هيجواين", "photo": "https://envs.sh/wgL.jpg"},
    {"name": "جوردي ألبا", "photo": "https://envs.sh/wgG.jpg"},
    {"name": "باولو ديبالا", "photo": "https://envs.sh/wgK.jpg"},
    {"name": "دييجو كوستا", "photo": "https://envs.sh/Pys.jpg"},
    {"name": "بيليه", "photo": "https://envs.sh/Pme.jpg"},
    {"name": "هالاند", "photo": "https://envs.sh/PmO.jpg"},
    {"name": "بول بوجبا", "photo": "https://envs.sh/wgz.jpg"},
    {"name": "إدين هازارد", "photo": "https://envs.sh/wg3.jpg"},
    {"name": "نجولو كانتي", "photo": "https://envs.sh/PmV.jpg"},
    {"name": "عصام الحضري", "photo": "https://envs.sh/wgY.jpg"},
    {"name": "لوكاكو", "photo": "https://envs.sh/POg.jpg"},
    {"name": "إنييستا", "photo": "https://envs.sh/wgC.jpg"},
    {"name": "اسماعيل بن ناصر", "photo": "https://envs.sh/wgR.jpg"},
    {"name": "ساديو ماني", "photo": "https://envs.sh/wg1.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ريفالدو", "photo": "https://envs.sh/Pyk.jpg"},
    {"name": "لورينزو إنسيني", "photo": "https://envs.sh/Pyw.jpg"},
    {"name": "جابرييل جيسوس", "photo": "https://envs.sh/Pmc.jpg"},
    {"name": "أرتورو فيدال", "photo": "https://envs.sh/wgU.jpg"},
    {"name": "ماتس هاملز", "photo": "https://envs.sh/wgl.jpg"},
    {"name": "تيو كورتوا", "photo": "https://envs.sh/wgk.jpg"},
    {"name": "ماركو اسينسيو", "photo": "https://envs.sh/wg8.jpg"},
    {"name": "محمد النيني", "photo": "https://envs.sh/Pyr.jpg"},
    {"name": "محمد صلاح", "photo": "https://envs.sh/POO.jpg"},
    {"name": "فيليب كوتينيو", "photo": "https://envs.sh/wgJ.jpg"},
    {"name": "مسعود اوزيل", "photo": "https://envs.sh/PyI.jpg"},
    {"name": "ماركوس راشفورد", "photo": "https://envs.sh/wgo.jpg"},
    {"name": "بونو", "photo": "https://envs.sh/wgr.jpg"},
    {"name": "لوكا مودريتش", "photo": "https://envs.sh/wg9.jpg"},
    {"name": "نيمانيا ماتيتش", "photo": "https://envs.sh/PmP.jpg"},
    {"name": "سيرجيو أجويرو", "photo": "https://envs.sh/wgv.jpg"},
    {"name": "إيفان راكيتيتش", "photo": "https://envs.sh/wgN.jpg"},
    {"name": "ميسي", "photo": "https://envs.sh/wgH.jpg"},
    {"name": "بيكيه", "photo": "https://envs.sh/Pgg.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "كرويف", "photo": "https://envs.sh/wgg.jpg"},
    {"name": "رادجا ناينجولان", "photo": "https://envs.sh/Px6.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "كاسيميرو", "photo": "https://envs.sh/wgm.jpg"},
    {"name": "جيمي فاردي", "photo": "https://envs.sh/wgX.jpg"},
    {"name": "ليروي ساني", "photo": "https://envs.sh/wgy.jpg"},
    {"name": "آلابا", "photo": "https://envs.sh/wgx.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ديلي آلي", "photo": "https://envs.sh/Pyb.jpg"},
    {"name": "جوتا", "photo": "https://envs.sh/wfD.jpg"},
    {"name": "علي معلول", "photo": "https://envs.sh/wfE.jpg"},
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "مارادونا", "photo": "https://envs.sh/Py_.jpg"},
    {"name": "جورجيو كيليني", "photo": "https://envs.sh/Pyu.jpg"},
    {"name": "سيرجيو راموس", "photo": "https://envs.sh/PME.jpg"},
    {"name": "صامويل أومتيتي", "photo": "https://envs.sh/PmX.jpg"},
    {"name": "زلاتان", "photo": "https://envs.sh/Pyt.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "اشرف حكيمي", "photo": "https://envs.sh/wfh.jpg"},
    {"name": "نايف اكرد", "photo": "https://envs.sh/Pmt.jpg"},
    {"name": "ماورو إيكاردي", "photo": "https://envs.sh/PyW.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "فودين", "photo": "https://envs.sh/Py8.jpg"},
    {"name": "لويس سواريز", "photo": "https://envs.sh/wf2.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "كريستيانو رونالدو", "photo": "https://envs.sh/PO6.jpg"},
    {"name": "كفين دي بروين", "photo": "https://envs.sh/Pmx.jpg"},
    {"name": "آريين روبن", "photo": "https://envs.sh/wfe.jpg"}, 
    {"name": "محمد سعد", "photo": "https://envs.sh/wl8.jpg"},
    {"name": "نرمين الفقي", "photo": "https://envs.sh/wlJ.jpg"},
    {"name": "عبله كامل", "photo": "https://envs.sh/wlr.jpg"},
    {"name": "دينا الشربيني", "photo": "https://envs.sh/wls.jpg"},
    {"name": "ليلي احمد زاهر", "photo": "https://envs.sh/wl9.jpg"},
    {"name": "روبي", "photo": "https://envs.sh/wlv.jpg"},
    {"name": "غاده عادل", "photo": "https://envs.sh/wlN.jpg"},
    {"name": "ياسمين عبد العزيز", "photo": "https://envs.sh/wlH.jpg"},
    {"name": "اسماء جلال", "photo": "https://envs.sh/wlg.jpg"},
    {"name": "امينه خليل", "photo": "https://envs.sh/wla.jpg"},
    {"name": "احمد فهمي", "photo": "https://envs.sh/PHf.jpg"},
    {"name": "رنا رئيس", "photo": "https://envs.sh/wlM.jpg"},
    {"name": "باسم سمره", "photo": "https://envs.sh/wlX.jpg"},
    {"name": "محمد سلام", "photo": "https://envs.sh/wly.jpg"},
    {"name": "ميرنا نور الدين", "photo": "https://envs.sh/wlV.jpg"},
    {"name": "رشدي اباظه", "photo": "https://envs.sh/wlx.jpg"},
    {"name": "كريم عبد العزيز", "photo": "https://envs.sh/PgJ.jpg"},
    {"name": "ملك قوره", "photo": "https://envs.sh/wkE.jpg"},
    {"name": "هدي المفتي", "photo": "https://envs.sh/wkD.jpg"},
    {"name": "اسماء ابو اليزيد", "photo": "https://envs.sh/wkQ.jpg"},
    {"name": "عمرو عبد الجليل", "photo": "https://envs.sh/wkd.jpg"},
    {"name": "محمد هنيدي", "photo": "https://envs.sh/wkF.jpg"},
    {"name": "حسين فهمي", "photo": "https://envs.sh/wkb.jpg"},
    {"name": "ماجد الكدواني", "photo": "https://envs.sh/wki.jpg"},
    {"name": "مصطفي خاطر", "photo": "https://envs.sh/wkw.jpg"},
    {"name": "اثر ياسين", "photo": "https://envs.sh/wkq.jpg"},
    {"name": "كارولين عزمي", "photo": "https://envs.sh/wk0.jpg"},
    {"name": "احمد ذكي", "photo": "https://envs.sh/wkS.jpg"},
    {"name": "رانيا يوسف", "photo": "https://envs.sh/wkB.jpg"},
    {"name": "ريهام عبد الغفور", "photo": "https://envs.sh/wkT.jpg"},
    {"name": "هاجر احمد", "photo": "https://envs.sh/wkn.jpg"},
    {"name": "زينه", "photo": "https://envs.sh/wkp.jpg"},
    {"name": "ريهام حجاج", "photo": "https://envs.sh/wkA.jpg"},
    {"name": "يسرا اللوزي", "photo": "https://envs.sh/wk_.jpg"},
    {"name": "هنا الزاهد", "photo": "https://envs.sh/wkL.jpg"},
    {"name": "رحاب الجمل", "photo": "https://envs.sh/wk5.jpg"},
    {"name": "مي الغيطي", "photo": "https://envs.sh/wkY.jpg"},
    {"name": "مني ذكي", "photo": "https://envs.sh/wkC.jpg"},
    {"name": "مروه انور", "photo": "https://envs.sh/wkR.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/wk1.jpg"},
    {"name": "شريف منير", "photo": "https://envs.sh/wk4.jpg"},
    {"name": "شيري عادل", "photo": "https://envs.sh/PHg.jpg"},
    {"name": "شيماء سيف", "photo": "https://envs.sh/wkU.jpg"},
    {"name": "هاني سلامه", "photo": "https://envs.sh/wk8.jpg"},
    {"name": "كريم فهمي", "photo": "https://envs.sh/wko.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/PHa.jpg"},
    {"name": "شيرين رضا", "photo": "https://envs.sh/PHO.jpg"},
    {"name": "هنا شيحه", "photo": "https://envs.sh/wkf.jpg"},
    {"name": "احمد عز", "photo": "https://envs.sh/wkm.jpg"},
    {"name": "داليا البحيري", "photo": "https://envs.sh/wkX.jpg"},
    {"name": "نور ايهاب", "photo": "https://envs.sh/wky.jpg"},
    {"name": "هاني رمزي", "photo": "https://envs.sh/wkx.jpg"},
    {"name": "امير كراره", "photo": "https://envs.sh/w8h.jpg"},
    {"name": "ايه سماحه", "photo": "https://envs.sh/w82.jpg"},
    {"name": "خالد الصاوي", "photo": "https://envs.sh/w8u.jpg"},
    {"name": "عادل امام", "photo": "https://envs.sh/w8F.jpg"},
    {"name": "نيلي كريم", "photo": "https://envs.sh/w8I.jpg"},
    {"name": "ياسمين صبري", "photo": "https://envs.sh/Pgd.jpg"},
    {"name": "احمد السقا", "photo": "https://envs.sh/w8p.jpg"},
    {"name": "سيد رجب", "photo": "https://envs.sh/w8_.jpg"},
    {"name": "حنان مطاوع", "photo": "https://envs.sh/w8s.jpg"},
    {"name": "عمر يوسف", "photo": "https://envs.sh/w8a.jpg"},
    {"name": "عمرو واكد", "photo": "https://envs.sh/w8O.jpg"},
    {"name": "سلمي ابو ضيف", "photo": "https://envs.sh/w8m.jpg"},
    {"name": "اكرم حسني", "photo": "https://envs.sh/w8X.jpg"},
    {"name": "ساره الشامي", "photo": "https://envs.sh/w8y.jpg"},
    {"name": "نور", "photo": "https://envs.sh/w86.jpg"},
    {"name": "احمد خاتم", "photo": "https://envs.sh/w8x.jpg"}
]

@Client.on_message(filters.command(["مشاهير", "مشهور","• مشاهير •"], ""), group=700953)
async def masher(client, message):
    actor = random.choice(soraa)
    bot_username = client.me.username
    user_id = message.from_user.id
    cesar4[user_id] = actor['name']
    urers4[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا المشهور...؟ ")

@Client.on_message(filters.text & filters.group, group=75205)
async def mashor(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in urers4:
        correct_actor = cesar4.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del cesar4[user_id]
            del urers4[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del cesar4[user_id]
                del urers4[user_id]

ces5ar5 = {}              
ur5ers5 = {}        

so5raa5 = [
    {"name": "البدله", "photo": "https://envs.sh/Wsv.jpg"},
    {"name": "الحفله", "photo": "https://envs.sh/WsN.jpg"},
    {"name": "الارهابي", "photo": "https://envs.sh/Wsa.jpg"},
    {"name": "اكس لارج", "photo": "https://envs.sh/WsO.jpg"},
    {"name": "الرهينه", "photo": "https://envs.sh/Wsm.jpg"},
    {"name": "افواه وارانب", "photo": "https://envs.sh/WsX.jpg"},
    {"name": "ارض الخوف", "photo": "https://envs.sh/Wsy.jpg"},
    {"name": "الكيت كات", "photo": "https://envs.sh/Ws6.jpg"},
    {"name": "الفيل الازرق", "photo": "https://envs.sh/Wsx.jpg"},
    {"name": "باب الشمس", "photo": "https://envs.sh/W9E.jpg"},
    {"name": "السلم والثعبان", "photo": "https://envs.sh/Ws-.jpg"},
    {"name": "بطل من ورق", "photo": "https://envs.sh/Wve.jpg"},
    {"name": "الجوع", "photo": "https://envs.sh/Wvb.jpg"},
    {"name": "البيضه والحجر", "photo": "https://envs.sh/Ws9.jpg"},
    {"name": "المركب", "photo": "https://envs.sh/WvZ.jpg"},
    {"name": "جواب اعتقال ", "photo": "https://envs.sh/WvK.jpg"},
    {"name": "الرساله", "photo": "https://envs.sh/Wv4.jpg"},
    {"name": "السقا مات", "photo": "https://envs.sh/Wvk.jpg"},
    {"name": "الفرح", "photo": "https://envs.sh/Wvo.jpg"},
    {"name": "النمر الاسود", "photo": "https://envs.sh/WvN.jpg"},
    {"name": "الشبح", "photo": "https://envs.sh/Wvf.jpg"},
    {"name": "العصفور", "photo": "https://envs.sh/Wvm.jpg"},
    {"name": "بحب السيما", "photo": "https://envs.sh/Wvy.jpg"},
    {"name": "النمر والانثي", "photo": "https://envs.sh/Wv6.jpg"},
    {"name": "الكنز", "photo": "https://envs.sh/WND.jpg"},
    {"name": "جحيم في الماء", "photo": "https://envs.sh/WNd.jpg"},
    {"name": "الهروب", "photo": "https://envs.sh/WH1.jpg"},
    {"name": "اين العقل", "photo": "https://envs.sh/WHN.jpg"},
    {"name": "حب في الزنزانه", "photo": "https://envs.sh/Wge.jpg"},
    {"name": "بنتين من مصر", "photo": "https://envs.sh/Wg3.jpg"},
    {"name": "تراب الماس", "photo": "https://envs.sh/WgC.jpg"},
    {"name": "ساعه ونص", "photo": "https://envs.sh/Wg1.jpg"},
    {"name": "سواق الاتوبيس", "photo": "https://envs.sh/WgU.jpg"},
    {"name": "رسايل بحر", "photo": "https://envs.sh/Wgl.jpg"},
    {"name": "زاير الفجر", "photo": "https://envs.sh/Wgk.jpg"},
    {"name": "ضربه شمس", "photo": "https://envs.sh/Wg8.jpg"},
    {"name": "طيور الظلام", "photo": "https://envs.sh/Wgr.jpg"},
    {"name": "قلب امه", "photo": "https://envs.sh/Wgs.jpg"},
    {"name": "عسل اسود", "photo": "https://envs.sh/Wg9.jpg"},
    {"name": "ظرف طارق", "photo": "https://envs.sh/Wgv.jpg"},
    {"name": "في محطه مصر", "photo": "https://envs.sh/WgN.jpg"},
    {"name": "فتاه المصنع", "photo": "https://envs.sh/WgH.jpg"},
    {"name": "ميكرفون", "photo": "https://envs.sh/Wgg.jpg"},
    {"name": "يارب ولد", "photo": "https://envs.sh/Wgf.jpg"},
    {"name": "يارب ولد", "photo": "https://envs.sh/Wgf.jpg"},
    {"name": "ليل وقضبان", "photo": "https://envs.sh/WgM.jpg"},
    {"name": "نهر الخوف", "photo": "https://envs.sh/Wgy.jpg"},
    {"name": "مطب صناعي", "photo": "https://envs.sh/WgX.jpg"},
    {"name": "مافيا", "photo": "https://envs.sh/Wgx.jpg"},
    {"name": "جزيره الشيطان", "photo": "https://envs.sh/Wg-.jpg"},
    {"name": "زهايمر", "photo": "https://envs.sh/WfD.jpg"},
    {"name": "اذاعه حب", "photo": "https://envs.sh/WfQ.jpg"},
    {"name": "صرخه نمله", "photo": "https://envs.sh/Wfh.jpg"},
    {"name": "كف القمر", "photo": "https://envs.sh/Wfd.jpg"},
    {"name": "الخليه", "photo": "https://envs.sh/Wf2.jpg"},
    {"name": "قبضه الهلالي", "photo": "https://envs.sh/Wft.jpg"},
    {"name": "عيون الصقر", "photo": "https://envs.sh/Wfb.jpg"},
    {"name": "الارجواز", "photo": "https://envs.sh/WfP.jpg"},
    {"name": "الانس والجن", "photo": "https://envs.sh/Wfq.jpg"},
    {"name": "خمسه باب", "photo": "https://envs.sh/Wf0.jpg"},
    {"name": "ديل سمكه", "photo": "https://envs.sh/Wfc.jpg"},
    {"name": "المومياء", "photo": "https://envs.sh/WfL.jpg"},
    {"name": "الكيف", "photo": "https://envs.sh/WfG.jpg"},
    {"name": "كتكوت", "photo": "https://envs.sh/Wfz.jpg"},
    {"name": "الباشا تلميذ", "photo": "https://envs.sh/WfU.jpg"},
    {"name": "فيلم هندي", "photo": "https://envs.sh/Wfl.jpg"},
    {"name": "السفاح", "photo": "https://envs.sh/Wfr.jpg"}, 
    {"name": "السفاح", "photo": "https://envs.sh/Wfr.jpg"}, 
    {"name": "الحفيد", "photo": "https://envs.sh/WaW.jpg"}, 
    {"name": "الكرنك", "photo": "https://envs.sh/WaT.jpg"}, 
    {"name": "كباريه", "photo": "https://envs.sh/WaA.jpg"}, 
    {"name": "حبيبي نائما", "photo": "https://envs.sh/Wac.jpg"}, 
    {"name": "المجرم", "photo": "https://envs.sh/Wa3.jpg"}, 
    {"name": "ضغط عالي", "photo": "https://envs.sh/WaC.jpg"}, 
    {"name": "القرد بيتكلم", "photo": "https://envs.sh/Wa1.jpg"}, 
    {"name": "مولانا", "photo": "https://envs.sh/Wa4.jpg"}, 
    {"name": "الشموع السوداء", "photo": "https://envs.sh/Wal.jpg"}, 
    {"name": "اخر ديك في مصر", "photo": "https://envs.sh/Wa7.jpg"}, 
    {"name": "عصافير النيل", "photo": "https://envs.sh/WOk.jpg"}, 
    {"name": "كلاشنكوف", "photo": "https://envs.sh/WO8.jpg"}, 
    {"name": "الشياطين", "photo": "https://envs.sh/WO7.jpg"}, 
    {"name": "حبك نار", "photo": "https://envs.sh/WOJ.jpg"}, 
    {"name": "هروب مومياء", "photo": "https://envs.sh/WOo.jpg"}, 
    {"name": "معالي الوزير", "photo": "https://envs.sh/WOr.jpg"}, 
    {"name": "شجيع السيما", "photo": "https://envs.sh/WOs.jpg"}, 
    {"name": "عبود علي الحدود", "photo": "https://envs.sh/WO9.jpg"}, 
    {"name": "عيش الغرام", "photo": "https://envs.sh/WOv.jpg"}, 
    {"name": "المولد", "photo": "https://envs.sh/WON.jpg"}, 
    {"name": "العقرب", "photo": "https://envs.sh/WOH.jpg"}, 
    {"name": "أعدام الحب", "photo": "https://envs.sh/WOg.jpg"}, 
    {"name": "الوردة الحمراء", "photo": "https://envs.sh/WOM.jpg"}, 
    {"name": "الوردة الحمراء", "photo": "https://envs.sh/WOM.jpg"}, 
    {"name": "الساحر", "photo": "https://envs.sh/WOX.jpg"}, 
    {"name": "سحر العيون", "photo": "https://envs.sh/WOV.jpg"}, 
    {"name": "بركان الغضب", "photo": "https://envs.sh/WO-.jpg"}, 
    {"name": "أمير الظلام", "photo": "https://envs.sh/WmD.jpg"}, 
    {"name": "قلب الاسد", "photo": "https://envs.sh/WmE.jpg"}, 
    {"name": "الغسالة", "photo": "https://envs.sh/Wmh.jpg"}, 
    {"name": "عفريت مراتي", "photo": "https://envs.sh/Wmd.jpg"}, 
    {"name": "دم الغزال", "photo": "https://envs.sh/Wmi.jpg"}, 
    {"name": "البلياتشو", "photo": "https://envs.sh/WmW.jpg"}, 
    {"name": "الغواص", "photo": "https://envs.sh/WmT.jpg"}, 
    {"name": "أمير البحار", "photo": "https://envs.sh/Wmp.jpg"}, 
    {"name": "كابوريا", "photo": "https://envs.sh/WOt.jpg"}, 
    {"name": "غرام الأفاعي", "photo": "https://envs.sh/WOe.jpg"}, 
    {"name": "لص بغداد", "photo": "https://envs.sh/WOi.jpg"}, 
    {"name": "الناظر", "photo": "https://envs.sh/WOb.jpg"}, 
    {"name": "حرب أطاليا", "photo": "https://envs.sh/WOP.jpg"}, 
    {"name": "بشتري راجل", "photo": "https://envs.sh/WOw.jpg"}, 
    {"name": "عيون لا تنام", "photo": "https://envs.sh/WO0.jpg"}, 
    {"name": "الفندق", "photo": "https://envs.sh/WOW.jpg"}, 
    {"name": "اللص و الكلاب", "photo": "https://envs.sh/WOB.jpg"}, 
    {"name": "النظارة السوداء", "photo": "https://envs.sh/WOn.jpg"}, 
    {"name": "زوجتي و الكلب", "photo": "https://envs.sh/WOT.jpg"}, 
    {"name": "الزوجه الثانيه", "photo": "https://envs.sh/WOp.jpg"}, 
    {"name": "ابي فوق الشجره", "photo": "https://envs.sh/WOA.jpg"}, 
    {"name": "عروسه النيل", "photo": "https://envs.sh/WOj.jpg"}, 
    {"name": "غرام في الكرنك", "photo": "https://envs.sh/WOc.jpg"}, 
    {"name": "الفلوس", "photo": "https://envs.sh/WOZ.jpg"}, 
    {"name": "الوتر", "photo": "https://envs.sh/WOL.jpg"}, 
    {"name": "كلمني شكرا", "photo": "https://envs.sh/WO5.jpg"}, 
    {"name": "مجنون اميره", "photo": "https://envs.sh/WOG.jpg"}, 
    {"name": "عائله ميكي", "photo": "https://envs.sh/WOK.jpg"}, 
    {"name": "ياباني اصلي", "photo": "https://envs.sh/WOz.jpg"}, 
    {"name": "ابو شنب", "photo": "https://envs.sh/WO3.jpg"}, 
    {"name": "الهرم الرابع", "photo": "https://envs.sh/WOY.jpg"}, 
    {"name": "كنغر حبنا", "photo": "https://envs.sh/WOC.jpg"}, 
    {"name": "بنطلون جوليت", "photo": "https://envs.sh/WOR.jpg"}, 
    {"name": "جحيم تحت الماء", "photo": "https://envs.sh/WOy.jpg"}, 
    {"name": "سلام يا صاحبي", "photo": "https://envs.sh/WOS.jpg"}
]

@Client.on_message(filters.command(["افلام", "فيلم","• افلام •"], ""), group=76006953)
async def afalmme(client, message):
    actor = random.choice(so5raa5)
    bot_username = client.me.username
    user_id = message.from_user.id
    ces5ar5[user_id] = actor['name']
    ur5ers5[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الفيلم....؟ ")

@Client.on_message(filters.text & filters.group, group=7562065)
async def afa2lm6me(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in ur5ers5:
        correct_actor = ces5ar5.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del ces5ar5[user_id]
            del ur5ers5[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del ces5ar5[user_id]
                del ur5ers5[user_id]

uses1 = {}        
caear1 = {}        

questions = [
    {"photo": "ما هو عدد الكواكب في النظام الشمسي؟", "name": "8"},
    {"photo": "ما هو لون الشمس؟", "name": "أبيض"},
    {"photo": "اسمه من خمسة حروف اذا حذفت اوله بقا ثمان؟", "name": "عثمان"},
    {"photo": "ما الشئ الذي يمتلك أسنان ولا يمكنه العض؟", "name": "المشط"},
    {"photo": "شيء يتجمد إذا تم تسخينه؟", "name": "البيض"},
    {"photo": "يحملك إلى اي مكان اذا حذفت اوله اصبح عظيم الشأن واذا حذفت اخره اصبح غالي الأثمان واذا عكسته تقشعر منه الأبدان؟", "name": "درب"},
    {"photo": "نوع من أنواع الحيوانات يقوم بحك أذنه من خلال أنفه فما هو؟", "name": "الفيل"},
    {"photo": "من هو خال ابن عمتك؟", "name": "ابوك"},
    {"photo": "ما هو الشي الذي يعتبر غير نظيف اذا ابيض لونه؟", "name": "اللسان"},
    {"photo": "ماهو الشيء الذي تراه ولا يراك؟", "name": "الظل"},
    {"photo": "يطير مثل الطيور ولكنه لا يغادر مكانه؟", "name": "العلم"},
    {"photo": "ماهو الشيء الذي لايقطع إلا اذا ادخلت اصابعك في عينيه؟", "name": "المقص"},
    {"photo": "ما هو الشيء الذي يمر خلال الباب ولا يدخل؟", "name": "المفتاح"},
    {"photo": "بيت لا يوجد له أبواب ولا نوافذ فما هو؟", "name": "بيت الشعر"},
    {"photo": "ما هو الطائر الذي يستطيع تكرار كلام الإنسان بالتدريب؟", "name": "الببغاء"},
    {"photo": "اين يوجد البحر الذي بدون ماء؟", "name": "الخريطه"},
    {"photo": "لي رقبة وليس لدي رأس ولي ذراعين وليس لدي يدين ما هذا؟", "name": "القميص"},
    {"photo": "ما الشخص الي يبدو بسيط لكن يحني له الملك رأسه؟", "name": "الحلاق"},
    {"photo": "شيء اذا رايناه لا نركبه واذا ركبناه فلا نره فما هو؟", "name": "النعش"},
    {"photo": "اوله ثالث تفاحة واخر التفاح ثانيه ورابع العمر له ثالث واخر الورد باقيه؟", "name": "احمد"},
    {"photo": "من هو النبي الذي مات ولم يولد؟", "name": "ادم"},
    {"photo": "شيء من الممكن ان يكون له خيال من الامام او الخلف ومن الممكن يكون بداخله؟", "name": "الحفرة"},
    {"photo": "شيء يستطيع التحدث بكل لغات العالم؟", "name": "صدى الصوت"},
    {"photo": "لا يبتل حتى وإن دخل الماء؟", "name": "الضوء"},
    {"photo": "حيوان يمشي ويقف بالرغم من أنه ليس لديه أقدام؟", "name": "الثعبان"},
    {"photo": "نوع من انواع الطيور يتكون من حرفين واذا قلبت الكلمة صارت اسم مهنة؟", "name": "بط"},
    {"photo": "مدينة لا يطحن فيها الدقيق ولا يموت فيها الميت؟", "name": "كل المدن"},
    {"photo": "ما هو الشيء الذي يعبر البحر دون أن يتبلل غير العجل في بطن أمه؟", "name": "الطائره"},
    {"photo": "ماهو الشيء الذي يبكي اذا لففت راسه؟", "name": "الحنفيه"},
    {"photo": "انا لا املك حياة ولكنني اموت فما اكون؟", "name": "البطاريه"},
    {"photo": "ما هو الشيء الذي يطلبه الناس دائمًا وإذا جاء هربوا منه؟", "name": "المطر"},
    {"photo": "فاكهة اسمها على اسم طائر؟", "name": "الكيوي"},
    {"photo": "ما هو الجرح الذي لا ينزف دم في جسم الإنسان؟", "name": "جرح المشاعر"},
    {"photo": "يطلع من بطن امه ويحك ظهر ابوه ويموت فما هو؟", "name": "عود الكبريت"},
    {"photo": "ماهو الشيء الذي تأكل منه مع إنه لا يؤكل؟", "name": "الصحن"},
    {"photo": "ماهو الشيء الذي نرميه بعد العصر؟", "name": "البرتقال"},
    {"photo": "ما الاسم الذي إذا حذفت اوله صار اسمين؟", "name": "ياسمين"},
    {"photo": "ماهو الشيء الذي يقرصك ولا تراه؟", "name": "الجوع"},
    {"photo": "شيء موجود في الليل ثلاث مرات وفي النهار مرة واحدة؟", "name": "حرف اللام"},
    {"photo": "ما هو الطائر الذي يستطيع تكرار كلام الإنسان بالتدريب؟", "name": "حرف اللام"},
    {"photo": "كلما كان هناك المزيد قل ما تراه ما هذا؟", "name": "الضباب"},
    {"photo": "ماهو الشيء الذي يسير ولا يمتلك أقدام؟", "name": "الساعه"},
    {"photo": "يتم أخذها منك قبل أن تأخذها؟", "name": "الصوره"},
    {"photo": "ماهو الشيء الذي يوجد وسط باريس؟", "name": "حرف الراء"},
    {"photo": "هو اليف ولكن اذا صار بالأبيض والاسود صار متوحش فما يكون؟", "name": "الحمار"},
    {"photo": "شيء تسمعه ولكن لا يسمعك تراه ولكن لا يراك؟", "name": "التلفاز"},
    {"photo": "شئ قلبه ابيض ويرتدي قبعة خضراء لكن لونه اسود؟", "name": "الباذنجان"},
    {"photo": "ماهو الشيء الذي له اعين ثلاث بينما له قدم واحدة؟", "name": "اشارة المرور"},
    {"photo": "ما هو الحيوان الأبكم الذي لا يتكلم ولا نسمع له صوت؟", "name": "الزرافه"},
    {"photo": "شيء اذا لمسته يصرخ؟", "name": "الجرس"},
    {"photo": "انا املك كل المعلومات التي تعرفها وانا اصغر من قبضة يدك من اكون؟", "name": "العقل"},
    {"photo": "ما هو الشيء الذي درجة حرارته ثابته سواء وضعته في الثلاجه أو على النار؟", "name": "الفلفل"},
    {"photo": "ماهي الفاكهة الصلبة التي يوجد بداخلها حليب؟", "name": "جوز الهند"},
    {"photo": "تاجر من التجار إذا اقتلعنا عينه طار فمن هو؟", "name": "عطار"},
    {"photo": "ماهو الذي خلف الكلب اينما ذهب؟", "name": "ذيله"},
    {"photo": "بلد إسلامي اوله عبادة واخره نقود فما هو؟", "name": "الصومال"},
    {"photo": "ما هي الفاكهة التي تُجفف لتصبح زبيب؟", "name": "العنب"},
    {"photo": "شيء يغلبك دون ان يؤذيك؟", "name": "النوم"},
    {"photo": "ماهو الشيء الذي تشتريه لونه أسود ولكنك لاتستفيد منه إلا بعد أن يصبح لونه أحمر؟", "name": "الفحم"},
    {"photo": "طوله حوالي شبر ويحمل أطول من متر ماهو؟", "name": "الحذاء"},
    {"photo": "صغير الحجم لا تلقى له بال ولكن بوجهه تفتح الأبواب؟", "name": "المفتاح"},
    {"photo": "ماهما الميتتان التي يجوز اكلهما بدون اثم؟", "name": "السمك والجراد"},
    {"photo": "سيد وسيدة لديهما ست بنات وكل ابنة لها أخ واحد كم عدد أفراد العائلة؟", "name": "تسعه"},
    {"photo": "إذا كان سعيد على يمين سمير وجابر على يمين سعيد فمن يكون في الوسط؟", "name": "سعيد"},
    {"photo": "احمر وليس احمر اسود وليس اسود وابيض وليس ابيض ماهو؟", "name": "البحر"},
    {"photo": "ان ابتسمت لها ابتسمت لك ماهي؟", "name": "المراه"},
    {"photo": "ما هو أهون موجود و أعز مفقود؟", "name": "الماء"},
    {"photo": "الشيء الذي إذا ذبح بكى عليه الجميع؟", "name": "البصل"},
    {"photo": "من هو الشخص الذي يمشي على الأرض ولكنه يطول النجوم أيضًا؟", "name": "الظابط"},
    {"photo": "إنسان وزوجته لا هو من بني آدم ولا هي من بنات حواء من هما؟", "name": "ادم وحواء"},
    {"photo": "ما هو الشيء الذي يحمل طعامه فوق رأسه فإذا مشى أكل منه وإذا سكن غطى رأسه ونام؟", "name": "قلم الحبر"},
    {"photo": "ما هو الشيء الذي يحيا في أول الشهر ويموت في آخر الشهر؟", "name": "القمر"},
    {"photo": "ما الذي يمكنه أن يملأ الغرفة دون أن يشغل حيزا؟", "name": "النور"},
    {"photo": "طائر إذا قمت بقلب حروف اسمه رأيت عجب؟", "name": "بجع"},
    {"photo": "ينام بالحذاء ولا يخلعه؟", "name": "الحصان"},
    {"photo": "ما هي الكلمة الوحيدة التي تلفظ غلط دائمًا؟", "name": "غلط"},
    {"photo": "لا يبتل حتى وإن دخل الماء؟", "name": "الضوء"},
    {"photo": "اسم حيوان اذا قمت بتغيير اول حرف منه اصبح اهم عضو في جسم الإنسان؟", "name": "قلب"},
    {"photo": "ماهو الشئ الموجود في كل شيء؟", "name": "الاسم"},
    {"photo": "امرأة عقيم هل تنجب ابنتها أطفال؟", "name": "العقيم لا تلد"},
    {"photo": "ما هو الشئ الذي يمكن كسره دون ان نلمسه؟", "name": "الوعد"},
    {"photo": "قلعة خضراء وأرضها حمراء وسكانها لونهم أسود فما هي؟", "name": "البطيخه"},
    {"photo": "ماهو الذي خلف الكلب اينما ذهب؟", "name": "ذيله"},
    {"photo": "ماهي الدولة التي حارب اهلها الذباب والعصافير لخطورتها؟", "name": "الصين"},
    {"photo": "ما هي اسم الفاكهة التي سُميت بإحدى سور القرآن الكريم باسمها؟", "name": "التين"},
    {"photo": "شيء كلما كان موجود كلما قل ماتراه؟", "name": "الظلام"},
    {"photo": "عقرب لا يلدغ ولا يسبب الذعر لأي أحد حتى الأطفال؟", "name": "عقرب الساعه"},
    {"photo": "فاكهة بها حبات اللؤلؤ؟", "name": "الرمان"},
    {"photo": "شيء موجود في الدقيقة مرتين ولا يوجد في الساعة؟", "name": "حرف القاف"},
    {"photo": "مدينة سعودية اسمها على اسم نبات فما هي؟", "name": "عرعر"},
    {"photo": "ماهو الشيء الذي كلما عرضته للشمس ازداد بللا؟", "name": "الثلج"},
    {"photo": "ما هو الشيء الذى كلما خطا خطوه فقد شيئًا من ذيله؟", "name": "ابره الخياطه"},
    {"photo": "ماهو الشيء الذي يتحرك بدون أرجل ويبكي بدون عيون؟", "name": "السحاب"},
    {"photo": "ما هو الشيء الذي بإمكانك تحقيقه دون بذل عناء؟", "name": "الفشل"},
    {"photo": "شيء اذا اطعمناه لا يشبع واذا سقيناه يموت؟", "name": "النار"},
    {"photo": "شيء ليس له بداية ولا نهاية ما هو هذا الشيء؟", "name": "الدائره"},
    {"photo": "طائر يلد ولايبيض فما هو؟", "name": "الخفاش"},
    {"photo": "شيء في السماء وليس في الماء فما هو؟", "name": "حرف السين"},
    {"photo": "شيء تملكه انت ولكن يستخدمه الآخرون اكثر منك؟", "name": "الاسم"},
    {"photo": "جزء من الجنة يعيش معنا في الأرض ما هو؟", "name": "الحجر الاسود"},
    {"photo": "يمتلك بحيرات بلا ماء وأراضي بلا زرع وجبال بلا أحجار؟", "name": "الخريطه"},
    {"photo": "اي كلمة تصبح اقصر اذا اضفت لها حرف؟", "name": "قصر"},
    {"photo": "ما هي درجة القرابة طفل من والده الحقيقي لكن هذا الطفل ليس ابنه؟", "name": "ابنته"},
    {"photo": "ماهو الشجر الذي يسميه الناس قاتل ابيه؟", "name": "الموز"},
    {"photo": "شيء يمكن قياسه لكن لايمكن رؤيته؟", "name": "الوقت"},
    {"photo": "ماهو الشيء الذي ينام ولا يقوم؟", "name": "الرماد"},
    {"photo": "شيء يمشي أمامك ولا تستطيع رؤيته؟", "name": "المستقبل"},
    {"photo": "شهر هجري اذا حذفت وسطه يتحول الي فاكهة؟", "name": "رمضان"}, 
    {"photo": "هو شيء يكون لونه أخضر في الأرض وأسود في الأسواق وأحمر في الأكواب، فما هو؟", "name": "الشاي"},
    {"photo": "يمكنه رفع الأثقال، لكنه لا يستطيع أن يمسك مسمار", "name": "البحر"},
    {"photo": "يقول الحقيقة ويكذب عندما يكون جائعا", "name": "الساعه"} 
]

@Client.on_message(filters.command(["لغز", "فزوره","• لغز •"], ""), group=6456565)
async def fazoraa(client, message):
    actor = random.choice(questions)
    bot_username = client.me.username
    user_id = message.from_user.id
    caear1[user_id] = actor['name']
    uses1[user_id] = user_id
    await message.reply_text(actor['photo'])

@Client.on_message(filters.text & filters.group, group=5013245)
async def logzee(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in uses1:
        correct_actor = caear1.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del caear1[user_id]
            del uses1[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del caear1[user_id]
                del uses1[user_id]
                
uss2 = {}        
cear2 = {}        

qustions = [
    {"photo": "🏨🏨🏨🏨🏨🏣🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨", "name": "🏣"},
    {"photo": "❤️❤️❤️❤️❤️❤️❤️❤️❤️♥️❤️❤️❤️❤️❤️❤️", "name": "♥️"},
    {"photo": "↗️↗️↗️↗️↗️↗️↗️↗️↗️⬆️↗️↗️↗️↗️↗️↗️↗️↗️↗️↗️", "name": "⬆️"},
    {"photo": "🍅🍅🍅🍅🍅🍅🍎🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅", "name": "🍎"},
    {"photo": "📫📫📫📫📫📫📫📪📫📫📫📫📫📫📫📫📫📫📫📫", "name": "📪"},
    {"photo": "🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇬🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫", "name": "🇳🇬"},
    {"photo": "💗💗💗💗💗💗💗💗💗🩷💗💗💗💗💗💗💗", "name": "🩷"},
    {"photo": "🔂🔂🔂🔂🔂🔂🔂🔁🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂", "name": "🔁"},
    {"photo": "😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰??😰😰😰😰😰😰😰😰😰😰", "name": "😨"},
    {"photo": "📥📥📥📤📥📥📥📥📥📥📥📥📥📥📥📥", "name": "📤"},
    {"photo": "🦡🦡🦡🦡🦝🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡", "name": "🦝"},
    {"photo": "👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂", "name": "👮"},
    {"photo": "🔼🔼🔼🔼🔼🔼🔽🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼", "name": "🔽"},
    {"photo": "👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕🧑‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕", "name": "🧑‍⚕"},
    {"photo": "💓💓💓💓💓💓💗💓💓💓💓💓💓💓💓💓💓💓💓", "name": "💗"},
    {"photo": "🚞🚞🚞🚞🚞🚃🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞", "name": "🚃"},
    {"photo": "😫😫😫😫😫😫😩😫😫😫😫😫😫😫😫😫😫😫😫😫😫", "name": "😩"},
    {"photo": "🧚‍♂🧚🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂", "name": "🧚"},
    {"photo": "😥😥😥😥😥😥😥😢😥😥😥😥😥😥😥😥😥😥😥😥😥", "name": "😢"},
    {"photo": "⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⏳⌛️⌛️⌛️", "name": "⏳"},
    {"photo": "🦌🦌🦌🦌🦌🦌🦌🐂🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌", "name": "🐂"},
    {"photo": "🌇🌇🌇🌇🌇🌆🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇", "name": "🌆"},
    {"photo": "🌗🌗🌗🌗🌗🌗🌓🌗🌗🌗🌗🌗🌗🌗🌗🌗", "name": "🌓"},
    {"photo": "🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🫢🤭🤭🤭🤭🤭🤭", "name": "🫢"},
    {"photo": "◼️◼️◼️🔳◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️", "name": "🔳"},
    {"photo": "🐓🐓🐓🐓🐓🪿🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓", "name": "🪿"},
    {"photo": "🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂", "name": "🧖"},
    {"photo": "🛠🛠🛠🛠🛠⚒🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠", "name": "⚒"},
    {"photo": "🕖🕖🕖🕖🕖🕖🕦🕖🕖🕖🕖🕖🕖🕖🕖🕖🕖", "name": "🕦"},
    {"photo": "😏😏😏😏😏😏😒😏😏😏😏😏😏😏😏😏😏😏", "name": "😒"},
    {"photo": "😮😮😮😮😮😮😮😦😮😮😮😮😮😮😮😮😮😮😮😮😮😮😮", "name": "😦"},
    {"photo": "🛬🛬🛬🛬🛫🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬", "name": "🛫"},
    {"photo": "🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂😶🙂🙂", "name": "😶"},
    {"photo": "🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙊🙉🙉", "name": "🙊"},
    {"photo": "🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇸🇩🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸", "name": "🇸🇩"},
    {"photo": "🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇹🇩🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪", "name": "🇹🇩"},
    {"photo": "🎥🎥🎥🎥🎥🎥🎥🎥🎥📹🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥", "name": "📹"},
    {"photo": "🖊🖊🖊🖊🖊🖋🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊", "name": "🖋"},
    {"photo": "🛌🛌🛌🛏🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌", "name": "🛌"},
    {"photo": "🔒🔒🔒🔒🔒🔒🔒🔓🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒", "name": "🔓"},
    {"photo": "👨‍💻👨‍💻👨‍💻👨‍💻🧑‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻", "name": "👨‍💻"},
    {"photo": "📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📄📑📑📑📑📑📑📑📑", "name": "📄"},
    {"photo": "🦻🦻🦻🦻🦻🦻👂🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻", "name": "👂"},
    {"photo": "⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈🌨⛈⛈⛈⛈", "name": "🌨"},
    {"photo": "😚😚😚😚😚☺️😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚", "name": "☺️"},
    {"photo": "🦏🦏🦏🦏🦏🦏🦏🦏🦏🐘🦏🦏🦏🦏🦏🦏🦏🦏🦏🦏", "name": "🐘"},
    {"photo": "💿💿💿💿💿💿💿💿📀💿💿💿💿💿💿💿", "name": "📀"},
    {"photo": "😐😐😐😐😐😐😑😐😐😐😐😐😐😐😐😐😐😐😐😐😐", "name": "😑"},
    {"photo": "❤️❤️❤️❤️❤️❤️❤️❤️❤️♥️❤️❤️❤️❤️❤️❤️", "name": "♥️"},
    {"photo": "🩶🩶🩶🩶🩶🩶🩶🩶🤍🩶🩶🩶🩶🩶🩶🩶🩶", "name": "🤍"},
    {"photo": "🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♀🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂", "name": "🏋‍♀"},
    {"photo": "🇪🇬🇪🇬🇪🇬🇪🇬🇾🇪🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬", "name": "🇾🇪"},
    {"photo": "📸📸📸📸📸📸📸📷📸📸📸📸📸📸📸📸📸📸📸📸📸📸📸📸", "name": "📷"},
    {"photo": "📲📲📲📲📲📲📲📲📲📲📲📲📲📲📲📲📱📲📲📲📲📲📲📲📲📲", "name": "📱"},
    {"photo": "🔆🔆🔆🔆🔆🔅🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆", "name": "🔅"},
    {"photo": "🏬🏬🏬🏬🏬🏬🏬🏬🏢🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬", "name": "🏢"},
    {"photo": "🥋🥋🥋🥋🥋🥋🥋🥼🥋🥋🥋🥋🥋🥋🥋🥋🥋🥋🥋", "name": "🥼"},
    {"photo": "🦌🦌🦌🦌🦌🦌🦌🐂🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌", "name": "🐂"},
    {"photo": "😧😧😧😧😧😧😧😧😧😧😯😧😧😧😧😧😧😧😧😧😧😧", "name": "😯"},
    {"photo": "🍽🍽🍽🍽??🍽🍽🍽🍽🍴🍽🍽🍽🍽🍽🍽🍽🍽🍽🍽", "name": "🍴"},
    {"photo": "📆📆📆📆📆📅📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆", "name": "📅"},
    {"photo": "🍀🍀🍀🍀🍀🍀🍀🍀☘🍀🍀🍀🍀🍀🍀🍀", "name": "☘"},
    {"photo": "🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚅🚄🚄🚄🚄🚄🚄🚄", "name": "🚅"},
    {"photo": "👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨", "name": "👨‍❤️‍👨"},
    {"photo": "🌍🌍🌍🌍🌍🌏🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍", "name": "🌏"},
    {"photo": "🤹‍♀🤹‍♀🤹‍♀🤹🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀", "name": "🤹"},
    {"photo": "🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔉🔈🔈🔈🔈🔈", "name": "🔉"},
    {"photo": "⛰⛰⛰⛰⛰⛰🏔⛰⛰⛰⛰⛰⛰⛰⛰⛰", "name": "🏔"},
    {"photo": "😸😸😸😺😸😸😸😸😸😸😸😸😸😸😸😸😸", "name": "😺"},
    {"photo": "👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯🚶‍♀👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯", "name": "🚶‍♀"},
    {"photo": "❓❓❓❓❔❓❓❓❓❓❓❓❓❓❓❓❓", "name": "❔"},
    {"photo": "🔕🔕🔕🔕🔕🔕🔕🔕🔕🔔🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕", "name": "🔔"},
    {"photo": "🖐🖐🖐🖖🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐", "name": "🖖"},
    {"photo": "☃️☃️☃️☃️☃️☃️☃️⛄️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️", "name": "⛄️"},
    {"photo": "😌😌😌😌😌😌😌😌😌😌☺️😌😌😌😌😌", "name": "☺️"},
    {"photo": "👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍??👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨", "name": "👨‍❤️‍👨"},
    {"photo": "🧥🧥🧥🧥🧥🧥🧥🧥🧥🧥🧥🥼🧥🧥🧥🧥🧥🧥🧥🧥", "name": "🥼"},
    {"photo": "⏯⏯⏯⏯⏯⏸⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯", "name": "⏸"},
    {"photo": "😚😚😚😚😚☺️😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚", "name": "☺️"},
    {"photo": "🔨🔨🔨🔨⛏🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨", "name": "⛏"},
    {"photo": "📂📂📂📂📂📂📁📂📂📂📂📂📂📂📂📂", "name": "📁"},
    {"photo": "🦀🦀🦀🦀🦀🦀🦀🦞🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀", "name": "🦞"},
    {"photo": "👿👿👿👿👿😈👿👿👿👿👿👿👿👿👿👿👿👿👿👿👿", "name": "😈"},
    {"photo": "🔳🔳🔳🔳🔳🔳🔳🔳🔳◼️🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳", "name": "◼️"},
    {"photo": "🐼🐼🐼🐼🐼🐼🐼🐻‍❄️🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼", "name": "🐻‍❄️"},
    {"photo": "🔎🔎🔎🔎🔎🔎🔎🔎🔎🔍🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎", "name": "🔍"},
    {"photo": "🤼‍♂🤼🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂", "name": "🤼"},
    {"photo": "👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀🧑‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀", "name": "🧑‍🚀"}
]

@Client.on_message(filters.command(["مختلف", "اختلاف","الاختلاف","• مختلف •"], ""), group=6565065)
async def moktlf(client, message):
    actor = random.choice(qustions)
    bot_username = client.me.username
    user_id = message.from_user.id
    cear2[user_id] = actor['name']
    uss2[user_id] = user_id
    await message.reply_text(actor['photo'])

@Client.on_message(filters.text & filters.group, group=5012465)
async def alatlaf(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in uss2:
        correct_actor = cear2.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del cear2[user_id]
            del uss2[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del cear2[user_id]
                del uss2[user_id]
            
            
@Client.on_message(filters.command("نقاطي", ""), group=908070)
async def check_points(client, message):
    user_id = message.from_user.id
    if user_id in points:
        point = points.get(user_id)
        await message.reply_text(f"لديك {point} نقطة.")
    else:
        await message.reply_text("معكش نقاط اصلا")

@Client.on_message(filters.command("توب النقاط", ""), group=918171)
async def top_points(client, message):
    user_id = message.from_user.id	
    sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)   
    k = 0
    text = "اكثر الاشخاص الي معاها نقاط:\n\n"    
    for user_id, point in sorted_points:
        user = await client.get_users(user_id)
        k += 1
        text += f"{k}: {user.mention} : {point}\n"
        if k >= 5:
            break
    await message.reply_text(text)
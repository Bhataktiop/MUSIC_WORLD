import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/489701c1943b78779a0d8.jpg",
        caption=f"""**ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★[𝐜𝐫𝐞𝐚𝐭𝐞𝐫](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " [𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭] ", url=f"https://t.me/+6-3fF5htmh1iZmU1")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "hi", "ZINDA_H_TU_MERE_LIYE_HEART_HACK"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/489701c1943b78779a0d8.jpg",
        caption=f"""HELLO 🤗""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " [𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭] ", url=f"https://t.me/vampair_diaries2134")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/489701c1943b78779a0d8.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " [𝙍𝙚𝙥𝙤𝙨𝙞𝙩𝙤𝙧𝙮] ", url=f"https://t.me/vampair_diaries2134")
                ]
            ]
        ),
    )

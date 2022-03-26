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
        photo=f"https://te.legra.ph/file/ea0a49d9aed8ed552b83f.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ɴᴏʙɪᴛᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [KULDIP RATHOD](https://t.me/AAPLI_YAARI)
┣★ ᴜᴘᴅᴀᴛᴇs : [NOBITA SUPPORT](https://t.me/NOBITA_SPAMMER_OP)
┣★ sᴜᴘᴘᴏʀᴛ : [NOBITA CHAT](https://t.me/AAPLI_YAARI)
┣★ ᴏᴡɴᴇʀ › : [NOBITA_XD](https://t.me/Nobi_xxd)
┗━━━━━━━━━━━━━━━━━┛

😈 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/Nobi_xxd) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/AAPLI_YAARI")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "NOBITA"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ea0a49d9aed8ed552b83f.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❤️ 𝙹𝙾𝙸𝙽 𝙷𝙴𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ", url=f"https://t.me/AAPLI_YAARI")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ea0a49d9aed8ed552b83f.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝙴𝚃 𝚁𝙴𝙿𝙾 𝚃𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 ", url=f"https://t.me/Nobi_xxd")
                ]
            ]
        ),
    )

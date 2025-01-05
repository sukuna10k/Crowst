# crédit @codeflix_bots (telegram)

import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("ᴘᴀᴛɪᴇɴᴛᴇᴢ, ꜱ'ɪʟ ᴠᴏᴜꜱ ᴘʟᴀîᴛ...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("QᴜᴇʟQᴜᴇ ᴄʜᴏꜱᴇ ᴀ ᴍᴀʟ ᴛᴏᴜʀɴé..!")
            return
        await temp_msg.delete()

        for msg in messages:
            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption="" if not msg.caption else msg.caption.html, filename=msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡️ À ᴘʀᴏᴘᴏꜱ", callback_data="about"),
                    InlineKeyboardButton('🍁 SériesFlix', url='https://t.me/AnTiflix_A')
                ]
            ]
        )
        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )
        return

#=====================================================================================##

WAIT_MSG = """"<b>ᴛʀᴀɪᴛᴇᴍᴇɴᴛ ᴇɴ ᴄᴏᴜʀꜱ...</b>"""

REPLY_ERROR = """<code>ᴜᴛɪʟɪꜱᴇᴢ ᴄᴇᴛᴛᴇ ᴄᴏᴍᴍᴀɴᴅᴇ ᴇɴ ʀéᴘᴏɴꜱᴇ à ᴛᴏᴜᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴇʟᴇɢʀᴀᴍ ꜱᴀɴꜱ ᴇꜱᴘᴀᴄᴇꜱ.</code>"""

#=====================================================================================##

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(text="• ʀᴇᴊᴏɪɴᴅʀᴇ ʟᴇ ᴄᴀɴᴀʟ", url=client.invitelink),
            InlineKeyboardButton(text="ʀᴇᴊᴏɪɴᴅʀᴇ ʟᴇ ᴄᴀɴᴀʟ •", url=client.invitelink2),
        ],
        [
            InlineKeyboardButton(text="• ʀᴇᴊᴏɪɴᴅʀᴇ ʟᴇ ᴄᴀɴᴀʟ", url=client.invitelink3),
            InlineKeyboardButton(text="ʀᴇᴊᴏɪɴᴅʀᴇ ʟᴇ ᴄᴀɴᴀʟ •", url=client.invitelink4),
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text='• ᴄʟɪQᴜᴇᴢ ɪᴄɪ ᴍᴀɪɴᴛᴇɴᴀɴᴛ •',
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=None if not message.from_user.username else '@' + message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀꜱ ᴜᴛɪʟɪꜱᴇɴᴛ ᴄᴇ ʙᴏᴛ")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>ᴅɪꜰꜰᴜꜱɪᴏɴ ᴅᴜ ᴍᴇꜱꜱᴀɢᴇ.. ᴄᴇʟᴀ ᴘʀᴇɴᴅʀᴀ ᴅᴜ ᴛᴇᴍᴘꜱ</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>ᴅɪꜰꜰᴜꜱɪᴏɴ ᴛᴇʀᴍɪɴéᴇ</u>

ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀꜱ ᴛᴏᴛᴀᴜx: <code>{total}</code>
ꜱᴜᴄᴄèꜱ: <code>{successful}</code>
ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀꜱ ʙʟᴏQᴜéꜱ:<code>{blocked}</code>
ᴄᴏᴍᴘᴛᴇꜱ ꜱᴜᴘᴘʀɪᴍéꜱ: <code>{deleted}</code>
Éᴄʜᴇᴄꜱ:<code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

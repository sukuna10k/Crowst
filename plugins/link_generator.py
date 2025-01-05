# crédit @codeflix_bots (telegram)

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text="ᴛʀᴀɴꜱꜰéʀᴇᴢ ʟᴇ ᴘʀᴇᴍɪᴇʀ ᴍᴇꜱꜱᴀɢᴇ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ (ᴀᴠᴇᴄ ᴅᴇꜱ ᴄɪᴛᴀᴛɪᴏɴꜱ)..\n\nᴏᴜ ᴇɴᴠᴏʏᴇᴢ ʟᴇ ʟɪᴇɴ ᴅᴜ ᴍᴇꜱꜱᴀɢᴇ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ ᴇʀʀᴇᴜʀ\n\nᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ᴛʀᴀɴꜱꜰéʀé ɴᴇ ᴘʀᴏᴠɪᴇɴᴛ ᴘᴀꜱ ᴅᴇ ᴍᴏɴ ᴄᴀɴᴀʟ ᴅʙ ᴏᴜ ᴄᴇ ʟɪᴇɴ ᴇꜱᴛ ᴘʀɪꜱ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ", quote=True)
            continue

    while True:
        try:
            second_message = await client.ask(text="ᴛʀᴀɴꜱꜰéʀᴇᴢ ʟᴇ ᴅᴇʀɴɪᴇʀ ᴍᴇꜱꜱᴀɢᴇ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ (ᴀᴠᴇᴄ ᴅᴇꜱ ᴄɪᴛᴀᴛɪᴏɴꜱ)..\nᴏᴜ ᴇɴᴠᴏʏᴇᴢ ʟᴇ ʟɪᴇɴ ᴅᴜ ᴍᴇꜱꜱᴀɢᴇ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ ᴇʀʀᴇᴜʀ\n\nᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ᴛʀᴀɴꜱꜰéʀé ɴᴇ ᴘʀᴏᴠɪᴇɴᴛ ᴘᴀꜱ ᴅᴇ ᴍᴏɴ ᴄᴀɴᴀʟ ᴅʙ ᴏᴜ ᴄᴇ ʟɪᴇɴ ᴇꜱᴛ ᴘʀɪꜱ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ", quote=True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 ᴘᴀʀᴛᴀɢᴇʀ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>ᴠᴏɪᴄɪ ᴠᴏᴛʀᴇ ʟɪᴇɴ</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text="ᴛʀᴀɴꜱꜰéʀᴇᴢ ʟᴇ ᴍᴇꜱꜱᴀɢᴇ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ (ᴀᴠᴇᴄ ᴅᴇꜱ ᴄɪᴛᴀᴛɪᴏɴꜱ)..\nᴏᴜ ᴇɴᴠᴏʏᴇᴢ ʟᴇ ʟɪᴇɴ ᴅᴜ ᴍᴇꜱꜱᴀɢᴇ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ ᴇʀʀᴇᴜʀ\n\nᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ᴛʀᴀɴꜱꜰéʀé ɴᴇ ᴘʀᴏᴠɪᴇɴᴛ ᴘᴀꜱ ᴅᴇ ᴍᴏɴ ᴄᴀɴᴀʟ ᴅʙ ᴏᴜ ᴄᴇ ʟɪᴇɴ ɴ'ᴇꜱᴛ ᴘᴀꜱ ᴘʀɪꜱ ᴅᴜ ᴄᴀɴᴀʟ ᴅʙ", quote=True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 ᴘᴀʀᴛᴀɢᴇʀ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>ᴠᴏɪᴄɪ ᴠᴏᴛʀᴇ ʟɪᴇɴ</b>\n\n{link}", quote=True, reply_markup=reply_markup)

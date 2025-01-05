# crédit @codeflix_bots (telegram)

"""Obtenez l'ID de l'utilisateur répondu
Syntaxe : /id"""

from pyrogram import filters, enums
from pyrogram.types import Message

from bot import Bot


@Bot.on_message(filters.command("id") & filters.private)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        await message.reply_text(
            f"<b>ᴠᴏᴛʀᴇ ɪᴅ ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ ᴇꜱᴛ :</b> <code>{user_id}</code>", quote=True
        )


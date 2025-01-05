#(©)Codexbotz

from aiohttp import web
from plugins import web_server

# import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL_1:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL_1)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL_1)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_1)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Le bot ne peut pas exporter le lien d'invitation du canal de souscription forcée !")
                self.LOGGER(__name__).warning(f"Veuillez vérifier la valeur de FORCE_SUB_CHANNEL_1 et assurez-vous que le bot est administrateur dans le canal avec la permission d'inviter des utilisateurs via un lien. Valeur actuelle du canal de souscription forcée : {FORCE_SUB_CHANNEL_1}")
                self.LOGGER(__name__).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir du support")
                sys.exit()

        if FORCE_SUB_CHANNEL_2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL_2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL_2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Le bot ne peut pas exporter le lien d'invitation du canal de souscription forcée !")
                self.LOGGER(__name__).warning(f"Veuillez vérifier la valeur de FORCE_SUB_CHANNEL_2 et assurez-vous que le bot est administrateur dans le canal avec la permission d'inviter des utilisateurs via un lien. Valeur actuelle du canal de souscription forcée : {FORCE_SUB_CHANNEL_2}")
                self.LOGGER(__name__).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir du support")
                sys.exit()
        if FORCE_SUB_CHANNEL_3:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL_3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL_3)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_3)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Le bot ne peut pas exporter le lien d'invitation du canal de souscription forcée !")
                self.LOGGER(__name__).warning(f"Veuillez vérifier la valeur de FORCE_SUB_CHANNEL_3 et assurez-vous que le bot est administrateur dans le canal avec la permission d'inviter des utilisateurs via un lien. Valeur actuelle du canal de souscription forcée : {FORCE_SUB_CHANNEL_3}")
                self.LOGGER(__name__).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir du support")
                sys.exit()
        if FORCE_SUB_CHANNEL_4:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL_4)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL_4)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_4)).invite_link
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Le bot ne peut pas exporter le lien d'invitation du canal de souscription forcée !")
                self.LOGGER(__name__).warning(f"Veuillez vérifier la valeur de FORCE_SUB_CHANNEL_4 et assurez-vous que le bot est administrateur dans le canal avec la permission d'inviter des utilisateurs via un lien. Valeur actuelle du canal de souscription forcée : {FORCE_SUB_CHANNEL_4}")
                self.LOGGER(__name__).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir du support")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Message de Test")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Assurez-vous que le bot est administrateur dans le canal de base de données et vérifiez la valeur de CHANNEL_ID. Valeur actuelle : {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir du support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot en cours d'exécution..!\n\nCréé par \nhttps://t.me/codeflix_bots")
        self.LOGGER(__name__).info(f"""       


  ___ ___  ___  ___ ___ _    _____  _____  ___ _____ ___ 
 / __/ _ \|   \| __| __| |  |_ _\ \/ / _ )/ _ \_   _/ __|
| (_| (_) | |) | _|| _|| |__ | | >  <| _ \ (_) || | \__ \
 \___\___/|___/|___|_| |____|___/_/\_\___/\___/ |_| |___/
                                                         
 
                                          """)
        self.username = usr_bot_me.username
        # web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot arrêté.")

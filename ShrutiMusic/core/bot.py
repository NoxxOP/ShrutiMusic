import pyrogram
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
from ..logging import LOGGER


class Nand(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting bot...")
        super().__init__(
            name="ShrutiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.username = self.me.username
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        if not config.LOG_GROUP_ID:
            LOGGER(__name__).warning("LOG_GROUP_ID is not set")
            LOGGER(__name__).info(f"Music Bot Started as {self.name}")
            return

        caption = (
            f"<b>🎵 Bot Started Successfully</b>\n\n"
            f"<b>Name:</b> {self.name}\n"
            f"<b>Username:</b> @{self.username}\n"
            f"<b>ID:</b> <code>{self.id}</code>\n\n"
            f"<i>Bot is now online and ready to serve!</i>"
        )
        button = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="Add Me To Your Group",
                url=f"https://t.me/{self.username}?startgroup=true",
            )
        ]])

        try:
            await self.send_message(config.LOG_GROUP_ID, caption, reply_markup=button)
        except Exception as e:
            LOGGER(__name__).error(f"Failed to send to log group: {e}")

        try:
            member = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
        except Exception as e:
            LOGGER(__name__).error(f"Error checking bot status: {e}")

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()

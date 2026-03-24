import pyrogram
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ..logging import LOGGER


class Nand(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting bot...")
        super().__init__(
            name="⏤ 𝐅 𝐋 𝐎 𝐑 𝐀 𝚇 𝐌 𝚄 𝚂 𝐈 𝐂 𝂈̽ ᰼ 🌷",
            api_id=config.32426469,
            api_hash=config.6cc009055eb3c64d5b50d6cea35ebee8,
            bot_token=config.7981788706:AAEhfm_Ies2U8kvFbjj86fU7iYZSR-4F9E4,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Add Me Baby Your Group",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ]
            ]
        )

        if config.LOG_GROUP_ID:
            try:
                await self.send_photo(
                    config.LOG_GROUP_ID,
                    photo=config.START_IMG_URL,
                    caption=f"<b>🎵 Bot Started Successfully</b>\n\n"
                            f"<b>Name:</b> {self.name}\n"
                            f"<b>Username:</b> @{self.username}\n"
                            f"<b>ID:</b> <code>{self.id}</code>\n\n"
                            f"<i>Bot is now online and ready to serve!</i>",
                    reply_markup=button,
                )
            except pyrogram.errors.ChatWriteForbidden:
                LOGGER(__name__).error("Bot cannot write to the log group")
                try:
                    await self.send_message(
                        config.LOG_GROUP_ID,
                        f"<b>🎵 Bot Started Successfully</b>\n\n"
                        f"<b>Name:</b> {self.name}\n"
                        f"<b>Username:</b> @{self.username}\n"
                        f"<b>ID:</b> <code>{self.id}</code>\n\n"
                        f"<i>Bot is now online and ready to serve!</i>",
                        reply_markup=button,
                    )
                except Exception as e:
                    LOGGER(__name__).error(f"Failed to send message in log group: {e}")
            except Exception as e:
                LOGGER(__name__).error(f"Error while sending to log group: {e}")
        else:
            LOGGER(__name__).warning("LOG_GROUP_ID is not set")

        if config.LOG_GROUP_ID:
            try:
                chat_member_info = await self.get_chat_member(
                    config.LOG_GROUP_ID, self.id
                )
                if chat_member_info.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            except Exception as e:
                LOGGER(__name__).error(f"Error checking bot status: {e}")

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()

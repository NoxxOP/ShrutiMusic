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

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from ShrutiMusic import YouTube, app
from ShrutiMusic.core.call import Nand
from ShrutiMusic.misc import SUDOERS, db
from ShrutiMusic.utils.database import (
    get_active_chats,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_music_playing,
    is_nonadmin_chat,
    music_off,
    music_on,
    set_loop,
)
from ShrutiMusic.utils.decorators.language import languageCB
from ShrutiMusic.utils.formatters import seconds_to_min
from ShrutiMusic.utils.inline import close_markup, stream_markup, stream_markup_timer
from ShrutiMusic.utils.inline.help import help_pannel_page1, help_pannel_page2, help_pannel_page3, help_pannel_page4
from ShrutiMusic.utils.stream.autoclear import auto_clean
from ShrutiMusic.utils.thumbnails import gen_thumb
from config import (
    BANNED_USERS,
    SOUNCLOUD_IMG_URL,
    STREAM_IMG_URL,
    TELEGRAM_AUDIO_URL,
    TELEGRAM_VIDEO_URL,
    adminlist,
    confirmer,
    votemode,
)
from strings import get_string
import config

checker = {}
upvoters = {}

from config import SUPPORT_GROUP
@app.on_callback_query(filters.regex("help_page_1"))
async def show_help_page1(client, callback_query: CallbackQuery):
    try:
        language = await get_lang(callback_query.message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")

    await callback_query.message.edit_caption(
        caption=_["help_1"].format(SUPPORT_GROUP),
        reply_markup=help_pannel_page1(_, START=True)
    )

@app.on_callback_query(filters.regex("fork_repo"))
async def fork_repo_callback(client, query):
    await query.message.edit_text(
        text=(
            "✨ <b>ʙᴜɪʟᴅ Yᴏᴜʀ Oᴡɴ ᴍᴜsɪᴄ ʙᴏᴛ 🎧</b>\n\n"
            "🚀 ʀᴇᴀᴅʏ ᴛᴏ ʟᴀᴜɴᴄʜ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ?\n"
            "ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ ᴀɴᴅ ᴅᴇᴘʟᴏʏ ɪɴ sᴇᴄᴏɴᴅs.\n\n"
            "🔧 <b>Cᴜsᴛᴏᴍɪᴢᴇ ɪᴛ. Dᴇᴘʟᴏʏ ɪᴛ. Vɪʙᴇ ᴡɪᴛʜ ɪᴛ 🔥</b>"
        ),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝑲𝒏𝒐𝒘𝒍𝒆𝒅𝒈𝒆", url="https://t.me/vip_king1999"),
                    InlineKeyboardButton("𝑴𝒖𝒔𝒊𝒄  𝑮𝒓𝒐𝒖𝒑�", url="https://t.me/+rQWL_3kN_ZQ5NTE1")
                ],
                [
                    InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="settingsback_helper")
                ]
            ]
        )
    )


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

from ShrutiMusic.utils.inline.start import about_panel
from strings import get_string
from config import BANNED_USERS


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from ShrutiMusic.utils.inline.start import owner_panel  # Import owner_panel function
from strings import get_string
from config import BANNED_USERS
from ShrutiMusic import app

@app.on_callback_query(filters.regex("about_page") & ~BANNED_USERS)
async def about_cb(client, callback_query):
    try:
        lang = "en"
        _ = get_string(lang)
        await callback_query.answer()
        await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(about_panel(_))
        )
    except Exception as e:
        await callback_query.answer(f"❌ Error: {e}", show_alert=True)

@app.on_callback_query(filters.regex("owner_page") & ~BANNED_USERS)
async def owner_page_cb(client, callback_query):
    try:
        lang = "en"
        _ = get_string(lang)
        await callback_query.answer()
        await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(owner_panel(_))
        )
    except Exception as e:
        await callback_query.answer(f"❌ Error: {e}", show_alert=True)



from pyrogram import filters
from pyrogram.types import CallbackQuery
from ShrutiMusic import app
from ShrutiMusic.core.call import Nand
from ShrutiMusic.utils import bot_sys_stats
import time, psutil, asyncio

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and result == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        ping_time = str(time_list[x]) + time_suffix_list[x] + " " + ping_time
    return ping_time.strip()

@app.on_callback_query(filters.regex("ping_status"))
async def ping_status_callback(client, callback_query: CallbackQuery):
    
    loading = await callback_query.message.reply_text("🔄 ᴘɪɴɢɪɴɢ...")

    start = time.time()
    try:
        await Nand.ping()
    except:
        pass
    end = time.time()
    ping = round((end - start) * 1000)

    try:
        UP, CPU, RAM, DISK = await bot_sys_stats()
    except Exception:
        UP = "Unknown"
        CPU = psutil.cpu_percent()
        RAM = psutil.virtual_memory().percent
        DISK = psutil.disk_usage('/').percent

    # Step 4: Select Ping Color
    if ping < 100:
        color = "🟢"
    elif ping < 300:
        color = "🟡"
    else:
        color = "🔴"

    final_text = (
        f"📡 ᴘɪɴɢ: {ping}ms {color}\n"
        f"⏱ ᴜᴘᴛɪᴍᴇ: {UP}\n"
        f"💾 ᴅɪꜱᴋ: {DISK}%\n"
        f"📈 ᴍᴇᴍᴏʀʏ: {RAM}%\n"
        f"🖥 ᴄᴘᴜ: {CPU}%"
    )

    await loading.edit_text(final_text)
    
    await asyncio.sleep(8)
    await loading.delete()


@app.on_callback_query(filters.regex("help_page_2"))
async def show_help_page2(client, callback_query: CallbackQuery):
    try:
        language = await get_lang(callback_query.message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")

    await callback_query.message.edit_caption(
        caption=_["help_1"].format(SUPPORT_GROUP),
        reply_markup=help_pannel_page2(_, START=True)
    )

@app.on_callback_query(filters.regex("help_page_3"))
async def show_help_page3(client, callback_query: CallbackQuery):
    try:
        language = await get_lang(callback_query.message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")

    await callback_query.message.edit_caption(
        caption=_["help_1"].format(SUPPORT_GROUP),
        reply_markup=help_pannel_page3(_, START=True)
    )

@app.on_callback_query(filters.regex("help_page_4"))
async def show_help_page4(client, callback_query: CallbackQuery):
    try:
        language = await get_lang(callback_query.message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")

    await callback_query.message.edit_caption(
        caption=_["help_1"].format(SUPPORT_GROUP),
        reply_markup=help_pannel_page4(_, START=True)
    )


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")
    counter = None
    
    if "_" in str(chat):
        bet = chat.split("_")
        chat = bet[0]
        counter = bet[1]
    
    chat_id = int(chat)
    
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    
    mention = CallbackQuery.from_user.mention
    
    if command == "UpVote":
        if chat_id not in votemode:
            votemode[chat_id] = {}
        if chat_id not in upvoters:
            upvoters[chat_id] = {}

        voters = (upvoters[chat_id]).get(CallbackQuery.message.id)
        if not voters:
            upvoters[chat_id][CallbackQuery.message.id] = []

        vote = (votemode[chat_id]).get(CallbackQuery.message.id)
        if not vote:
            votemode[chat_id][CallbackQuery.message.id] = 0

        if CallbackQuery.from_user.id in upvoters[chat_id][CallbackQuery.message.id]:
            (upvoters[chat_id][CallbackQuery.message.id]).remove(
                CallbackQuery.from_user.id
            )
            votemode[chat_id][CallbackQuery.message.id] -= 1
        else:
            (upvoters[chat_id][CallbackQuery.message.id]).append(
                CallbackQuery.from_user.id
            )
            votemode[chat_id][CallbackQuery.message.id] += 1
        
        upvote = await get_upvote_count(chat_id)
        get_upvotes = int(votemode[chat_id][CallbackQuery.message.id])
        
        if get_upvotes >= upvote:
            votemode[chat_id][CallbackQuery.message.id] = upvote
            try:
                exists = confirmer[chat_id][CallbackQuery.message.id]
                current = db[chat_id][0]
            except:
                return await CallbackQuery.edit_message_text(f"ғᴀɪʟᴇᴅ.")
            
            try:
                if current["vidid"] != exists["vidid"]:
                    return await CallbackQuery.edit_message_text(_["admin_35"])
                if current["file"] != exists["file"]:
                    return await CallbackQuery.edit_message_text(_["admin_35"])
            except:
                return await CallbackQuery.edit_message_text(_["admin_36"])
            
            try:
                await CallbackQuery.edit_message_text(_["admin_37"].format(upvote))
            except:
                pass
            
            command = counter
            mention = "ᴜᴘᴠᴏᴛᴇs"
        else:
            if (
                CallbackQuery.from_user.id
                in upvoters[chat_id][CallbackQuery.message.id]
            ):
                await CallbackQuery.answer(_["admin_38"], show_alert=True)
            else:
                await CallbackQuery.answer(_["admin_39"], show_alert=True)
            
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"👍 {get_upvotes}",
                            callback_data=f"ADMIN  UpVote|{chat_id}_{counter}",
                        )
                    ]
                ]
            )
            await CallbackQuery.answer(_["admin_40"], show_alert=True)
            return await CallbackQuery.edit_message_reply_markup(reply_markup=upl)
    else:
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            if CallbackQuery.from_user.id not in SUDOERS:
                admins = adminlist.get(CallbackQuery.message.chat.id)
                if not admins:
                    return await CallbackQuery.answer(_["admin_13"], show_alert=True)
                else:
                    if CallbackQuery.from_user.id not in admins:
                        return await CallbackQuery.answer(
                            _["admin_14"], show_alert=True
                        )
    
    if command == "Pause":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(_["admin_1"], show_alert=True)
        await CallbackQuery.answer()
        await music_off(chat_id)
        await Nand.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_2"].format(mention), reply_markup=close_markup(_)
        )
    
    elif command == "Resume":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(_["admin_3"], show_alert=True)
        await CallbackQuery.answer()
        await music_on(chat_id)
        await Nand.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_4"].format(mention), reply_markup=close_markup(_)
        )
    
    elif command == "Stop" or command == "End":
        await CallbackQuery.answer()
        await Nand.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await CallbackQuery.message.reply_text(
            _["admin_5"].format(mention), reply_markup=close_markup(_)
        )
        await CallbackQuery.message.delete()
    
    elif command == "Skip" or command == "Replay":
        check = db.get(chat_id)
        if not check:
            return await CallbackQuery.answer("No music in queue!", show_alert=True)
        
        if command == "Skip":
            txt = f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
            popped = None
            try:
                popped = check.pop(0)
                if popped:
                    await auto_clean(popped)
                if not check:
                    await CallbackQuery.edit_message_text(
                        f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
                    )
                    await CallbackQuery.message.reply_text(
                        text=_["admin_6"].format(
                            mention, CallbackQuery.message.chat.title
                        ),
                        reply_markup=close_markup(_),
                    )
                    try:
                        return await Nand.stop_stream(chat_id)
                    except:
                        return
            except:
                try:
                    await CallbackQuery.edit_message_text(
                        f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
                    )
                    await CallbackQuery.message.reply_text(
                        text=_["admin_6"].format(
                            mention, CallbackQuery.message.chat.title
                        ),
                        reply_markup=close_markup(_),
                    )
                    return await Nand.stop_stream(chat_id)
                except:
                    return
        else:
            txt = f"➻ sᴛʀᴇᴀᴍ ʀᴇ-ᴘʟᴀʏᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
        
        await CallbackQuery.answer()
        
        if not check:
            return await CallbackQuery.edit_message_text("Queue is empty!")
        
        queued = check[0]["file"]
        title = (check[0]["title"]).title()
        user = check[0]["by"]
        duration = check[0]["dur"]
        streamtype = check[0]["streamtype"]
        videoid = check[0]["vidid"]
        status = True if str(streamtype) == "video" else None
        
        db[chat_id][0]["played"] = 0
        exis = (check[0]).get("old_dur")
        if exis:
            db[chat_id][0]["dur"] = exis
            db[chat_id][0]["seconds"] = check[0]["old_second"]
            db[chat_id][0]["speed_path"] = None
            db[chat_id][0]["speed"] = 1.0
        
        if "live_" in queued:
            n, link = await YouTube.video(videoid, True)
            if n == 0:
                return await CallbackQuery.message.reply_text(
                    text=_["admin_7"].format(title),
                    reply_markup=close_markup(_),
                )
            try:
                image = await YouTube.thumbnail(videoid, True)
            except:
                image = None
            try:
                await Nand.skip_stream(chat_id, link, video=status, image=image)
            except:
                return await CallbackQuery.message.reply_text(_["call_6"])
            
            button = stream_markup(_, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    f"https://t.me/{app.username}?start=info_{videoid}",
                    title[:23],
                    duration,
                    user,
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))
        
        elif "vid_" in queued:
            mystic = await CallbackQuery.message.reply_text(
                _["call_7"], disable_web_page_preview=True
            )
            try:
                file_path, direct = await YouTube.download(
                    videoid,
                    mystic,
                    videoid=True,
                    video=status,
                )
            except:
                return await mystic.edit_text(_["call_6"])
            
            try:
                image = await YouTube.thumbnail(videoid, True)
            except:
                image = None
            
            try:
                await Nand.skip_stream(chat_id, file_path, video=status, image=image)
            except:
                return await mystic.edit_text(_["call_6"])
            
            button = stream_markup(_, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    f"https://t.me/{app.username}?start=info_{videoid}",
                    title[:23],
                    duration,
                    user,
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))
            await mystic.delete()
        
        elif "index_" in queued:
            try:
                await Nand.skip_stream(chat_id, videoid, video=status)
            except:
                return await CallbackQuery.message.reply_text(_["call_6"])
            
            button = stream_markup(_, chat_id)
            run = await CallbackQuery.message.reply_photo(
                photo=STREAM_IMG_URL,
                caption=_["stream_2"].format(user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))
        
        else:
            if videoid == "telegram":
                image = None
            elif videoid == "soundcloud":
                image = None
            else:
                try:
                    image = await YouTube.thumbnail(videoid, True)
                except:
                    image = None
            
            try:
                await Nand.skip_stream(chat_id, queued, video=status, image=image)
            except:
                return await CallbackQuery.message.reply_text(_["call_6"])
            
            if videoid == "telegram":
                button = stream_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=TELEGRAM_AUDIO_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_1"].format(
                        config.SUPPORT_GROUP, title[:23], duration, user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            
            elif videoid == "soundcloud":
                button = stream_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=SOUNCLOUD_IMG_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_1"].format(
                        config.SUPPORT_GROUP, title[:23], duration, user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            
            else:
                button = stream_markup(_, chat_id)
                img = await gen_thumb(videoid)
                run = await CallbackQuery.message.reply_photo(
                    photo=img,
                    caption=_["stream_1"].format(
                        f"https://t.me/{app.username}?start=info_{videoid}",
                        title[:23],
                        duration,
                        user,
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
            
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))


async def markup_timer():
    while True:
        try:
            await asyncio.sleep(7)
            active_chats = await get_active_chats()
            for chat_id in active_chats:
                try:
                    if not await is_music_playing(chat_id):
                        continue
                    playing = db.get(chat_id)
                    if not playing:
                        continue
                    duration_seconds = int(playing[0]["seconds"])
                    if duration_seconds == 0:
                        continue
                    try:
                        mystic = playing[0]["mystic"]
                    except:
                        continue
                    try:
                        check = checker[chat_id][mystic.id]
                        if check is False:
                            continue
                    except:
                        pass
                    try:
                        language = await get_lang(chat_id)
                        _ = get_string(language)
                    except:
                        _ = get_string("en")
                    try:
                        buttons = stream_markup_timer(
                            _,
                            chat_id,
                            seconds_to_min(playing[0]["played"]),
                            playing[0]["dur"],
                        )
                        await mystic.edit_reply_markup(
                            reply_markup=InlineKeyboardMarkup(buttons)
                        )
                    except:
                        continue
                except:
                    continue
        except:
            continue


asyncio.create_task(markup_timer())


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 

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


from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from ShrutiMusic import app
from ShrutiMusic.utils.database import get_lang
from ShrutiMusic.utils.decorators.language import LanguageStart, languageCB
from ShrutiMusic.utils.inline.help import (
    help_back_markup,
    private_help_panel,
    help_pannel_page1,
    help_pannel_page2,
    help_pannel_page3,
    help_pannel_page4,
)
from config import BANNED_USERS, START_IMG_URL, SUPPORT_GROUP
from strings import get_string, helpers


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("help_page_1") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        from ShrutiMusic.utils.inline.help import help_pannel_page1
        keyboard = help_pannel_page1(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_GROUP), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        from ShrutiMusic.utils.inline.help import help_pannel_page1
        keyboard = help_pannel_page1(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_GROUP),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    from ShrutiMusic.utils.inline.help import private_help_panel
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]

    # Helper to return keyboard with correct page
    def get_keyboard_for(cb):
        page1 = ["hb1", "hb2", "hb3", "hb4", "hb5", "hb6", "hb7", "hb8", "hb9", "hb10"]
        page2 = ["hb11", "hb12", "hb13", "hb14", "hb15", "hb17", "hb18", "hb19", "hb20", "hb21"]
        page3 = ["hb22", "hb23", "hb24", "hb25", "hb26", "hb27", "hb28", "hb29", "hb30", "hb31"]
        page4 = ["hb32", "hb33", "hb34", "hb35", "hb36", "hb37", "hb38", "hb39"]

        if cb in page1:
            return help_back_markup(_, page=1)
        elif cb in page2:
            return help_back_markup(_, page=2)
        elif cb in page3:
            return help_back_markup(_, page=3)
        elif cb in page4:
            return help_back_markup(_, page=4)
        else:
            return help_back_markup(_, page=1)  # fallback

    # Show the correct help message based on callback
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=get_keyboard_for(cb))
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=get_keyboard_for(cb))
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=get_keyboard_for(cb))
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=get_keyboard_for(cb))
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=get_keyboard_for(cb))
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=get_keyboard_for(cb))
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=get_keyboard_for(cb))
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=get_keyboard_for(cb))
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=get_keyboard_for(cb))
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=get_keyboard_for(cb))
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=get_keyboard_for(cb))
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=get_keyboard_for(cb))
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=get_keyboard_for(cb))
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=get_keyboard_for(cb))
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=get_keyboard_for(cb))
    elif cb == "hb16":
        await CallbackQuery.edit_message_text(helpers.HELP_16, reply_markup=get_keyboard_for(cb))
    elif cb == "hb17":
        await CallbackQuery.edit_message_text(helpers.HELP_17, reply_markup=get_keyboard_for(cb))
    elif cb == "hb18":
        await CallbackQuery.edit_message_text(helpers.HELP_18, reply_markup=get_keyboard_for(cb))
    elif cb == "hb19":
        await CallbackQuery.edit_message_text(helpers.HELP_19, reply_markup=get_keyboard_for(cb))
    elif cb == "hb20":
        await CallbackQuery.edit_message_text(helpers.HELP_20, reply_markup=get_keyboard_for(cb))
    elif cb == "hb21":
        await CallbackQuery.edit_message_text(helpers.HELP_21, reply_markup=get_keyboard_for(cb))
    elif cb == "hb22":
        await CallbackQuery.edit_message_text(helpers.HELP_22, reply_markup=get_keyboard_for(cb))
    elif cb == "hb23":
        await CallbackQuery.edit_message_text(helpers.HELP_23, reply_markup=get_keyboard_for(cb))
    elif cb == "hb24":
        await CallbackQuery.edit_message_text(helpers.HELP_24, reply_markup=get_keyboard_for(cb))
    elif cb == "hb25":
        await CallbackQuery.edit_message_text(helpers.HELP_25, reply_markup=get_keyboard_for(cb))
    elif cb == "hb26":
        await CallbackQuery.edit_message_text(helpers.HELP_26, reply_markup=get_keyboard_for(cb))
    elif cb == "hb27":
        await CallbackQuery.edit_message_text(helpers.HELP_27, reply_markup=get_keyboard_for(cb))
    elif cb == "hb28":
        await CallbackQuery.edit_message_text(helpers.HELP_28, reply_markup=get_keyboard_for(cb))
    elif cb == "hb29":
        await CallbackQuery.edit_message_text(helpers.HELP_29, reply_markup=get_keyboard_for(cb))
    elif cb == "hb30":
        await CallbackQuery.edit_message_text(helpers.HELP_30, reply_markup=get_keyboard_for(cb))
    elif cb == "hb31":
        await CallbackQuery.edit_message_text(helpers.HELP_31, reply_markup=get_keyboard_for(cb))
    elif cb == "hb32":
        await CallbackQuery.edit_message_text(helpers.HELP_32, reply_markup=get_keyboard_for(cb))
    elif cb == "hb33":
        await CallbackQuery.edit_message_text(helpers.HELP_33, reply_markup=get_keyboard_for(cb))
    elif cb == "hb34":
        await CallbackQuery.edit_message_text(helpers.HELP_34, reply_markup=get_keyboard_for(cb))
    elif cb == "hb35":
        await CallbackQuery.edit_message_text(helpers.HELP_35, reply_markup=get_keyboard_for(cb))
    elif cb == "hb36":
        await CallbackQuery.edit_message_text(helpers.HELP_36, reply_markup=get_keyboard_for(cb))
    elif cb == "hb37":
        await CallbackQuery.edit_message_text(helpers.HELP_37, reply_markup=get_keyboard_for(cb))
    elif cb == "hb38":
        await CallbackQuery.edit_message_text(helpers.HELP_38, reply_markup=get_keyboard_for(cb))
    elif cb == "hb39":
        await CallbackQuery.edit_message_text(helpers.HELP_39, reply_markup=get_keyboard_for(cb))
        


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 

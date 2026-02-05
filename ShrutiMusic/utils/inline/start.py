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

from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["E_X_1"], url=config.UPSTREAM_REPO),
            InlineKeyboardButton(text=_["S_B_11"], callback_data="about_page")  # About button
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_11"],
                callback_data="about_page"
            ),
            InlineKeyboardButton(
                text=_["S_B_12"],
                callback_data="owner_page"
            )
        ],
        [
            InlineKeyboardButton(
                text="ကိုယ်ပိုင် Bot လုပ်ရန် 🇲🇲",
                url="https://t.me/SHWEMM_TEAM"
            ),
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="help_page_1")
        ],
    ]
    return buttons

def about_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")
        ]
    ]
    return buttons

def owner_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_H_1"], url=config.INSTAGRAM),
            InlineKeyboardButton(text=_["S_H_2"], url=config.YOUTUBE),
        ],
        [
            InlineKeyboardButton(text=_["S_H_3"], url=config.GITHUB),
            InlineKeyboardButton(text=_["S_H_4"], url=config.DONATE),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")
        ]
    ]
    return buttons


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 

"""
░█▀█░█▀▄░█▀█░█▀█░█▀▄░▀█▀░█▀▀░▀█▀░█▀█░█▀▄░█░█░░░█░░░▀█▀░█▀▀░█▀▀░█▀█░█▀▀░█▀▀
░█▀▀░█▀▄░█░█░█▀▀░█▀▄░░█░░█▀▀░░█░░█▀█░█▀▄░░█░░░░█░░░░█░░█░░░█▀▀░█░█░▀▀█░█▀▀
░▀░░░▀░▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀

Copyright (c) 2025 Nand Yaduwanshi (@NoxxOP)
Location: Supaul, Bihar
Email: badboy809075@gmail.com
GitHub: https://github.com/NoxxOP

All rights reserved.

This code is the intellectual property of Nand Yaduwanshi.
You are not allowed to copy, modify, redistribute, or use this
code for commercial or personal projects without explicit permission.

Allowed:
- Forking for personal learning
- Submitting improvements via pull requests

Not Allowed:
- Claiming this code as your own
- Re-uploading without credit or permission
- Selling or using commercially

Love From ShrutiBots
Telegram: https://t.me/ShrutiBots
"""

from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ShrutiMusic import app

def help_pannel_page1(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1"),
                InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3"),
                InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5"),
                InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6"),
                InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8"),
                InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9"),
                InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10"),
            ],
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_4"),
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_2"),
            ],
        ]
    )

def help_pannel_page2(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11"),
                InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13"),
                InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15"),
                InlineKeyboardButton(text=_["H_B_16"], callback_data="help_callback hb16"),
                InlineKeyboardButton(text=_["H_B_17"], callback_data="help_callback hb17"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_18"], callback_data="help_callback hb18"),
                InlineKeyboardButton(text=_["H_B_19"], callback_data="help_callback hb19"),
                InlineKeyboardButton(text=_["H_B_20"], callback_data="help_callback hb20"),
            ],
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_1"),
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_3"),
            ],
        ]
    )

def help_pannel_page3(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_21"], callback_data="help_callback hb21"),
                InlineKeyboardButton(text=_["H_B_22"], callback_data="help_callback hb22"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_23"], callback_data="help_callback hb23"),
                InlineKeyboardButton(text=_["H_B_24"], callback_data="help_callback hb24"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_25"], callback_data="help_callback hb25"),
                InlineKeyboardButton(text=_["H_B_26"], callback_data="help_callback hb26"),
                InlineKeyboardButton(text=_["H_B_27"], callback_data="help_callback hb27"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_28"], callback_data="help_callback hb28"),
                InlineKeyboardButton(text=_["H_B_29"], callback_data="help_callback hb29"),
                InlineKeyboardButton(text=_["H_B_30"], callback_data="help_callback hb30"),
            ],
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_2"),
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_4"),
            ],
        ]
    )

def help_pannel_page4(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_31"], callback_data="help_callback hb31"),
                InlineKeyboardButton(text=_["H_B_32"], callback_data="help_callback hb32"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_33"], callback_data="help_callback hb33"),
                InlineKeyboardButton(text=_["H_B_34"], callback_data="help_callback hb34"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_35"], callback_data="help_callback hb35"),
                InlineKeyboardButton(text=_["H_B_37"], callback_data="help_callback hb37"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_38"], callback_data="help_callback hb38"),
                InlineKeyboardButton(text=_["H_B_39"], callback_data="help_callback hb39"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_36"], callback_data="help_callback hb36"),
            ],   
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_3"),
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_1"),
            ],
        ]
    )

def help_back_markup(_, page: int = 1):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"help_page_{page}",
                )
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ]
    ]

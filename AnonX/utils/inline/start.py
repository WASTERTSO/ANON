from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeybᴏardButton(
                text="𝑨𝒅𝒅 𝑴𝒆 𝑩𝒂𝒃𝒚 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑺𝒖𝒑𝒑𝒐𝒓𝒕 🚑",
                url=f"https://t.me/full_on_bakchodii",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 ❓",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=""𝑺𝒆𝒕𝒕𝒊𝒏𝒈𝒔 ⚙, callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝑴𝒆 𝑩𝒂𝒃𝒚 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 ❓", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑀𝑎𝑖𝑛𝑡𝑎𝑖𝑛𝑒𝑟 💸", url=f"https://t.me/about_your_shiv"
            )
            ],
     ]
    return buttons

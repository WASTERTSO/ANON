from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝑴𝒆 𝑩𝒂𝒃𝒚 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑 🚨",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑺𝒆𝒕𝒕𝒊𝒏𝒈𝒔 ⚙", callback_data="settings_helper"
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
                text="𝑯𝒆𝒍𝒑 🚨", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑺𝒖𝒑𝒑𝒐𝒓𝒕 🚑", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝑼𝒑𝒅𝒂𝒕𝒆𝒔 ❓", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑫𝒆𝒗 👨‍💻", url=config.OWNER_ID
            )
        ],
     ]
    return buttons

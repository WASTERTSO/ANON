from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐴𝑑𝑑 𝑀𝑒 𝐵𝑎𝑏𝑦 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠 🚨",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑆𝑒𝑡𝑡𝑖𝑛𝑔𝑠 ⚙", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐴𝑑𝑑 𝑀𝑒 𝐵𝑎𝑏𝑦 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠 🚨", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑆𝑢𝑝𝑝𝑜𝑟𝑡 🚑", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝑈𝑝𝑑𝑎𝑡𝑒𝑠 ❓", url=config.SUPPORT_CHANNEL
            )
            ].
     ]
    return buttons

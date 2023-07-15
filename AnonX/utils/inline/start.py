from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeybᴏardButton(
                text="𝐴𝑑𝑑 𝑀𝑒 𝑇𝑜 𝑌𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑂𝑤𝑛𝑒𝑟 💸",
                url=f"https://t.me/sleeping_alwasy",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐻𝑒𝑙𝑝 ❓",
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
                text="𝐴𝑑𝑑 𝑀𝑒 𝑇𝑜 𝑌𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐻𝑒𝑙𝑝 𝐴𝑛𝑑 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠 ❓", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑂𝑤𝑛𝑒𝑟 💸", url=f"https://t.me/sleeping_alwasy"
            )
            ],
     ]
    return buttons

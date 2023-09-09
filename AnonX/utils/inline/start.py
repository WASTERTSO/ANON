from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeybᴏardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴅᴇᴠᴇʟᴏᴘᴇʀ",
                url=f"https://t.me/tso_king",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/tso_king"
            )
            ],
     ]
    return buttons

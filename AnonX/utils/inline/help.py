from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="fallen_back",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴍɪɴ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ᴀᴜᴛʜ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="ʙʀᴏᴀᴅᴄᴀsᴛ",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʙʟᴀᴄᴋ-ʟɪsᴛ",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="sʜᴜғғʟᴇ",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="ʙʟ-ᴜsᴇʀ",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ɢʙᴀɴ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="ʟᴏᴏᴘ",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="ᴄ-ᴘʟᴀʏ",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴘɪɴɢ",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="ᴘʟᴀʏ",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="ᴍᴀɪɴᴛᴇɴ",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

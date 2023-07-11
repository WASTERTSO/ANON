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
            callback_data=f"settingsback_helper",
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
                    text="𝐴𝑑𝑚𝑖𝑛",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝐴𝑢𝑡𝒉",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝐵𝑙𝑎𝑐𝑘𝑙𝑖𝑠𝑡",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐵𝑟𝑜𝑎𝑑𝑐𝑎𝑠𝑡",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝐺𝑏𝑎𝑛",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="𝐿𝑦𝑟𝑖𝑐𝑠",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝑃𝑖𝑛𝑔",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="𝑃𝑙𝑎𝑦",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="𝑃𝑙𝑎𝑦𝑙𝑖𝑠𝑡",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝑉𝑖𝑑𝑒𝑜𝑐𝒉𝑎𝑡𝑠",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="𝑆𝑡𝑎𝑟𝑡",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="𝑆𝑢𝑑𝑜",
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
                text="𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠 🚨",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

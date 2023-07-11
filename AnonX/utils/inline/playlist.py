from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑃𝑒𝑟𝑠𝑜𝑛𝑎𝑙",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="𝐺𝑙𝑜𝑏𝑎𝑙", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐶𝑙𝑜𝑠𝑒", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑇𝑜𝑝 10 𝑃𝑙𝑎𝑦𝑙𝑖𝑠𝑡", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑃𝑒𝑟𝑠𝑜𝑛𝑎𝑙", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐺𝑙𝑜𝑏𝑎𝑙", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="𝐺𝑟𝑜𝑢𝑝'𝑠", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐵𝑎𝑐𝑘", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="𝐶𝑙𝑜𝑠𝑒", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐴𝑢𝑑𝑖𝑜", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="𝑉𝑖𝑑𝑒𝑜", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐵𝑎𝑐𝑘", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="𝐶𝑙𝑜𝑠𝑒", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑇𝑜𝑝 10 𝑃𝑙𝑎𝑦𝑙𝑖𝑠𝑡", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑃𝑒𝑟𝑠𝑜𝑛𝑎𝑙", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐺𝑙𝑜𝑏𝑎𝑙", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="𝐺𝑟𝑜𝑢𝑝'𝑠", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐵𝑎𝑐𝑘", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="𝐵𝑎𝑐𝑘", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐵𝑎𝑐𝑘",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="𝐶𝑙𝑜𝑠𝑒", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝐷𝑒𝑙𝑒𝑡𝑒",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐵𝑎𝑐𝑘",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="𝐶𝑙𝑜𝑠𝑒",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝐶𝑙𝑜𝑠𝑒",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl

import asyncio
import time

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config import OWNER_ID
from strings import get_command, get_string
from AnonX import Telegram, YouTube, app
from AnonX.misc import SUDOERS, _boot_
from AnonX.plugins.playlist import del_plist_msg
from AnonX.plugins.sudoers import sudoers_list
from AnonX.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from AnonX.utils.decorators.language import LanguageStart
from AnonX.utils.formatters import get_readable_time
from AnonX.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            await message.reply_sticker("CAACAgIAAxkDAAIB_GSte9ArHQS7e8oOZ-KO96mtImkvAAIoIAACJaYJS-FqCk576-FVLwQ")
            return await message.reply_photo(
                       photo=config.START_IMG_URL,
                       caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 𝐺𝑒𝑡𝑡𝑖𝑛𝑔 𝑌𝑜𝑢𝑟 𝑃𝑒𝑟𝑠𝑜𝑛𝑎𝑙 𝑆𝑡𝑎𝑡𝑠 𝐹𝑟𝑜𝑚 {config.MUSIC_BOT_NAME} 𝑆𝑒𝑟𝑣𝑒𝑟."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚](https://t.me/strangers_hell) ** 𝑃𝑙𝑎𝑦𝑒𝑑 {count} 𝑇𝑖𝑚𝑒𝑠**\n\n"
                    else:
                        msg += f"🔗 [{𝑇𝑖𝑡𝑙𝑒}](https://www.youtube.com/watch?v={vidid}) ** 𝑃𝑙𝑎𝑦𝑒𝑑 {count} 𝑇𝑖𝑚𝑒𝑠**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} 𝐽𝑢𝑠𝑡 𝑆𝑡𝑎𝑟𝑡𝑒𝑑 𝑇𝒉𝑒 𝐵𝑜𝑡 𝑡𝑜 𝐶𝒉𝑒𝑐𝑘 <code>𝑆𝑢𝑑𝑜𝑙𝑖𝑠𝑡</code>\n\n**𝑈𝑠𝑒𝑟 𝑖𝑑:** {sender_id}\n**𝑈𝑠𝑒𝑟𝑛𝑎𝑚𝑒:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "𝐹𝑎𝑖𝑙𝑒𝑑 𝑇𝑜 𝐺𝑒𝑡 𝐿𝑦𝑟𝑖𝑐𝑠."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name == "verify":
            await message.reply_text(f"𝐻𝑒𝑦 {message.from_user.first_name},\n𝑇𝒉𝑎𝑛𝑘𝑠 𝐹𝑜𝑟 𝑉𝑒𝑟𝑖𝑓𝑖𝑛𝑔 𝑌𝑜𝑢𝑟𝑠𝑒𝑙𝑓 {config.MUSIC_BOT_NAME}, 𝐼𝑛 𝐵𝑎𝑐𝑘 𝐴𝑛𝑑 𝑆𝑡𝑎𝑟𝑡 𝑈𝑠𝑖𝑛𝑔 𝑀𝑒.")
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} 𝐽𝑢𝑠𝑡 𝑆𝑡𝑎𝑟𝑡𝑒𝑑 𝑇𝒉𝑒 𝐵𝑜𝑡 𝑇𝑜 <code>𝑉𝑒𝑟𝑖𝑓𝑦 𝐻𝑖𝑚𝑠𝑒𝑙𝑓</code>\n\n**𝑈𝑠𝑒𝑟 𝑖𝑑:** {sender_id}\n**𝑈𝑠𝑒𝑟𝑛𝑎𝑚𝑒:** {sender_name}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
**𝑇𝑟𝑎𝑐𝑘 𝐼𝑛𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛**

📌 **𝑇𝑖𝑡𝑙𝑒:** {title}

⏳ **𝐷𝑢𝑟𝑎𝑡𝑖𝑜𝑛:** {duration} 𝑀𝑖𝑛𝑢𝑡𝑒𝑠
👀 **𝑉𝑖𝑒𝑤𝑠:** `{views}`
⏰ **𝑃𝑢𝑏𝑙𝑖𝑠𝒉𝑒𝑑 𝑂𝑛:** {published}
🎥 **𝐶𝒉𝑎𝑛𝑛𝑒𝑙:** {channel}
📎 **𝐶𝒉𝑎𝑛𝑛𝑒𝑙 𝐿𝑖𝑛𝑘:** [𝑉𝑖𝑠𝑖𝑡 𝐶𝒉𝑎𝑛𝑛𝑒𝑙]({channellink})
🔗 **𝐿𝑖𝑛𝑘:** [𝑊𝑎𝑡𝑐𝒉 𝑂𝑛 𝑌𝑜𝑢𝑡𝑢𝑏𝑒]({link})

💖 𝑆𝑒𝑎𝑟𝑐𝒉 𝑃𝑜𝑤𝑒𝑟𝑒𝑑 𝐵𝑦 {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝑌𝑜𝑢𝑡𝑢𝑏𝑒", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="𝑆𝑢𝑝𝑝𝑜𝑟𝑡 🚑", url="https://t.me/strangers_hell"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_sticker("CAACAgIAAxkDAAIEtmSzvBqE5cxPp6t95DAo1ZUHp7TqAAIoIAACJaYJS-FqCk576-FVLwQ")
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**ᴩʀɪᴠᴀᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ**\n\nᴏɴʟʏ ғᴏʀ ᴛʜᴇ ᴄʜᴀᴛs ᴀᴜᴛʜᴏʀɪsᴇᴅ ʙʏ ᴍʏ ᴏᴡɴᴇʀ, ʀᴇǫᴜᴇsᴛ ɪɴ ᴍʏ ᴏᴡɴᴇʀ's ᴩᴍ ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ᴀɴᴅ ɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛᴏ ᴅᴏ sᴏ ᴛʜᴇɴ ғᴜ*ᴋ ᴏғғ ʙᴇᴄᴀᴜsᴇ ɪ'ᴍ ʟᴇᴀᴠɪɴɢ."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                OWNER = OWNER_ID[0]
                out = start_pannel(_, app.username, OWNER)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return

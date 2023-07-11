from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            InlineQueryResultPhoto)
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[
                0
            ]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝑌𝑜𝑢𝑡𝑢𝑏𝑒",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
📌 **𝑇𝑖𝑡𝑙𝑒:** [{title}]({link})

⏳ **𝐷𝑢𝑟𝑎𝑡𝑖𝑜𝑛:** {duration} Mins
👀 **𝑉𝑖𝑒𝑤𝑠:** `{views}`
⏰ **𝑃𝑢𝑏𝑙𝑖𝑠𝒉𝑒𝑑:** {published}
🎥 **𝐶𝒉𝑎𝑛𝑛𝑒𝑙:** {channel}
📎 **𝐶𝒉𝑎𝑛𝑛𝑒𝑙 𝐿𝑖𝑛𝑘:** [𝑉𝑖𝑠𝑖𝑡 𝐶𝒉𝑎𝑛𝑛𝑒𝑙]({channellink})

💖 **𝑆𝑒𝑎𝑟𝑐𝒉 𝑃𝑜𝑤𝑒𝑟𝑒𝑑 𝐵𝑦 {MUSIC_BOT_NAME}**"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(
                query.id, results=answers
            )
        except:
            return

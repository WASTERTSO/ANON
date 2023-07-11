import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**𝑅𝑢𝑛𝑛𝑖𝑔 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 𝑆𝑝𝑒𝑒𝑑𝑡𝑒𝑠𝑡...**")
        test.download()
        m = m.edit("**𝑅𝑢𝑛𝑛𝑖𝑔 𝑈𝑝𝑙𝑜𝑎𝑑 𝑆𝑝𝑒𝑒𝑑𝑡𝑒𝑠𝑡...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**𝑆𝒉𝑎𝑟𝑖𝑛𝑔 𝑆𝑝𝑒𝑒𝑑𝑡𝑒𝑠𝑡 𝑅𝑒𝑠𝑢𝑙𝑡𝑠...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 𝑇𝑦𝑟𝑖𝑛𝑔 𝑇𝑜 𝐶𝒉𝑒𝑐𝑘 𝑈𝑝𝑙𝑜𝑎𝑑 𝐴𝑛𝑑 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 𝑆𝑝𝑒𝑒𝑑...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f""" **𝑆𝑝𝑒𝑒𝑑𝑡𝑒𝑠𝑡 𝑅𝑒𝑠𝑢𝑙𝑡𝑠** 
    
<u>**𝐶𝑖𝑙𝑒𝑛𝑡 :**</u>
**__𝐼𝑠𝑝 :__** {result['client']['isp']}
**__𝐶𝑜𝑢𝑛𝑡𝑟𝑦 :__** {result['client']['country']}
  
<u>**𝑆𝑒𝑟𝑣𝑒𝑟 :**</u>
**__𝑁𝑎𝑚𝑒 :__** {result['server']['name']}
**__𝐶𝑜𝑢𝑛𝑡𝑟𝑦 :__** {result['server']['country']}, {result['server']['cc']}
**__𝑆𝑝𝑜𝑛𝑠𝑜𝑟 :__** {result['server']['sponsor']}
**__𝐿𝑎𝑡𝑒𝑛𝑐𝑦 :__** {result['server']['latency']}  
**__𝑃𝑖𝑛𝑔 :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()

from pyrogram import Client, idle
from pyromod import listen

OWNER_ID = int(f"7291869416")
ch = "z1_xa" 
OWNER_USERNAME = "dev_blal"
ST = "z1_xa"
LT = "z1_xa"
DEVS = []
DEVS.append(OWNER_USERNAME)
DEVS.append(ST)
DEVS.append(LT)
OWNER = "عباس"

bot_token="توكن"
bot_token2="كود جلسه بايروجرام "


bot = Client("ITA", api_id=9671629, api_hash="be5c84e9dc1ca0e2b53d54b71e575124", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=9671629, api_hash="be5c84e9dc1ca0e2b53d54b71e575124", session_string=bot_token2)    

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(OWNER_USERNAME, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()

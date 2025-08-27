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

bot_token="7121027327:AAEVE4wgyK0LKfH62OZ36dPbwknj-nPkvrs"
bot_token2="1BJWap1sBu4jlc1gdc77ZEfKecrk9xPJ5Kz8SpTnRpvrXhQXnxAAgXK_EY3XigWO-dQCPIfVd1HSP5TH_3bpobzrsNv0hZeE2fQ_UZwX4jZME13aEBwp4o1Z9XNPyRDWRChEzQhkwmx7y9grdsfD4B0TBntq67TidMU_TRnVt5CRELKAqkl4sQSCH8e2TcxFP0gbHrASvVwzDxp88VyhQOvWld3gRfOR0d43OoLnLPXUOJPGNdRSqNDrSV1kV0YNc1BQnsg-3iA7ZnqpqZY784p-84M-CZOmSErRUfcPDL0j_QuSh4AT1uDQLcYwch-EWggpR9vIg8RjmMh-gkzUX-FqPz_sJkN4="


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

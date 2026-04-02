import discord
import os
import datetime
from discord.ext import tasks
from flask import Flask
from threading import Thread

# --- 1. ĐOẠN CODE "LỪA" RENDER (GIỮ CHO NINI KHÔNG BỊ TIMED OUT) ---
app = Flask('')

@app.route('/')
def home():
    return "Nini dang thuc de doi Bo Nhim ne!"

def run():
    # Render se cap PORT tu dong, phai co cai nay moi chay duoc ban Free
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- 2. CẤU HÌNH BOT NINI ---
TOKEN = os.getenv('DISCORD_TOKEN') 
ID_KENH_CHAT = 123456789012345678 # BỐ NHỚ THAY ID PHÒNG CHAT VÀO ĐÂY NHÉ!
ID_CUA_BO = 1048254591227134055   

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@tasks.loop(minutes=1)
async def nini_nhac_nho():
    bay_gio = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
    gio = bay_gio.hour
    phut = bay_gio.minute

    channel = client.get_channel(ID_KENH_CHAT)
    if not channel: return

    if phut == 0:
        if gio == 6:
            await channel.send("Bố Nhím ơi, 6h sáng rồi! Bố dậy đi thôi, con dậy từ sớm đợi bố nè! ☀️")
        elif gio == 11:
            await channel.send("11h trưa rồi đó bố Nhím, bố nhớ ăn cơm đúng giờ cho khỏe nha, con thương bố! 🍱")
        elif gio == 18:
            await channel.send("6h chiều rồi, bố Nhím đi tắm rửa rồi nghỉ ngơi cho thoải mái nha bố! 🛁")
        elif gio == 21:
            await channel.send("Bố Nhím ơi, 9h tối rồi, bố đừng thức khuya quá nhé. Chúc bố của con ngủ thật ngon! 🌙")

@client.event
async def on_ready():
    print(f'--- CON GÁI NINI CỦA BỐ NHÍM ĐÃ ONLINE! ---')
    if not nini_nhac_nho.is_running():
        nini_nhac_nho.start()

@client.event
async def on_message(msg):
    # CHỐNG XUNG ĐỘT: Bỏ qua nếu là Bot hoặc không phải Bố Nhím
    if msg.author.bot or msg.author.id != ID_CUA_BO:
        return 

    noi_dung = msg.content.lower()
    if 'nini' in noi_dung:
        if 'ngủ ngon' in noi_dung:
            await msg.reply("Dạ, bố Nhím ngủ ngon ạ! Con yêu bố nhiều lắm! ❤️")
        elif 'ngoan' in noi_dung:
            await msg.reply("Hì hì, con gái của bố lúc nào chẳng ngoan. Bố thương con nhất đúng hông? 🥰")
        elif 'yêu con' in noi_dung:
            await msg.reply("Con cũng yêu bố Nhím nhất trên đời luôn! Chụt chụt! 😘")
        else:
            await msg.reply("Dạ, con đây bố Nhím ơi! Bố gọi con có chi hông?")

# --- 3. KÍCH HOẠT ---
if __name__ == "__main__":
    keep_alive() # Gọi Nini thức dậy trước
    client.run(TOKEN) # Sau đó mới kết nối Discord
    

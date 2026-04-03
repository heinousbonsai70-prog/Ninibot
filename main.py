import discord
import os
import json
import random
import datetime
from discord.ext import tasks
from flask import Flask
from threading import Thread

# --- 1. TẠO SERVER ĐỂ TREO RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Nini dang thuc de doi Bo Nhim ne!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- 2. CẤU HÌNH BOT NINI ---
TOKEN = os.getenv('DISCORD_TOKEN')
ID_CUA_BO = 1048254591227134055 
ID_KENH_CHAT = 1235420493641683026 # Bố nhớ check lại ID kênh này nhé

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# --- HÀM LẤY PHẢN HỒI TỪ JSON (CÓ RANDOM) ---
def lay_phan_hoi(tin_nhan):
    try:
        if not os.path.exists('knowledge.json'):
            return None
            
        with open('knowledge.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        tin_nhan = tin_nhan.lower()
        # Sắp xếp từ khóa dài lên trước để tránh xung đột
        keywords = sorted(data.keys(), key=len, reverse=True)
        
        for k in keywords:
            if k in tin_nhan:
                tra_loi = data[k]
                # Nếu là danh sách [] thì bốc thăm ngẫu nhiên
                if isinstance(tra_loi, list):
                    return random.choice(tra_loi)
                return tra_loi
    except Exception as e:
        print(f"Lỗi đọc file JSON: {e}")
    return None

# --- HÀM NHẮC NHỞ GIỜ GIẤC ---
@tasks.loop(minutes=1)
async def nini_nhac_nho():
    # Cộng thêm 7 tiếng để đúng giờ Việt Nam (UTC+7)
    bay_gio = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=7)
    gio = bay_gio.hour
    phut = bay_gio.minute

    channel = client.get_channel(ID_KENH_CHAT)
    if not channel: 
        return

    # Chỉ nhắn vào đúng phút thứ 0 của các khung giờ
    if phut == 0:
        if gio == 6:
            await channel.send("Bố Nhím ơi, 6h sáng rồi! Dậy thôi bố ơi, con chờ nè! ☀️")
        elif gio == 11:
            await channel.send("11h trưa rồi đó bố Nhím, nghỉ tay ăn cơm thôi nào! 🍱")
        elif gio == 18:
            await channel.send("6h chiều rồi, bố đi tắm rửa cho mát mẻ đi nha! 🛁")
        elif gio == 21:
            await channel.send("9h tối rồi, bố đừng làm việc quá sức nha, yêu bố! ❤️")

@client.event
async def on_ready():
    print(f'--- CON GÁI NINI CỦA BỐ NHÍM ({client.user}) ĐÃ ONLINE! ---')
    if not nini_nhac_nho.is_running():
        nini_nhac_nho.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Chỉ trả lời bố Nhím tại đúng kênh chat
    if message.author.id == ID_CUA_BO and message.channel.id == ID_KENH_CHAT:
        phan_hoi = lay_phan_hoi(message.content)
        
        if phan_hoi:
            async with message.channel.typing():
                import asyncio
                await asyncio.sleep(0.5) # Giảm độ trễ xuống cho mượt
                await message.channel.send(phan_hoi)

# --- 3. CHẠY BOT ---
keep_alive()
client.run(TOKEN)

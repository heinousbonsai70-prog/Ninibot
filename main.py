import discord
import os
import json
import random
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
ID_CUA_BO = 1048254591227134055 # ID tài khoản Discord của bố Nhím
ID_KENH_CHAT = 123456789012345678 # Bố nhớ thay ID phòng chat vào đây

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Hàm đọc file kiến thức JSON và bốc thăm câu trả lời
def lay_phan_hoi(tin_nhan):
    try:
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

@client.event
async def on_ready():
    print(f'--- CON GÁI NINI CỦA BỐ NHÍM ({client.user}) ĐÃ ONLINE! ---')

@client.event
async def on_message(message):
    # KHÔNG trả lời chính mình
    if message.author == client.user:
        return
    
    # CHỈ trả lời nếu người nhắn là Bố Nhím và nhắn đúng trong phòng chat quy định
    if message.author.id == ID_CUA_BO and message.channel.id == ID_KENH_CHAT:
        
        phan_hoi = lay_phan_hoi(message.content)
        
        if phan_hoi:
            # Tạo hiệu ứng đang soạn tin nhắn cho tự nhiên
            async with message.channel.typing():
                import asyncio
                await asyncio.sleep(1) # Chờ 1 giây rồi mới gửi
                await message.channel.send(phan_hoi)

# --- 3. CHẠY BOT ---
keep_alive()
client.run(TOKEN)
    

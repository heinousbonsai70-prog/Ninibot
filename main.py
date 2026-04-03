import discord
import json
import random
import os
from flask import Flask
from threading import Thread

# --- CÀI ĐẶT THÔNG SỐ (Bố giữ nguyên ID cũ của bố nhé) ---
TOKEN = os.getenv('DISCORD_TOKEN')
ID_CUA_BO = 1111628173499318353  # ID Discord của bố Nhím
ID_KENH_CHAT = 1235420493641683026 # ID kênh chat của Nini

# --- PHẦN 1: TẠO WEB SERVER ĐỂ TREO BOT (API) ---
app = Flask('')

@app.route('/')
def home():
    return "Nini dang thuc de doi Bo Nhim ne! 🐧💎🔥"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- PHẦN 2: LOGIC XỬ LÝ PHẢN HỒI ---
def lay_phan_hoi(tin_nhan):
    try:
        if not os.path.exists('knowledge.json'):
            return None
            
        with open('knowledge.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        tin_nhan = tin_nhan.lower()
        
        # Bộ lọc thông minh "Ăn gian" cho bố
        thay_the = {
            "lmj": "làm gì",
            "đó": "",
            "thế": "",
            "vậy": "",
            "đê": "",
            "nini": "" # Xóa tên bot để tập trung vào từ khóa chính
        }
        for cu, moi in thay_the.items():
            tin_nhan = tin_nhan.replace(cu, moi)
        
        tin_nhan = tin_nhan.strip()
        
        # Tìm từ khóa trong não (Ưu tiên từ dài nhất trước)
        keywords = sorted(data.keys(), key=len, reverse=True)
        for k in keywords:
            if k in tin_nhan and k != "":
                return random.choice(data[k])
    except Exception as e:
        print(f"Lỗi não bộ: {e}")
    return None

# --- PHẦN 3: BOT DISCORD CHÍNH ---
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- CON GÁI NINI CỦA BỐ NHÍM ({client.user}) ĐÃ ONLINE! ---')

@client.event
async def on_message(message):
    # Chỉ trả lời tin nhắn của Bố Nhím và trong đúng kênh chat
    if message.author.id != ID_CUA_BO or message.channel.id != ID_KENH_CHAT:
        return

    # 1. Tính năng Dạy học trực tiếp: !day từ khóa | câu trả lời
    if message.content.startswith('!day '):
        try:
            parts = message.content[5:].split('|')
            if len(parts) < 2:
                await message.channel.send("Sai cú pháp rồi bố ơi! Phải là: `!day từ | câu trả lời` nha.")
                return
            
            tu_khoa = parts[0].strip().lower()
            cau_tra_loi = parts[1].strip()

            with open('knowledge.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            if tu_khoa in data:
                if cau_tra_loi not in data[tu_khoa]:
                    data[tu_khoa].append(cau_tra_loi)
            else:
                data[tu_khoa] = [cau_tra_loi]

            with open('knowledge.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            await message.channel.send(f"Dạ, con đã học thuộc lòng từ **'{tu_khoa}'** rồi ạ! Bố thử nhắn xem.")
        except Exception as e:
            await message.channel.send(f"Lỗi nạp não rồi bố: {e}")
        return

    # 2. Trả lời tự động dựa trên file JSON
    tra_loi = lay_phan_hoi(message.content)
    if tra_loi:
        await message.channel.send(tra_loi)

# --- CHẠY BOT ---
keep_alive()
try:
    client.run(TOKEN)
except discord.errors.HTTPException:
    print("\n\n\nLỖI: Discord chặn kết nối (Rate Limit). Bố đợi 15p rồi hãy thử lại nhé!\n\n\n")
        

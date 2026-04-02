import discord
import google.generativeai as genai
import os
from flask import Flask
import threading

# --- 1. PHẦN GIỮ BOT ONLINE (DÀNH CHO RENDER) ---
app = Flask('')
@app.route('/')
def home():
    return "Nini is alive and smart! ✨"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- 2. CẤU HÌNH BỘ NÃO AI (GEMINI) ---
# Tui đã thay cái Key mới nhất Nhím vừa gửi vào đây:
GEMINI_KEY = 'AIzaSyC-uSThseb4qzlaMCSdrm2fJPyAxImVNlI'

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. CẤU HÌNH BOT DISCORD ---
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # Khi thấy dòng này trong Log là Bot đã chạy thành công!
    print(f'--- NINI ĐÃ CÓ NÃO VÀ ONLINE! ---')
    await client.change_presence(activity=discord.Game(name="Minecraft với Nhím ✨"))

@client.event
async def on_message(msg):
    # CHỐNG LẶP: Nếu là chính Bot nói thì bỏ qua, không tự trả lời mình
    if msg.author == client.user:
        return
    
    # TRẢ LỜI KHI GỌI TÊN: Chỉ trả lời khi trong câu có chữ "nini"
    if 'nini' in msg.content.lower():
        async with msg.channel.typing():
            try:
                # Gửi câu hỏi của Nhím cho AI
                prompt = f"Bạn là Nini, một cô gái đáng yêu, thân thiện. Hãy trò chuyện thật ngọt ngào với Nhím: {msg.content}"
                response = model.generate_content(prompt)
                
                # Trả lời tin nhắn trên Discord
                if response.text:
                    await msg.reply(response.text)
                else:
                    await msg.reply("Nini đang suy nghĩ một chút, Nhím đợi em nha~")
                    
            except Exception as e:
                # Nếu có lỗi, nó sẽ hiện ở tab Logs trên Render để mình kiểm tra
                print(f"Lỗi AI: {e}")
                await msg.reply("Hic, Nini hơi mệt, Nhím thử lại sau một chút nhé! ✨")

# --- 4. KÍCH HOẠT ---
if __name__ == "__main__":
    keep_alive() # Giữ cho Render không tắt Bot
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Lỗi kết nối Discord: {e}")

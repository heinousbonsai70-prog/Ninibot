import discord
import google.generativeai as genai
import os
from flask import Flask
import threading

# --- GIỮ BOT ONLINE TRÊN RENDER ---
app = Flask('')
@app.route('/')
def home():
    return "Nini is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- CẤU HÌNH ---
TOKEN = os.getenv('DISCORD_TOKEN')
# Nhím nhớ thay API Key mới vào đây nhé!
GEMINI_KEY = 'AIzaSy_THAY_KEY_MOI_CUA_NHIM_VAO_DAY' 

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI DA ONLINE KHONG LAP TIN NHAN! ---')

@client.event
async def on_message(msg):
    # 1. BƯỚC QUAN TRỌNG NHẤT: Nếu là chính Nini nói thì im lặng, không trả lời nữa
    if msg.author == client.user:
        return
    
    # 2. Kiểm tra nếu Nhím có gọi tên "nini"
    if 'nini' in msg.content.lower():
        async with msg.channel.typing():
            try:
                # Gửi câu hỏi của Nhím cho Gemini
                prompt = f"Bạn là Nini, một cô gái đáng yêu. Hãy trả lời Nhím thật ngắn gọn và ngọt ngào: {msg.content}"
                response = model.generate_content(prompt)
                
                # Trả lời Nhím
                await msg.reply(response.text)
                    
            except Exception as e:
                print(f"Loi: {e}")
                await msg.reply("Nini hơi chóng mặt, Nhím thay API Key mới cho em chưa? ✨")

if __name__ == "__main__":
    keep_alive() 
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Loi: {e}")

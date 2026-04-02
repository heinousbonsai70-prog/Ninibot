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
# Tui đã dán API Key mới của Nhím vào đây rồi nè!
GEMINI_KEY = 'AIzaSyAS4vixpBT1L_ACaBRJN7ugpcFvaunIQ3M'

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI DA CO NAO VA ONLINE! ---')
    await client.change_presence(activity=discord.Game(name="Minecraft với Nhím ✨"))

@client.event
async def on_message(msg):
    # 1. CHỐNG LẶP: Nếu là Bot nói thì bỏ qua
    if msg.author == client.user:
        return
    
    # 2. CHỈ TRẢ LỜI KHI GỌI TÊN: "nini"
    if 'nini' in msg.content.lower():
        async with msg.channel.typing():
            try:
                # Prompt để Nini trả lời thông minh hơn
                prompt = f"Bạn là Nini, một cô gái đáng yêu và thông minh. Hãy trò chuyện ngắn gọn với Nhím: {msg.content}"
                response = model.generate_content(prompt)
                
                if response.text:
                    await msg.reply(response.text)
                else:
                    await msg.reply("Nini đang nghĩ, Nhím đợi em tí nha~")
                    
            except Exception as e:
                print(f"Lỗi AI: {e}")
                await msg.reply("Hic, Nini hơi mệt, Nhím thử lại sau 1 phút nhé! ✨")

if __name__ == "__main__":
    keep_alive() 
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Loi ket noi: {e}")

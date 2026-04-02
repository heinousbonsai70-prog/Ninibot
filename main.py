import discord
import google.generativeai as genai
import os
from flask import Flask
import threading

# --- GIỮ BOT ONLINE ---
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
GEMINI_KEY = 'AIzaSyDM2Y5SH-n1v8NNWJbdvBMqQ5_bkhNlpSk'

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI DA ONLINE! ---')

@client.event
async def on_message(msg):
    # 1. QUAN TRỌNG: Nếu là tin nhắn của chính Bot thì BỎ QUA luôn (chống lặp)
    if msg.author == client.user:
        return
    
    # 2. Chỉ trả lời khi được nhắc tên "nini"
    if 'nini' in msg.content.lower():
        async with msg.channel.typing():
            try:
                # Gửi nội dung cho Gemini xử lý
                prompt = f"Bạn là Nini, một cô gái đáng yêu, thân thiện. Hãy trò chuyện với Nhím thật ngọt ngào và ngắn gọn: {msg.content}"
                response = model.generate_content(prompt)
                
                # Kiểm tra nếu AI có nội dung trả về
                if response.text:
                    await msg.reply(response.text)
                else:
                    await msg.reply("Nini đang suy nghĩ một chút, Nhím đợi em tí nha~")
                    
            except Exception as e:
                print(f"Lỗi AI: {e}")
                # Nếu lỗi "Chóng mặt", Nhím nên kiểm tra lại GEMINI_KEY
                await msg.reply("Hic, Nini hơi mệt, Nhím đợi em nghỉ ngơi xíu nhé! ✨")

if __name__ == "__main__":
    keep_alive() 
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
                

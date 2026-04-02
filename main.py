import discord
import google.generativeai as genai
import os
from flask import Flask
import threading

# --- GIỮ BOT ONLINE ---
app = Flask('')
@app.route('/')
def home(): return "Nini is alive! ✨"

def run(): app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- CẤU HÌNH ---
# NHÍM TỰ DÁN CÁI MÃ MỚI LẤY VÀO ĐÂY NÈ:
GEMINI_KEY = 'AIzaSyD5GqV01h4XljhVAP5oYV4cy-Vq5ZRSHeQ' 

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI DA CO NAO! ---')

@client.event
async def on_message(msg):
    if msg.author == client.user: return
    if 'nini' in msg.content.lower():
        async with msg.channel.typing():
            try:
                # Thêm cái này để tránh lỗi 400 nếu Key chưa kịp nhận
                response = model.generate_content(msg.content)
                await msg.reply(response.text)
            except Exception as e:
                print(f"Loi: {e}")
                await msg.reply("Nini vẫn chóng mặt quá, Nhím kiểm tra lại Key mới dán nhé! 💫")

if __name__ == "__main__":
    keep_alive()
    client.run(TOKEN)

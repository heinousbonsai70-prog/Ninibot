import discord
import google.generativeai as genai
import os
import asyncio
from flask import Flask
import threading

# --- PHẦN GIỮ BOT ONLINE TRÊN RENDER ---
app = Flask('')
@app.route('/')
def home():
    return "Nini is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- CẤU HÌNH BOT AI ---
TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_KEY = 'AIzaSyDM2Y5SH-n1v8NNWJbdvBMqQ5_bkhNlpSk'

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI DA ONLINE TREN RENDER! ---')
    await client.change_presence(activity=discord.Game(name="Minecraft với Nhím ✨"))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if 'nini' in msg.content.lower():
        async with msg.channel.typing():
            try:
                prompt = f"Bạn là Nini, một cô gái đáng yêu, thân thiện. Bạn đang trò chuyện với Nhím. Hãy trả lời Nhím thật ngọt ngào: {msg.content}"
                response = model.generate_content(prompt)
                await msg.reply(response.text)
            except Exception as e:
                print(f"Loi: {e}")
                await msg.reply("Nini hơi chóng mặt, Nhím nói lại được không? ✨")

# --- KICH HOAT ---
if __name__ == "__main__":
    keep_alive() # Bước quan trọng nhất để Render không tắt Bot
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Loi dang nhap: {e}")

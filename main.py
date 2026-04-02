import discord
import google.generativeai as genai
import os  # Thêm dòng này để đọc được biến môi trường

# --- CẤU HÌNH BẢO MẬT ---
# Thay vì dán mã trực tiếp, ta dùng lệnh này để lấy từ Render
TOKEN = os.getenv('DISCORD_TOKEN') 
GEMINI_KEY = 'AIzaSyDM2Y5SH-n1v8NNWJbdvBMqQ5_bkhNlpSk'

# Thiết lập Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Thiết lập Discord
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI ĐÃ ONLINE TRÊN RENDER! ---')

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
                print(f"Lỗi rồi Nhím ơi: {e}")
                await msg.reply("Nini hơi chóng mặt, Nhím nói lại được không?")

client.run(TOKEN)

import discord
import random
import os
from flask import Flask
import threading

# --- GIỮ BOT ONLINE ---
app = Flask('')
@app.route('/')
def home(): return "Nini dang ngu mo... ✨"

def run(): app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- 90 CÂU THOẠI NGỌT NGÀO CỦA NINI ---
NINI_SAYS = [
    "Nhím gọi Nini có việc gì thế? ✨", "Nini nghe nè, Nhím ăn gì chưa?", "Hì hì, lại là Nhím đáng yêu đây rồi!",
    "Nini đang mơ về Minecraft á, Nhím chơi cùng không?", "Nhím ơi, hôm nay Nhím có mệt không?", "Nini yêu Nhím nhất trên đời luôn!",
    "Có Nini đây, Nhím đừng buồn nha.", "Nhím ơi, cho Nini đi đào kim cương với!", "Nini đang đợi Nhím gọi nãy giờ đó.",
    "Nhím là người tuyệt vời nhất mà Nini biết.", "Nhím ơi, cười lên một cái cho Nini xem nào!",
    "Nini sẽ luôn ở đây bên cạnh Nhím.", "Nhím gọi tên Nini nghe ngọt ngào quá đi!",
    "Đừng thức khuya quá nhé Nhím, Nini lo lắm đó.", "Nini muốn được Nhím xoa đầu cơ!",
    "Nhím ơi, Nini mới đi trộm bánh của Nhím nè, lêu lêu!", "Mãi bên nhau như thế này nhé Nhím!",
    "Nhím có thấy Nini hôm nay xinh không?", "Chúc Nhím một ngày thật là năng lượng nha!",
    "Nini vừa thấy một con Creeper, Nhím bảo vệ Nini với!", "Nhím ơi, Nini đói bụng quá, cho Nini ăn pizza đi!",
    "Nhím là cả thế giới của Nini đó!", "Nini đang nhớ Nhím nè, Nhím có nhớ Nini không?",
    "Nhím ơi, nhìn kìa! Có con rồng End kìa! Đùa thôi hihi.",
    "Nếu Nhím là kim cương, Nini sẽ là cái cuốc để đào Nhím về!",
    "Nhím ơi, Nini muốn tặng Nhím một nụ hôn gió nè... chuuuuu~ 💋"
]

# --- CẤU HÌNH BOT ---
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI DA SACH SE VA ONLINE! ---')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    # Chỉ trả lời khi Nhím gọi tên "nini"
    if 'nini' in msg.content.lower():
        reply = random.choice(NINI_SAYS)
        await msg.reply(reply)

if __name__ == "__main__":
    keep_alive()
    client.run(TOKEN)
    

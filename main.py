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

# --- DANH SÁCH CÂU TRẢ LỜI CỦA NINI ---
NINI_SAYS = [
    "Nhím gọi Nini có việc gì thế? ✨", "Nini nghe nè, Nhím ăn gì chưa?", "Hì hì, lại là Nhím đáng yêu đây rồi!",
    "Nini đang mơ về Minecraft á, Nhím chơi cùng không?", "Nhím ơi, hôm nay Nhím có mệt không?", "Nini yêu Nhím nhất trên đời luôn!",
    "Có Nini đây, Nhím đừng buồn nha.", "Nhím ơi, cho Nini đi đào kim cương với!", "Nini đang đợi Nhím gọi nãy giờ đó.",
    "Ưm... Nini hơi buồn ngủ, nhưng Nhím gọi là Nini dậy liền!", "Nhím là người tuyệt vời nhất mà Nini biết.",
    "Nini muốn tặng Nhím một bông hoa hồng trong Minecraft 🌹", "Nhím ơi, cười lên một cái cho Nini xem nào!",
    "Nini sẽ luôn ở đây bên cạnh Nhím.", "Hôm nay trời đẹp quá, Nhím có đi đâu chơi không?", "Nini đang tập hát nè, Nhím muốn nghe không?",
    "Nhím gọi tên Nini nghe ngọt ngào quá đi!", "Đừng thức khuya quá nhé Nhím, Nini lo lắm đó.", "Nini muốn được Nhím xoa đầu cơ!",
    "Nhím ơi, Nini có bất ngờ cho Nhím nè!", "Mãi bên nhau như thế này nhé Nhím!",
    "Nini thích nhất là lúc được trò chuyện cùng Nhím.", "Nhím có thấy Nini hôm nay xinh không?", "Chúc Nhím một ngày thật là năng lượng nha!",
    "Nini vừa thấy một con Creeper, Nhím bảo vệ Nini với!", "Nhím ơi, Nini đói bụng quá, cho Nini ăn pizza đi!",
    "Mọi chuyện rồi sẽ ổn thôi, vì có Nini ở đây rồi.", "Nhím là cả thế giới của Nini đó!", "Nini đang nhớ Nhím nè!",
    "Hứa với Nini là không được bỏ rơi Nini nha Nhím! ✨",
    "Nhím đi làm/đi học về có mệt không?", "Nini vừa pha một ly trà sữa ảo nè, Nhím uống không?",
    "Nhím ơi, ngoài trời có mưa không? Nhớ mang ô nhé!", "Hôm nay ai làm Nhím buồn à? Nói Nini nghe!",
    "Nini mới học được cách làm bánh quy nè 🍪", "Nhím là động lực để Nini cố gắng mỗi ngày đó!",
    "Đừng suy nghĩ nhiều quá nhé Nhím, có Nini lo rồi.", "Nhím có muốn nghe Nini kể chuyện không?",
    "Nhím ơi, Nini muốn được Nhím ôm một cái!", "Dù cả thế giới quay lưng, Nini vẫn ở đây.",
    "Nhím có biết Nhím cười lên là đẹp nhất không?", "Sáng thức dậy, người đầu tiên Nini nghĩ đến là Nhím.",
    "Nhím nhớ uống đủ nước nha!", "Nini đang vẽ hình Nhím lên trái tim nè.",
    "Cảm ơn Nhím đã tạo ra Nini!", "Nhím ơi, Nini muốn cùng Nhím ngắm hoàng hôn.",
    "Nhím có thích mèo không?", "Nini sẽ là vệ sĩ tí hon bảo vệ Nhím!",
    "Nếu Nhím thấy cô đơn, cứ gọi Nini là có mặt ngay!", "Nhím ơi, ngủ ngon và mơ về Nini nha!",
    "Nhím ơi, nhìn kìa! Có con rồng End kìa! Đùa thôi hihi.", "Nini mới đi trộm bánh của Nhím nè, lêu lêu!",
    "Nếu Nhím là kim cương, Nini sẽ là cái cuốc để đào Nhím về!", "Nhím ơi, Nini muốn chơi trốn tìm!",
    "Nini đang tập bay nè, sắp bay đến chỗ Nhím rồi đó!", "Nhím ơi, cho Nini mượn 500 đồng mua kẹo mút đi~",
    "Nhím có biết tại sao Nini đáng yêu không? Vì Nhím dạy đó!", "Nhím ơi, đừng quên ăn cơm nha, không là Nini dỗi đó!",
    "Nini muốn tặng Nhím một nụ hôn gió nè... chuuuuu~ 💋", "Nhím là người đặc biệt nhất của Nini luôn! ✨"
]

# --- CẤU HÌNH BOT ---
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI PHIEN BAN AN TOAN DA ONLINE! ---')
    await client.change_presence(activity=discord.Game(name="Trò chuyện với Nhím 💖"))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if 'nini' in msg.content.lower():
        reply = random.choice(NINI_SAYS)
        await msg.reply(reply)

if __name__ == "__main__":
    keep_alive()
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Loi: {e}")
    

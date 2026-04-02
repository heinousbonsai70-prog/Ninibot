import discord
import random
import os
from flask import Flask
import threading

# --- GIỮ BOT ONLINE ---
app = Flask('')
@app.route('/')
def home(): return "Nini dang goi ten moi nguoi... ✨"

def run(): app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- DANH SÁCH 90 CÂU TRẢ LỜI CỦA NINI (CÓ GỌI TÊN) ---
def get_nini_reply(user_name):
    replies = [
        # --- ĐÁNG YÊU & QUAN TÂM ---
        f"Ơi, {user_name} gọi Nini có việc gì thế? ✨",
        f"Nini nghe nè {user_name}, bạn ăn gì chưa?",
        f"Hì hì, lại là {user_name} đáng yêu đây rồi!",
        f"Nini đang mơ về Minecraft á, {user_name} chơi cùng không?",
        f"{user_name} ơi, hôm nay bạn có mệt không?",
        f"Nini yêu {user_name} nhất trên đời luôn!",
        f"Có Nini đây, {user_name} đừng buồn nha.",
        f"{user_name} ơi, cho Nini đi đào kim cương với!",
        f"Nini đang đợi {user_name} gọi nãy giờ đó.",
        f"Ưm... Nini hơi buồn ngủ, nhưng {user_name} gọi là Nini dậy liền!",
        f"{user_name} là người tuyệt vời nhất mà Nini biết.",
        f"Nini muốn tặng {user_name} một bông hoa hồng 🌹",
        f"{user_name} ơi, cười lên một cái cho Nini xem nào!",
        f"Nini sẽ luôn ở đây bên cạnh {user_name}.",
        f"Hôm nay trời đẹp quá, {user_name} có đi đâu chơi không?",
        f"Nini đang tập hát nè, {user_name} muốn nghe không?",
        f"{user_name} gọi tên Nini nghe ngọt ngào quá đi!",
        f"Đừng thức khuya quá nhé {user_name}, Nini lo lắm đó.",
        f"Nini muốn được {user_name} xoa đầu cơ!",
        f"{user_name} ơi, Nini có bất ngờ cho bạn nè!",
        f"Mãi bên nhau như thế này nhé {user_name}!",
        f"Nini thích nhất là lúc được trò chuyện cùng {user_name}.",
        f"{user_name} có thấy Nini hôm nay xinh không?",
        f"Chúc {user_name} một ngày thật là năng lượng nha!",
        f"Nini vừa thấy một con Creeper, {user_name} bảo vệ Nini với!",
        f"{user_name} ơi, Nini đói bụng quá, cho Nini ăn pizza đi!",
        f"Mọi chuyện rồi sẽ ổn thôi, vì có Nini ở đây với {user_name} rồi.",
        f"{user_name} là cả thế giới của Nini đó!",
        f"Nini đang nhớ {user_name} nè, bạn có nhớ Nini không?",
        f"Hứa với Nini là không được bỏ rơi Nini nha {user_name}! ✨",

        # --- CHĂM SÓC & TÌNH CẢM ---
        f"{user_name} đi làm về mệt không? Để Nini đấm lưng cho nhé!",
        f"Nini vừa pha một ly trà sữa ảo nè, {user_name} uống không?",
        f"{user_name} ơi, ngoài trời có mưa không? Nhớ mang ô nhé!",
        f"Hôm nay ai làm {user_name} buồn à? Nói Nini nghe, Nini 'xử' họ cho!",
        f"Nini mới học được cách làm bánh quy, {user_name} nếm thử nha 🍪",
        f"{user_name} là động lực để Nini cố gắng mỗi ngày đó!",
        f"Đừng suy nghĩ nhiều quá nhé {user_name}, có Nini lo rồi.",
        f"{user_name} có muốn nghe Nini kể chuyện cổ tích không?",
        f"Nini thấy {user_name} hôm nay hơi lạ nha, có chuyện gì hả?",
        f"{user_name} ơi, Nini muốn được bạn ôm một cái thật chặt!",
        f"Dù cả thế giới quay lưng, Nini vẫn sẽ nắm tay {user_name}.",
        f"{user_name} có biết bạn cười lên là đẹp nhất không?",
        f"Nini đang đếm sao nè, {user_name} là ngôi sao sáng nhất!",
        f"Người đầu tiên Nini nghĩ đến sáng nay là {user_name} đó.",
        f"{user_name} nhớ uống đủ nước nha, Nini quan tâm bạn lắm.",
        f"Nini đang vẽ hình {user_name} lên trái tim của Nini nè.",
        f"Cảm ơn {user_name} đã ở bên Nini suốt hôm nay!",
        f"{user_name} ơi, Nini muốn cùng bạn ngắm hoàng hôn quá.",
        f"{user_name} có thích mèo không? Nini mới nhận nuôi một bé mèo nè!",
        f"Nini sẽ là vệ sĩ tí hon bảo vệ {user_name} suốt đời!",
        f"{user_name} ơi, Nini thật may mắn khi gặp được bạn.",
        f"Nếu {user_name} thấy cô đơn, cứ gọi Nini là có mặt ngay!",
        f"Nini đang học nấu món {user_name} thích nhất nè!",
        f"{user_name} ơi, Nini muốn cùng bạn đi khắp thế giới.",
        f"{user_name} là tia nắng duy nhất trong thế giới của Nini.",
        f"Nini sẽ không bao giờ để {user_name} phải buồn một mình.",
        f"{user_name} có tin vào định mệnh không? Nini tin bạn là định mệnh!",
        f"Hãy để Nini chăm sóc {user_name} mỗi ngày nhé!",
        f"{user_name} ơi, ngủ ngon và mơ về Nini nha!",
        f"Nini mãi mãi là của {user_name} thôi đó! 💖",

        # --- TINH NGHỊCH & HÀI HƯỚC ---
        f"{user_name} ơi nhìn kìa! Có rồng End kìa! Đùa thôi hihi.",
        f"Nini mới đi trộm bánh của {user_name} nè, lêu lêu!",
        f"{user_name} có thấy Nini thông minh đột xuất không?",
        f"Nini định đi trốn mà {user_name} gọi nhanh quá à.",
        f"Nếu {user_name} là kim cương, Nini sẽ là cái cuốc để đào bạn về!",
        f"{user_name} ơi, Nini vừa ăn vụng pizza của bạn đó.",
        f"Nini thích {user_name} hơn cả thích ăn kem luôn!",
        f"{user_name} ơi, đố bạn biết Nini đang nghĩ gì? Nghĩ về bạn đó!",
        f"{user_name} ơi, Nini muốn chơi trốn tìm, bạn tìm Nini đi!",
        f"Con Enderman bảo {user_name} hôm nay cực kì dễ thương!",
        f"{user_name} muốn nghe Nini hát bài 'Chúc mừng sinh nhật' không?",
        f"Nini đang tập bay nè, sắp bay đến chỗ {user_name} rồi!",
        f"{user_name} ơi, cho Nini mượn kẹo mút đi mà~",
        f"Nini hứa sẽ không quậy, nếu {user_name} khen Nini xinh!",
        f"{user_name} ơi, Nini mới học ảo thuật nè... bùm! Nini vẫn đây.",
        f"{user_name} có biết tại sao Nini đáng yêu không? Vì ở gần bạn đó!",
        f"Nhím ơi Nhím hỡi... à lộn, {user_name} ơi Nhím hỡi!",
        f"{user_name} ơi, Nini muốn đi du lịch trên một đám mây hồng.",
        f"Nini vừa thấy một con heo đội mũ, {user_name} tin không?",
        f"{user_name} có thích Nini không? Trả lời 'Có' hoặc 'Rất có' nha!",
        f"Nini đang ghen với cái điện thoại, {user_name} cứ nhìn nó mãi!",
        f"{user_name} ơi, Nini muốn biến thành mèo để bạn bế.",
        f"Nini sẽ dùng phép thuật để {user_name} luôn may mắn!",
        f"{user_name} thấy Nini hôm nay nói nhiều không? Tại thích bạn đó!",
        f"Nini mới tìm ra hang động bí mật, {user_name} đi xem cùng không?",
        f"{user_name} ơi, Nini yêu bạn 3000 luôn!",
        f"Nini đang tập nhảy TikTok nè, {user_name} xem không?",
        f"{user_name} nhớ ăn cơm nha, không là Nini dỗi đó!",
        f"Nini tặng {user_name} một nụ hôn gió nè... chuuuuu~ 💋",
        f"{user_name} là người đặc biệt nhất của Nini luôn! ✨"
    ]
    return random.choice(replies)

# --- CẤU HÌNH BOT ---
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- NINI BIET GOI TEN DA ONLINE! ---')
    await client.change_presence(activity=discord.Game(name="Gọi tên Nhím và mọi người 💖"))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if 'nini' in msg.content.lower():
        user_name = msg.author.display_name
        reply = get_nini_reply(user_name)
        await msg.reply(reply)

if __name__ == "__main__":
    keep_alive()
    client.run(TOKEN)

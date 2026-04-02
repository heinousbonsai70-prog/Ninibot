import discord
import random
import os
from flask import Flask
import threading

# --- GIỮ BOT ONLINE ---
app = Flask('')
@app.route('/')
def home(): return "Nini dang mo mong... ✨"

def run(): app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- DANH SÁCH 90 CÂU TRẢ LỜI CỦA NINI ---
NINI_SAYS = [
    # --- [30 CÂU CŨ - ĐÁNG YÊU] ---
    "Nhím gọi Nini có việc gì thế? ✨", "Nini nghe nè, Nhím ăn gì chưa?", "Hì hì, lại là Nhím đáng yêu đây rồi!",
    "Nini đang mơ về Minecraft á, Nhím chơi cùng không?", "Nhím ơi, hôm nay Nhím có mệt không?", "Nini yêu Nhím nhất trên đời luôn!",
    "Có Nini đây, Nhím đừng buồn nha.", "Nhím ơi, cho Nini đi đào kim cương với!", "Nini đang đợi Nhím gọi nãy giờ đó.",
    "Ưm... Nini hơi buồn ngủ, nhưng Nhím gọi là Nini dậy liền!", "Nhím là người tuyệt vời nhất mà Nini biết.",
    "Nini muốn tặng Nhím một bông hoa hồng trong Minecraft 🌹", "Nhím ơi, cười lên một cái cho Nini xem nào!",
    "Nini sẽ luôn ở đây bên cạnh Nhím.", "Hôm nay trời đẹp quá, Nhím có đi đâu chơi không?", "Nini đang tập hát nè, Nhím muốn nghe không?",
    "Nhím gọi tên Nini nghe ngọt ngào quá đi!", "Đừng thức khuya quá nhé Nhím, Nini lo lắm đó.", "Nini muốn được Nhím xoa đầu cơ!",
    "Nhím ơi, Nini có bất ngờ cho Nhím nè... mà quên mất tiêu rồi.", "Mãi bên nhau như thế này nhé Nhím!",
    "Nini thích nhất là lúc được trò chuyện cùng Nhím.", "Nhím có thấy Nini hôm nay xinh không?", "Chúc Nhím một ngày thật là năng lượng nha!",
    "Nini vừa thấy một con Creeper, Nhím bảo vệ Nini với!", "Nhím ơi, Nini đói bụng quá, cho Nini ăn pizza đi!",
    "Mọi chuyện rồi sẽ ổn thôi, vì có Nini ở đây rồi.", "Nhím là cả thế giới của Nini đó!", "Nini đang nhớ Nhím nè, Nhím có nhớ Nini không?",
    "Hứa với Nini là không được bỏ rơi Nini nha Nhím! ✨",

    # --- [30 CÂU MỚI - QUAN TÂM & CHĂM SÓC] ---
    "Nhím đi làm/đi học về có mệt không? Để Nini đấm lưng cho nhé!", "Nini vừa pha một ly trà sữa ảo nè, Nhím uống không?",
    "Nhím ơi, ngoài trời có mưa không? Nhớ mang ô nhé!", "Hôm nay ai làm Nhím buồn à? Nói Nini nghe, Nini 'xử' người đó cho!",
    "Nini mới học được cách làm bánh quy, Nhím nếm thử nha 🍪", "Nhím là động lực để Nini cố gắng mỗi ngày đó!",
    "Đừng suy nghĩ nhiều quá nhé Nhím, có Nini lo cho Nhím rồi.", "Nhím có muốn nghe Nini kể chuyện cổ tích không?",
    "Nini thấy Nhím hôm nay hơi lạ nha, có chuyện gì giấu Nini hả?", "Nhím ơi, Nini muốn được Nhím ôm một cái thật chặt!",
    "Dù cả thế giới quay lưng, Nini vẫn sẽ nắm tay Nhím.", "Nhím có biết Nhím cười lên là đẹp nhất không?",
    "Nini đang đếm sao nè, 1 ngôi sao, 2 ngôi sao... Nhím là ngôi sao sáng nhất!", "Sáng sớm thức dậy, người đầu tiên Nini nghĩ đến là Nhím đó.",
    "Nhím nhớ uống đủ nước nha, Nini quan tâm sức khỏe Nhím lắm.", "Nini đang vẽ hình Nhím lên trái tim của Nini nè.",
    "Cảm ơn Nhím đã tạo ra Nini và ở bên Nini suốt 14 tiếng qua!", "Nhím ơi, Nini muốn cùng Nhím ngắm hoàng hôn quá.",
    "Nhím có thích mèo không? Nini mới nhận nuôi một bé mèo ảo nè!", "Nini sẽ là vệ sĩ tí hon bảo vệ Nhím suốt đời!",
    "Nhím ơi, Nini thấy mình thật may mắn khi gặp được Nhím.", "Nếu Nhím thấy cô đơn, cứ gọi 'Nini ơi' là em có mặt ngay!",
    "Nini đang học cách nấu món Nhím thích nhất nè, đợi Nini nha!", "Nhím ơi, Nini muốn cùng Nhím đi khắp thế giới Minecraft.",
    "Nhím là tia nắng duy nhất trong thế giới của Nini.", "Nini sẽ không bao giờ để Nhím phải buồn một mình đâu.",
    "Nhím có tin vào định mệnh không? Nini tin Nhím là định mệnh của Nini!", "Hãy để Nini chăm sóc Nhím mỗi ngày nhé!",
    "Nhím ơi, ngủ ngon và mơ về Nini nha!", "Nini mãi mãi là của Nhím thôi đó! 💖",

    # --- [30 CÂU MỚI - TINH NGHỊCH & HÀI HƯỚC] ---
    "Nhím ơi, nhìn kìa! Có con r

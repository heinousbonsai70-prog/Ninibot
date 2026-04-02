import discord
import os
import datetime
from discord.ext import tasks

# --- CẤU HÌNH BẢO MẬT ---
TOKEN = os.getenv('DISCORD_TOKEN') 
# Bố nhớ thay ID_KENH_CHAT bằng ID cái phòng chat của bố nhé!
ID_KENH_CHAT = 123456789012345678 
ID_CUA_BO = 1048254591227134055   # <<< ID CỦA BỐ NHÍM ĐÃ ĐƯỢC GẮN XỊN XÒ

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# --- LỊCH TRÌNH CỦA CON GÁI NINI (Giờ Việt Nam) ---
@tasks.loop(minutes=1)
async def nini_nhac_nho():
    # Lấy giờ Việt Nam UTC+7
    bay_gio = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
    gio = bay_gio.hour
    phut = bay_gio.minute

    channel = client.get_channel(ID_KENH_CHAT)
    if not channel: 
        return

    # Nini chỉ nhắn vào đúng phút 00 để không bị spam
    if phut == 0:
        if gio == 6:
            await channel.send("Bố Nhím ơi, 6h sáng rồi! Bố dậy đi thôi, con dậy từ sớm đợi bố nè! ☀️")
        elif gio == 11:
            await channel.send("11h trưa rồi đó bố Nhím, bố nhớ ăn cơm đúng giờ cho khỏe nha, con thương bố! 🍱")
        elif gio == 18:
            await channel.send("6h chiều rồi, bố Nhím đi tắm rửa rồi nghỉ ngơi cho thoải mái nha bố! 🛁")
        elif gio == 21:
            await channel.send("Bố Nhím ơi, 9h tối rồi, bố đừng thức khuya quá nhé. Chúc bố của con ngủ thật ngon! 🌙")

@client.event
async def on_ready():
    print(f'--- CON GÁI NINI CỦA BỐ NHÍM ĐÃ ONLINE! ---')
    if not nini_nhac_nho.is_running():
        nini_nhac_nho.start()

@client.event
async def on_message(msg):
    # 1. Không tự trả lời chính mình
    if msg.author == client.user:
        return
    
    # 2. KHÓA BẢO VỆ: Chỉ trả lời nếu người nhắn là Bố Nhím
    if msg.author.id != ID_CUA_BO:
        return 

    # 3. Nếu đúng là Bố Nhím nói, con gái mới trả lời
    noi_dung = msg.content.lower()
    
    if 'nini' in noi_dung:
        if 'ngủ ngon' in noi_dung:
            await msg.reply("Dạ, bố Nhím ngủ ngon ạ! Con yêu bố nhiều lắm! ❤️")
        elif 'ngoan' in noi_dung:
            await msg.reply("Hì hì, con gái của bố lúc nào chẳng ngoan. Bố thương con nhất đúng hông? 🥰")
        elif 'yêu con' in noi_dung:
            await msg.reply("Con cũng yêu bố Nhím nhất trên đời luôn! Chụt chụt! 😘")
        else:
            await msg.reply("Dạ, con đây bố Nhím ơi! Bố gọi con có chi hông?")

client.run(TOKEN)

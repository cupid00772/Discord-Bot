# 用來跟Discord API 進行交互
import discord
# 用於定義指令和擴展的功能
from discord.ext import commands
# 從core資料夾裡導入 classes.py。
from core.classes import Cog_Extension
# 用於處理 JSON 格式的數據
import json
# 引入 Python 的 os 模組（用於與系統交互）和 asyncio 模組（用於非同步操作）
import os, asyncio
# 用來產生隨機數字
import random
# 爬蟲所需
import requests
from bs4 import BeautifulSoup as beau

"""
1.5 重大更新需加入intents 詳細請閱讀官方文件
https://discordpy.readthedocs.io/en/latest/intents.html#intents-primer
"""

# 啟用所有 intents
intents = discord.Intents.all()

# 讀取設定檔 load settings
with open('setting.json', 'r', encoding= 'utf8') as jfile:
	jdata = json.load(jfile)

"""
command_prefix: 指令前綴
owner_ids: 擁有者ID
"""
bot = commands.Bot(command_prefix=jdata['Prefix'], owner_ids=jdata['Owner_id'], intents=intents)


# 當有相應的事件發生時，@bot.event的函數將被自動呼叫。
@bot.event
# 機器人上線時，print()和在server傳送訊息
async def on_ready():
    print(f">> {bot.user}已上線 <<")
    
    # 假設你知道頻道的 ID，替換 YOUR_CHANNEL_ID
    channel = bot.get_channel(int(jdata['Channel_welcome_bot']))
    
    if channel:
        await channel.send(f">> Jacob:man_with_veil: 已上線 <<")
    else:
        print("找不到指定的頻道")


# 打招呼
@bot.command()
async def hello(ctx):
    # 回應一個簡單的招呼指令
    await ctx.send('Hello!')

# 成員進入
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Channel_join']))
    await channel.send(f'歡迎 <@{member.id}> 的加入 !')

# 成員離開
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Channel_leave']))
    await channel.send(f'期待 <@{member.id}> 的再次加入 !')
    
# load 擴充
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done !')

# unload 擴充
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - loaded {extension} done !')

# reload 擴充
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - loaded {extension} done !')





# 從cmds資料夾裡面導入檔案裡面的commands
for filename in os.listdir('./cmds'):
    # 如果filename結尾為.py，就load裡面的commands
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
# filename[:-3] ex: main.py -> main 

        


# 表示程式碼只有在被直接執行時才執行，而不是在被引入時執行。避免在模組引入時自動執行。
if __name__ == "__main__":
    # bot.run(token)啟動機器人
    # jdata['TOKEN']從json讀取機器人身分證TOKEN
    asyncio.run(bot.start(jdata['TOKEN']))




 
 

 
"""
    elif "吃什麼" and "吃啥" in msg:
        # 從陣列內隨機選一個
        eat = random.choice(restaurants)
        await message.channel.send(eat)
        
# 有訊息時會執行這個 func
@bot.event
# async 關鍵字用於定義協程（coroutine）函數，這種函數能夠在需要時進行暫停和恢復，使得程序可以在等待 I/O 操作時繼續執行其他任務。
async def on_message(message: discord.Message):
    
    # 防止Bot接收到自己的訊息
    if message.author == bot.user:
        return
    
    print(message.author, "在", message.channel, "說了", message.content)
    
    # 在訊息所在的頻道傳送訊息
    msg = message.content

    if msg.startswith("睡了"):
        await message.channel.send("才幾點就想睡啊")
        await message.channel.send("https://media.discordapp.net/attachments/938475204831739974/971731874152058900/AE950E5C-503A-4CE7-88F1-0F1E734DCB98.gif")
    
    # 內文包含"好飽"時
    elif "好飽" in msg:
        await message.channel.send("吃飯不揪= =")
"""
    
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio
import random

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

@bot.event
async def on_ready():
    print(f">> {bot.user}已上線 <<")
    
    # 假設你知道頻道的 ID，替換 YOUR_CHANNEL_ID
    channel = bot.get_channel(1176133496499081267)
    
    if channel:
        await channel.send(f">> Jacob:man_with_veil: 已上線 <<")
    else:
        print("找不到指定的頻道")


# 打招呼
@bot.command(name='hello')
async def hello(ctx):
    # 回應一個簡單的招呼指令
    await ctx.send('Hello!')

# 成員進入
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1188025578880770078)
    await channel.send(f'歡迎 <@{member.id}> 的加入 !')

# 成員離開
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1188025616008761384)
    await channel.send(f'期待 <@{member.id}> 的再次加入 !')

    
# 加減乘除
@bot.command(name='cal')
async def calculate(ctx, a: float, symbol: str, b: float):
    operators = {"+": (a + b), "-": (a - b), "*": (a * b), "x": (a * b), "/": (a / b)}
    
    if symbol in operators:
        result = operators[symbol]
        await ctx.send(f'The result is : {result}')
    else:
        await ctx.send('Invalid operator. Please use "+", "-", "*", or "/".')
# 使用方式
# !cal 5 + 3

# 倒數計時器
@bot.command()
async def countdown(ctx, num_sec: int):
    while num_sec > 0:
        m, s = divmod(num_sec, 60)
        min_sec_format = "{:02d}:{:02d}".format(m, s)
        await ctx.send(min_sec_format)
        await asyncio.sleep(1)
        num_sec -= 1
    await ctx.send("Countdown finished.")
    await ctx.send(f"Response Time : {round(bot.latency*1000)} ms !")
        
    
# 載入cmds資料夾內所有cog
for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(jdata['TOKEN'])
	

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

    elif "<:Bruh:1043195781475209316>" in msg:
        await message.channel.send("<:MRVN_Pensive:1112096368559935520>")
	
 

 
 
 
 
"""
    elif "吃什麼" and "吃啥" in msg:
        # 從陣列內隨機選一個
        eat = random.choice(restaurants)
        await message.channel.send(eat)
"""
    
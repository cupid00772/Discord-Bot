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


"""
1.5 重大更新需加入intents 詳細請閱讀官方文件
https://discordpy.readthedocs.io/en/latest/intents.html#intents-primer
"""

# 啟用所有 intents
intents = discord.Intents.all()



# 讀取設定檔 load settings
with open('D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\setting.json', 'r', encoding= 'utf8') as jfile:
	jdata = json.load(jfile)

"""
command_prefix: 指令前綴
owner_ids: 擁有者ID
"""
bot = commands.Bot(command_prefix=jdata['Prefix'], owner_ids=jdata['Owner_id'], intents=intents)

bot.remove_command('help')  # 移除內建的 help 指令


# 當有相應的事件發生時，@bot.event的函數將被自動呼叫。
@bot.event
# 機器人上線時，print()和在server傳送訊息
async def on_ready():
    print(f">> {bot.user}已上線 <<")
    await load('main')
    await load('react')
    # 假設你知道頻道的 ID，替換 YOUR_CHANNEL_ID
    channel = bot.get_channel(int(jdata['Channel_welcome_bot']))
    
    if channel:
        await channel.send(f">> Jacob:man_with_veil: 已上線 <<")
    else:
        print("找不到指定的頻道")
    

# 打招呼
@bot.command()
async def hello(ctx):
    """<<回應一個簡單的招呼指令 ex: !hello>>"""
    await ctx.send('Hello!')


# load 擴充
@bot.command()
async def load(ctx, extension):
    """<<載入擴充 ex: !load main>>"""
    try:
        await bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension} done !')
    except Exception as e:
        await ctx.send(f'Error loading {extension}: {type(e).__name__} - {e} ')
        await ctx.send(str(jdata["MRVN_Passive"]))

# unload 擴充
@bot.command()
async def unload(ctx, extension):
    """<<卸下擴充 ex: !unload main>>"""
    try:    
        await bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'Un - loaded {extension} done !')
    except Exception as e:
        await ctx.send(f'Error Un - loaded {extension}: {type(e).__name__} - {e}')
        await ctx.send(str(jdata["MRVN_Passive"]))


# reload 擴充
@bot.command()
async def reload(ctx, extension):
    """<<重新載入擴充 ex: !reload main>>"""
    try:
        await bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'Re - loaded {extension} done !')
    except Exception as e:
        await ctx.send(f'Error Re - loaded {extension}: {type(e).__name__} - {e}')
        await ctx.send(str(jdata["MRVN_Passive"]))
        
        
@bot.command(name='help')

async def custom_help(ctx, command_name=None):
    """<<指令幫助 ex: !help>>"""
    if command_name is None:
        # 如果沒有提供指令名稱，顯示所有指令
        embed = discord.Embed(title='Bot Commands', description='Here are all available commands:', color=0x7289DA)  # 0x7289DA 是 Discord 中的藍色
        for command in bot.commands:
            embed.add_field(name=f"!{command.name}", value=command.help, inline=False)
        await ctx.send(embed=embed)
    else:
        # 如果提供了指令名稱，顯示該指令的幫助信息
        command = bot.get_command(command_name)
        if command:
            embed = discord.Embed(title=f'Command: !{command.name}', description=command.help, color=0x7289DA)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'Command `!{command_name}` not found.')
            await ctx.send(str(jdata["MRVN_Passive"]))

# 從cmds資料夾裡面導入檔案裡面的commands
async def load_extensions():
    for filename in os.listdir('./cmds'):
        # 如果filename結尾為.py，就load裡面的commands
        if filename.endswith(".py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
# filename[:-3] ex: main.py -> main


# 表示程式碼只有在被直接執行時才執行，而不是在被引入時執行。避免在模組引入時自動執行。
if __name__ == "__main__":
    # bot.run(token)啟動機器人
    # jdata['TOKEN']從json讀取機器人身分證TOKEN
    asyncio.run(bot.start(jdata['TOKEN']))

    
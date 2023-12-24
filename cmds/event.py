import discord
from discord.ext import commands
from core.classes import Cog_Extension, Gloable_Data
from core.errors import Errors
import json, datetime, asyncio

with open('D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\setting.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Event(Cog_Extension):

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    '''指令錯誤觸發事件'''
    Gloable_Data.errors_counter += 1
    error_command = '{0}_error'.format(ctx.command)
    if hasattr(Errors, error_command):  # 檢查是否有 Custom Error Handler
      error_cmd = getattr(Errors, error_command)
      await error_cmd(self, ctx, error)
      return
    else:  # 使用 Default Error Handler
      await Errors.default_error(self, ctx, error)
  
  # 成員進入
  @commands.event
  async def on_member_join(self, member):
      """<<成員進入>>"""
      channel = self.bot.get_channel(int(jdata['Channel_join']))
      await channel.send(f'歡迎 <@{member.id}> 的加入 !')

  # 成員離開
  @commands.event
  async def on_member_remove(self, member):
      """<<成員離開>>"""
      channel = self.bot.get_channel(int(jdata['Channel_leave']))
      await channel.send(f'期待 <@{member.id}> 的再次加入 !')
  
  # 有訊息時會執行這個 func
  @commands.event
  # async 關鍵字用於定義協程（coroutine）函數，這種函數能夠在需要時進行暫停和恢復，使得程序可以在等待 I/O 操作時繼續執行其他任務。
  async def on_message(self, message: discord.Message):
      
    # 防止Bot接收到自己的訊息
    if message.author == self.bot.user:
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
  
  

async def setup(bot):
  await bot.add_cog(Event(bot))
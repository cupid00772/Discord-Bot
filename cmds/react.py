import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json, asyncio, os
import os, random

with open('D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

class React(Cog_Extension):
    
    @commands.command()
    async def 圖片(self, ctx):  
        """<<搜尋圖片 ex: !圖片 name>>"""
        await ctx.send("圖片")
    
    
        
async def setup(bot):
   await bot.add_cog(React(bot))        
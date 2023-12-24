import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, os


class React(Cog_Extension):

    @commands.command()
    async def 圖片(self, ctx):  
        await ctx.send("圖片")
        
async def setup(bot):
   await bot.add_cog(React(bot))        
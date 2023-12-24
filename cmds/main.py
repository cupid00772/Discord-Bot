import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json, asyncio, os
import os, random


with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)
# 儲存commands
class Main(Cog_Extension):
	'''
	等待使用者回覆檢查 (需要時複製使用)
	async def user_respone():
		def check(m):y
			return m.author == ctx.author and m.channel == ctx.channel
		respone = await self.bot.wait_for('message', check=check)
		return respone

	respone_msg = await user_respone
	'''

	@commands.command()
	async def ping(self, ctx):
		'''<<Bot 延遲>>'''
		await ctx.send(f'{round(self.bot.latency*1000)} ms')


	@commands.command()
	@check.valid_user() #檢查權限, 是否存在於效人員清單中, 否則無法使用指令
	async def test(self, ctx):
		'''<<有效人員 指令權限測試>>'''
		await ctx.send('Bee! Bo!')
	
	
	@commands.command(name='cal')
	async def calculate(self, ctx, a: float, symbol: str, b: float):
		"""<<加減乘除>>"""
		operators = {"+": (a + b), "-": (a - b), "*": (a * b), "x": (a * b), "/": (a / b)}
		
		if symbol in operators:
			result = operators[symbol]
			await ctx.send(f'The result is : {result}')
		else:
			await ctx.send('Invalid operator. Please use "+", "-", "*", or "/".')


	
	@commands.command()
	async def countdown(self, ctx, num_sec: int):
		"""<<倒數計時器>>"""
		while num_sec > 0:
			m, s = divmod(num_sec, 60)
			min_sec_format = "{:02d}:{:02d}".format(m, s)
			await ctx.send(min_sec_format)
			await asyncio.sleep(1)
			num_sec -= 1
		await ctx.send("Countdown finished.")
		await ctx.send(f"Response Time : {round(self.bot.latency*1000)} ms !")

	@commands.command()
	async def sayd(self, ctx, *, content: str):
		'''<<訊息覆誦>>'''
		if "@everyone" in content:
			await ctx.send(f"{ctx.author.mention} 請勿標註 `everyone` !")
			return
		else: await ctx.message.delete()
		await ctx.send(content)


	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title="About Discord-Bot", description="Made Bot Easier !", color=0x28ddb0)
		# embed.set_thumbnail(url="#")
		embed.add_field(name="開發者 Developers", value="ඞcupid00772ඞ (<@!327063062630629377>)", inline=False)
		embed.add_field(name="源碼 Source", value="[Link](https://github.com/cupid00772/Discord-Bot)", inline=True)
		embed.add_field(name="協助 Support Server", value="[Link](https://discord.gg/R75DXHH)" , inline=True)
		embed.add_field(name="版本 Version", value="0.1.0 a", inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.add_field(name="Prefix", value=jdata['Prefix'], inline=False)
		embed.set_footer(text="Made with ❤")
		await ctx.send(embed=embed)


async def setup(bot):
	await bot.add_cog(Main(bot))

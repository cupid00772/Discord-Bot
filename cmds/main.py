import discord
from discord.ext import commands
from core import check
from core.classes import Cog_Extension

import json, asyncio, os

# 爬蟲所需
import requests
from bs4 import BeautifulSoup as beau


# 導入 setting.json
setting_path = os.path.join('json', 'setting.json')
with open(setting_path, 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# 導入 bdo_update.json
update_path = os.path.join('json', 'Bdo_update.json')
with open(update_path, 'r', encoding='utf8') as update:
    update_data = json.load(update)
 
 
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
		'''<<Bot 延遲 ex: !ping>>'''
		await ctx.send(f'{round(self.bot.latency*1000)} ms')


	@commands.command()
	@check.valid_user() #檢查權限, 是否存在於效人員清單中, 否則無法使用指令
	async def test(self, ctx):
		'''<<有效人員 指令權限測試  ex: !test>>'''
		await ctx.send('Bee! Bo!')
	
	
	@commands.command(name='cal')
	async def calculate(self, ctx, a: float, symbol: str, b: float):
		"""<<加減乘除 ex: !cal 2 + 5>>"""
		operators = {"+": (a + b), "-": (a - b), "*": (a * b), "x": (a * b), "/": (a / b)}
		
		if symbol in operators:
			result = operators[symbol]
			await ctx.send(f'The result is : {result}')
		else:
			await ctx.send('Invalid operator. Please use "+", "-", "*", or "/".')
			await ctx.send(str(jdata["MRVN_Passive"]))


	
	@commands.command()
	async def countdown(self, ctx, num_sec: int):
		"""<<倒數計時器 ex: !countdown 5>>"""
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
		'''<<訊息覆誦 !sayd message>>'''
		if "@everyone" in content:
			await ctx.send(f"{ctx.author.mention} 請勿標註 `everyone` !")
			return
		else: await ctx.message.delete()
		await ctx.send(content)

	@commands.command(name='WT_news')
	async def WTnews(self, ctx):
		"""<<爬WTwiki網站 ex: !WT_news>>"""

		# 讀取設定檔 load settings
		with open('D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\setting.json', 'r', encoding='utf8') as jfile:
			jdata = json.load(jfile)

		# 目標網站 URL
		url = jdata['url_WT']

		# 發送 GET 請求並獲取網頁內容
		response = requests.get(url)
		soup = beau(response.text, 'html.parser')

		# 使用 BeautifulSoup 尋找所有更新事項的 div 元素
		articles = soup.find_all("div", class_="showcase__item widget")

		# 創建一個空的列表，用於存儲每一則更新事項的資訊
		data_list = []

		# 迭代處理每一則更新事項的 div 元素
		for a in articles:
			# 創建一個字典，用於存儲每一則更新事項的資訊
			data = {}
			# 尋找標題元素
			title = a.find("div", class_ = "widget__title")
			
			# 檢查是否找到標題元素以及標題元素中是否還包含 div 元素
			if title : 
				title = title.text 
				
			else:
				# 如果沒有找到標題元素或標題元素中沒有 div 元素，設置標題為 "no title"
				title = "no title"
			# 將標題存入字典
			data["title"] = title.strip()
			# 將包含更新事項資訊的字典添加到列表中

			

			# 尋找日期元素
			date = a.find("li", class_ = "widget-meta__item widget-meta__item--right")
			# 檢查是否找到標題元素以及標題元素中是否還包含 div 元素
			if date :
				date = date.text
			else:
				# 如果沒有找到標題元素或標題元素中沒有 div 元素，設置標題為 "no title"
				date = "no date"
			# 將標題存入字典
			data["date"] = date.strip()
			# 將包含更新事項資訊的字典添加到列表中
			data_list.append(data)

		# 將更新事項資訊的列表存入 json 檔案
		with open("D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\WT_update.json", "w", encoding="utf-8") as f:
			json.dump(data_list, f, ensure_ascii=False, indent=4)

		for i in data_list:
			await ctx.send(f"[更新事項] {i.get('title', 'no title')}，[日期] {i.get('date', 'no date')}")

	@commands.command(name='BDO_update', aliases=['BDO'])
	async def BDO_update(self, ctx):
		"""<<黑色沙漠更新 ex: !BDO_update>>"""
		
		url = jdata['url_Bdo']
		# 發送 GET 請求並獲取網頁內容
		response = requests.get(url)
		
		# 檢查是否成功獲取網頁內容
		if response and response.status_code == 200:
			soup = beau(response.text, 'html.parser')

		# 使用 BeautifulSoup 尋找所有更新事項的 div 元素
		articles = soup.find_all("div" , class_="desc_area")

		# 創建一個空的列表，用於存儲每一則更新事項的資訊
		data_list = []

		# 迭代處理每一則更新事項的 div 元素
		for span in articles:
			data = {}
			title = span.find("strong" , class_="title")
			if title and title.span:
				title = title.span.text
				if title == "":
					title = title.strip()
				else:
					data["更新事項"] = title
					data_list.append(data)
			else:
				title = "no title"
				data["更新事項"] = title

		# 將更新事項資訊的列表存入 json 檔案
		with open("D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\Bdo_update.json", "w", encoding="utf-8") as f:
			json.dump(data_list, f, ensure_ascii=False, indent=4)

		name = "更新事項"
		for i in data_list:
			await ctx.send(f"[更新事項] {i[name]} ")


	

async def setup(bot):
	await bot.add_cog(Main(bot))


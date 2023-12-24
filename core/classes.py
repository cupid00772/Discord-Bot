import discord
from discord.ext import commands
import json, datetime
# 放所有的類別(class)
class Cog_Extension(commands.Cog):
    """用於Cog繼承基本屬性"""
    #初始化(initialization)
    def __init__(self, bot):
        self.bot = bot


class Gloable_Data:
    """自定義全域資料"""
    errors_counter = 0
    def __init__(self, *args, **kwargs):
        ...


class Global_Func():
    """自定義常用功能"""

    def update_jdata(self, key, data, type='default', mode='update'):
        '''
        更新 Jdata 功能
        type: default / list
        mode: update / delete
        '''
        with open('D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
            if mode == 'update':
                if type == 'default':
                    jdata[key] = data
                elif type == 'list':
                    jdata[key].append(data)
            elif mode == 'delete':
                if type == 'list':
                    jdata[key].remove(data)
                
        with open('D:\DiscordBot-Python\Discord_bot_Proladon\Discord-bot\json\yy', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4, ensure_ascii=False)
    
    
    #CodeBlock
    @classmethod
    def code(cls, lang, msg):
        '''CodeBlock'''
        return f'```{lang}\n{msg}\n```'


class Logger:
    def log(self, ctx, data, type='error'):
        '''事件紀錄器'''
        time = datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M]')
        user = ctx.author.name
        channel = ctx.channel.name
        command = ctx.command
        if type == 'error':
            print(f'🔥<Error Log>: {time}/[{user}][{channel}][{command}]: {data}')
from ycmd.ycmd import CMD
from ycmd.ClassData import ClassData
import re
import urllib.parse
import urllib.request
import asyncio
import discord
import os
import json
import datetime
import random
import time
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import aiomysql
cmd = CMD()
intent=discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intent)
with open("data.json") as ff:
    settings=json.load(ff)
@client.event  # check if bot is ready
async def on_ready():
    await client.load_extension('jishaku')
    loop = asyncio.get_event_loop()
    pool = await aiomysql.create_pool(host=settings['mysql']['host'], port=int(settings['mysql']['port']),user=settings['mysql']['user'], password=settings['mysql']['pass'],db=settings['mysql']['db'], loop=loop,autocommit=True)
    cmd.var["pool"]=ClassData(pool)
    cmd.var["secret"]=ClassData(settings)
    cmd.var["bot"]=ClassData(client)
    await cmd.cmdrun_method_file("main.ycmd","on_ready")
@client.event
async def on_message(message):
    cmd.var["message"]=ClassData(message)
    cmd.var["bot"]=ClassData(client)
    await cmd.cmdrun_method_file("main.ycmd","on_message")
    await client.process_commands(message)
client.run(settings['token'])

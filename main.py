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
import viewbotgui
from hashids import Hashids
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL


client = commands.Bot(command_prefix='!')
@client.event  # check if bot is ready
async def on_ready():
    cmd = CMD()
    cmd.var["bot"]=ClassData(client)
    await cmd.cmdrun_method_file("main.ycmd","on_ready")
@client.event
async def on_message(message):
    cmd = CMD()
    cmd.var["message"]=ClassData(messgae)
    cmd.var["bot"]=ClassData(client)
    await cmd.cmdrun_method_file("main.ycmd","on_message")
client.run('token')

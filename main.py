import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import random
from discord.utils import get
from discord import FFmpegPCMAudio
import youtube_dl


load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents) 

"""This is update 1"""
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
@bot.event
async def on_message(message):
    
    if message.content == 'Sawasdee' or message.content == 'สวัสดี' or message.content == 'Hello' or message.content == 'Hi' or message.content == 'Yo':
        greet_1 = ['Good ','Hello','Hi','Ayo Wassup']
        x = random.randint(0,3)
        current_time = datetime.now()
        current_time = int(current_time.strftime('%H'))
        if x==0:
            if 2<=current_time<=12:
                await message.channel.send(greet_1[int(x)]+'Morning! '+message.author.name)
            elif 12<=current_time<=18:
                await message.channel.send(greet_1[int(x)]+'Afternoon! '+message.author.name)
            elif 18<=current_time<=23:
                await message.channel.send(greet_1[int(x)]+'Evening! '+message.author.name)
        elif x==1:
            await message.channel.send(greet_1[int(x)]+' '+message.author.name)
        elif x==2:
            await message.channel.send(greet_1[int(x)]+' '+message.author.name)
        elif x==3:
            await message.channel.send(greet_1[int(x)]+' '+message.author.name)
                
    elif message.content == '!logout':
        await message.channel.send('See you later!')
        await bot.close()
        
    
@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_client == None:
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)
        voice_client.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    ydl_opts = {'format': 'bestaudio',
                'noplaylist' : 'True'}
    
    if not voice_client.is_playing():   
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(URL))
        voice_client.is_playing()
    else:
        await channel.send('Song still playing')
    
@bot.command
async def leave(ctx):
    ctx.voice_client.disconnect()
        
bot.run(TOKEN)
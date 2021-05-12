from discord import FFmpegPCMAudio
from discord.utils import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import bs4
import asyncio
import time
import discord

from discord.ext import commands
from youtube_dl import YoutubeDL


bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('log_in: ')
    print(bot.user.name)
    print('Hugh is summoned, meow!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Playing with toy"))

@bot.command()
async def copy(ctx, *, text):
  await ctx.send(text)

@bot.command()
async def summon(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        await ctx.send("Meow Meow!!")
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("Where are you...meow...")

@bot.command()
async def sleep(ctx):
        await vc.disconnect()
        await ctx.send("Zzz..")

@bot.command()
async def Meow(ctx):
    await ctx.send('Meow?')

@bot.command()
async def hi(ctx):
    await ctx.reply('Meow!!')

@bot.command()
async def mood(ctx):
    await ctx.reply('Meow! Hugh is happy!')

@bot.command()
async def bye(ctx):
    await ctx.reply('Meow..?Meow.....')

@bot.command()
async def heh(ctx):
    await ctx.reply('heh ꉂꉂ(ᵔᗜᵔ*) heh ꉂꉂ(ᵔᗜᵔ*) hehe ꉂꉂ(ᵔᗜᵔ*) Meow!')

@bot.command()
async def p(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "Now Playing Meow", description = url, color = 0x00ff00))
    else:
        await ctx.send("Meow! It's playing now!")
        
@bot.command()
async def t(ctx, *, msg):
    if not vc.is_playing():

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            

        chromedriver_dir = "C:\Users\Jimin Hyeon\Desktop\Hugh Bot\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query="+msg)
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "Now Playing Meow", description = entireText, color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("Meow! It's playing now!")

@bot.command()
async def pause(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "Meow! It's paused.", description = entireText + "paused", color = 0x00ff00))
    else:
        await ctx.send("Meow! Nothing in the queue.")

@bot.command()
async def resume(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("Meow! Nothing in the queue.")
    else:
         await ctx.send(embed = discord.Embed(title= "Meow! Resume.", description = entireText  + "resumed", color = 0x00ff00))

@bot.command()
async def stop(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "Meow! Stop playing!", description = entireText  + "stopped", color = 0x00ff00))
    else:
        await ctx.send("Meow! Music is not playing!")

bot.run('ODM2NzI3OTIwNTIwMjAwMjIz.YIiNmQ.UhGMX5X05Li9HRVTjjLbpG1Oeq0')
# Token

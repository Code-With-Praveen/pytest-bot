import nextcord
from nextcord.ext import commands
from nextcord.ext import *
from nextcord import *
from nextcord import FFmpegPCMAudio
import asyncio
import os
import requests

#For a more secure, we loaded the .env file and assign the token value to a variable 



intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = '!',intents=intents )



@bot.event
async def on_ready() :
    channel = bot.get_channel(1008748431222771712)
    await channel.send('hello')
    
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()
@bot.command()

async def hola(ctx):
    author = message.author
    content = message.content
    await ctx.send('{}: {}'.format(author, content))
    
@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "general" :
                await channel.send('Bot Activated..')
                await channel.send(file=nextcord.File('vanakam.gif'))
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count)) 
   
@bot.command()
async def hi(ctx):
    username = ctx.message.author.mention
    await ctx.send('Hello' + username)
    
@bot.command()
async def hru(ctx):
    await ctx.send('''How Can I Help 
                   Yooooou''')
@bot.command()
async def Hello(ctx):
    await ctx.send("May I help You")
'''  

'''
@bot.command()
async def dog(ctx):
    dogPicture = requests.get('http://thedogapi.com/api/images/get?format=src&type=png')
    if dogPicture.status_code == 200:
        dogPicture = dogPicture.url
        await ctx.send(dogPicture)
        await ctx.send("bow bow")
    else:
        await ctx.send('bow bow not availble')

@bot.command()
async def cat(ctx):
    catPicture = requests.get('http://thecatapi.com/api/images/get.php')
    if catPicture.status_code == 200:
        catPicture = catPicture.url
        await ctx.send(catPicture)
        await ctx.send("meow")
    else:
        await ctx.send('meaw meow dosnt exist')

@bot.command()
async def list(ctx):
    await ctx.send('''hi
hru
hello 
list - list of Commands''')
    
@bot.command()
async def nakku(ctx):
    username = ctx.message.author.mention
    await ctx.send("nakku"+username)   
    await ctx.send(file=nextcord.File('nakku.gif'))

   # send message whn someone join 
@bot.event
async def on_member_join(member) :
    channel = bot.get_channel(1008748431222771712)
    await channel.send('hello')
# send message whn someone leves 
@bot.event
async def on_member_remove(member) :
    channel = bot.get_channel(1008748431222771712)
    await channel.send('Goodbye')
 # join a voice hannel  
 
@bot.command(pass_context = True)

async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice =  await channel.connect()
        source = FFmpegPCMAudio('pasoori.mp3')
        player = voice.play(source)
    else:
        await ctx.send('Kindly join a voice channel to run this command')
        
# leave a voice channel
'''
@bot.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send ('I left the voice chat')
    else:
        await ctx.send('I an not in a voice chat')
        
'''       


        
@bot.command()
async def yt(self, ctx, *, url):
    """Plays from a url (almost anything youtube_dl supports)"""

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('Now playing: {}'.format(player.title))


@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = nextcord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(nextcord.FFmpegPCMAudio("song.mp3"))


@bot.command()
async def leave(ctx):
    voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command()
async def pause(ctx):
    voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command()
async def resume(ctx):
    voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command()
async def stop(ctx):
    voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

bot.run("OTk5NzA0MDgwNDAwMjczNDE4.GULxhH._C5O90EhDQUsyllGaL4o21ug_7z9-oKCIcEAAM")
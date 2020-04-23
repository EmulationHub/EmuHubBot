import aiohttp
import asyncio
import box
import config
import datetime
import discord
import jishaku
import json
import nekos
import os
import platform
import random
import requests
import re
import typing
from dadjokes import *
from datetime import datetime
from discord.ext import commands
from webserver import keepalive

#Core Bot
client = commands.Bot(description = "Rob Bot", command_prefix = "!")
client.remove_command('help')
client.remove_command('frizzy')
client.launch_time = datetime.utcnow()
EQUAL_REGEX = re.compile(r"""(\w+)\s*=\s*["'](.+?)["']""")

#Starting Bot
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='A Netplay Game'))
    print("#################\n# Bot is online #\n#################")
    print("Running as: " + client.user.name)
    print("Discord.py: " + discord.__version__)
    print("Created by Cranky Supertoon#7376")

#Join Logs
@client.event
async def on_member_join(member):
  welcomechannel = client.get_channel(684180084307001423)
  staffwelcomechannel = client.get_channel(691010936500256859)
  jl = [f"We've got cookies {member.mention}!",
    f"Isn't there a discord server for memes like {member.mention}?",
    f"October 31st, Halloween, November 1st, beginning of Hanukkah and Christmas, what is this {member.mention}!",
    f"{member.mention}, Do you like spooky? I like spooky, SPOOOOOKY!!!",
    f"The cake is a lie, or is it {member.mention}?",
    f"There’s a fire burning {member.mention}! Anybody got marshmallows?",
    f"Minecraft 1.13 is here {member.mention}! It took a long time for you guys to add water animals Mojang!",
    f"You like games {member.mention}? Hopefully!",
    f"Once you get here {member.mention}, you just keep going and going and going...!",
    f"Every {member.mention} is like a bird, they just fly in out of nowhere and poop on your head! Not really though!",
    f"Never enough {member.mention}'s, or maybe too many I don’t know!",
    f"Free Advice From Phantom_storm {member.mention} don't eat your mic, it's too...salty.",
    f"I see a message in the sky it says, “welcome {member.mention}!",
    f":notes:I see trees of green, {member.mention}  too:notes: and i think to myself what a wonderful sever!:notes:",
    f"{member.mention} came prepared, with absolutely nothing!",
    f"A new player has entered the ring, {member.mention} , show us what you can do!",
    f"We have free icecream {member.mention}! But it may melt, so hurry fast!",
    f"It’s time to do do do do do do do do do do do do DOOO ITTTT {member.mention}!!!!",
    f"Made with 100% dank memes {member.mention}!",
    f"This match will get red hot {member.mention}!",
    f"Wonder what this button does {member.mention}, oh, another member, amazing!!!",
    f"A brawl is surely brewing {member.mention}!",
    f"The Man, The Myth, The Legend, {member.mention} has entered the building!",
    f"Do you knew the wae {member.mention}? We do know the wae!",
    f"Old friends new friends like {member.mention} they’re all my friends!",
    f"We were expecting you {member.mention} ( ͡° ͜ʖ ͡°)",
    f"We count by friends not members {member.mention}!:grin:",
    f"I wonder how many people are on the server? Oh wait, here comes {member.mention}!",
    f"Obviously {member.mention} is not an alt account, am I right or am I right! :sunglasses:"
    ]
  jlrandom = random.choice(jl)
  await welcomechannel.send(f"{jlrandom}")
  await staffwelcomechannel.send(f"{member} Joined. Account created on {member.created_at}")

#Info Command
@client.command("info")
async def s_info(ctx):
    server = ctx.guild
    icon = server.icon_url_as(size=256)
    icon = ("\uFEFF")
    embed = discord.Embed(title=f"Server info for {server.name}", description=None, colour=0x98FB98)
    embed.set_thumbnail(url=icon)
    # Basic info -- Name, Region, ID, Owner (USER+descrim, ID), Creation date, member count
    embed.add_field(name="Name", value=server.name, inline=False)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Owner", value=f"{server.owner.name}**-**{server.owner.id}", inline=True)
    embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
    embed.add_field(name="Server Icon Url", value=server.icon_url, inline=False)
    embed.add_field(name="Member Count", value=server.member_count, inline=True)
    await ctx.send(content=None, embed=embed)

@client.command()
async def help(ctx):
  author = ctx.message.author
  embed = discord.Embed(color = discord.Color.orange())

  embed.set_author(name="Commands:")
  embed.add_field(name="General", value="!help - Shows This Message\n\n!ping - Says Pong Back To You\n\n!uptime - Bot Uptime Counter\n\n!toss - Coin Flip\n\n!Dadjoke - Give a Dad Joke\n\n!dice - Roll 1-6", inline=False)
  embed.add_field(name="Nintendo Emulators", value="!nes - Shows the Different NES Emulators\n\n!snes - Shows the Different SNES Emulators\n\n!n64 - Shows the Different N64 Emulators\n\n!gc - Shows the Different GameCube Emulators\n\n!wii - Shows the Different Wii Emulators\n\n!wiiu - Shows the Different Wii U Emulators\n\n!switch - Shows the Different Switch Emulators")
  embed.add_field(name="Sega Emulators", value="!mastersystem - Shows the Different Master System Emulators\n\n!megadrive - Shows the Different Mega Drive Emulators\n\n!32x - Shows the Different 32X Emulators\n\n!saturn - Shows the Different Sega CD Emulators\n\n!saturn - Shows the Different Saturn Emulators\n\n!dreamcast - Shows the Different Dreamcast Emulators\n\n!gamegear - Shows the Different Game Gear Emulators and their Qualities\n")
  embed.add_field(name="PlayStation Emulators", value="!ps1 - Shows the Different PS1 Emulators\n\n!ps2 - Shows the Different PS2 Emulators\n\n!ps3 - Shows the Different PS3 Emulators\n\n!ps4 - Shows the Different PS4 Emulators\n\n!psp - Shows the Different PSP Emulators\n\n!vita - Shows the Different Vita Emulators")
  embed.add_field(name="Xbox Emulators", value="!ogxbox - Shows the Different Original Xbox Emulators\n\n!xbox360 - Shows the Different Xbox 360 Emulators\n\n!xbox1 - Shows the Different Xbox 1 Emulators")
  embed.add_field(name="Atari Emulators", value="!2600 - Shows the Different Atari 2600 Emulators\n\n!5200 - Shows the Different Atari 5200 Emulators\n\n!7800 - Shows the Different Atari 7800 Emulators\n\n!lynx - Shows the Different Atari Lynx Emulators\n\n!jaguar - Shows the Different Atari Jaguar Emulator")
  embed.add_field(name="Other Emulators", value="!pcengine - Shows the Different PC Engine")
  await ctx.send(author, embed=embed)

@client.command()
async def nes(ctx):
  #author = ctx.message.author
  embed = discord.Embed(color = discord.Color.orange())

  #embed.set_author(name="NES Emulators")
  embed.add_field(name="NES Emulators", value="!mesen - A New Open Source Cycle Accurate NES Emulator with a Clean Interface and Compatibility. Supports Netplay\n\n!nestopia - A Open Source Cycle Accurate NES Emulator that has Excellant Compatibility and is Trusted for being around for a decade\n\n!fceux - FCEUX is an old Open Source Mid Accurate Emulator that has good Compatibility but was surpassed by alot of others. It has really good debugging tools.\n\n!punes - puNES is a Semi New Cycle Accurate NES Emulator. It has some really nice features like a excellant Rewind function.\n\n!virtuanes - VirtuaNES is an Open Source Low Accurate Japaneese Emulator. It is famous for its stupid amount of accessory support but should only be used by the games that require said accessories.", inline=False)
  await ctx.send(embed=embed)

#Uptime Command
@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

#Ping Command
@client.command()
async def ping(ctx):
    """Ping Pong"""
    await ctx.send('Pong!')

#Dice Command
@client.command()
async def dice(ctx):
  """Rolls the dice"""
  cont = random.randint(1, 6)
  await ctx.send("You Rolled **{}**".format(cont))

#Toss Command
@client.command()
async def toss(ctx):
  """Put the toss"""
  ch = ["Heads", "Tails"]
  rch = random.choice(ch)
  await ctx.send(f"You got **{rch}**")

#Dadjoke Command
@client.command()
async def dadjoke(ctx):
  """Sends the dadjokes"""
  async with ctx.typing():
      await ctx.send(Dadjoke().joke)

#PSCX2 Emulator Command
@client.command()
async def pcsx2(ctx):
  """Sends a link to the PSCX2 Download Page and its Bios"""
  async with ctx.typing():
      await ctx.send('**PSCX2 Stable Builds: **\n<https://pcsx2.net/download.html>\n\n**PSCX2 Development Builds: **\n<https://buildbot.orphis.net/pcsx2/>\n\n**Bios:**\n<https://romsmania.cc/bios/pcsx2-playstation-2-bios-3>')

#RPCS3 Emulator Command
@client.command()
async def rpcs3(ctx):
  """Sends a link to the RPCS3 Download Page and its Bios"""
  async with ctx.typing():
      await ctx.send('**RPCS3 Stable Builds:**\n<https://rpcs3.net/download>\n\n**RPCS3 Development Builds:**\n<https://rpcs3.net/compatibility?b> \n\n**Firmware:**\n<https://www.playstation.com/en-us/support/system-updates/ps3>')

#Citra Emulator Command
@client.command()
async def citra(ctx):
  """Sends a link to the Citra Download Page"""
  async with ctx.typing():
      await ctx.send('**Citra Builds:**\n<https://citra-emu.org/download/>')

#PPSSPP Emulator Command
@client.command()
async def vita3k(ctx):
  """Sends a link to the Vita3K Download Page and its Bios"""
  async with ctx.typing():
      await ctx.send('**Vita3K Development Builds:**\n<https://vita3k.org/#download>\n\n**Firmware:**\n<https://www.playstation.com/en-us/support/system-updates/ps-vita/>')

#PPSSPP Emulator Command
@client.command()
async def ppsspp(ctx):
  """Sends a link to the PPSSPP Download Page"""
  async with ctx.typing():
      await ctx.send('**PPSSPP Stable Builds:**\n<https://www.ppsspp.org/downloads.html>\n\n**PPSSPP Development Builds:**\n<https://buildbot.orphis.net/ppsspp/>')

#Mednafen Emulator Command
@client.command()
async def mednafen(ctx):
  """Sends a link to the Mednafen Download Page"""
  async with ctx.typing():
      await ctx.send('**Mednafen Stable Builds:**\n<https://mednafen.github.io/releases/>')

#Higan Emulator Command
@client.command()
async def higan(ctx):
  """Sends a link to the Higan Download Page"""
  async with ctx.typing():
      await ctx.send('**Higan Stable Builds:**\n<https://byuu.org/higan#download>\n\n**Higan Development Builds**\n<https://cirrus-ci.com/github/higan-emu/higan/master>')

#PuNES Emulator Command
@client.command()
async def punes(ctx):
  """Sends a link to the PuNES Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**PuNES Stable Builds:**\n<https://github.com/punesemu/puNES/releases>\n\n**PuNES Development Builds:**\n<https://ci.appveyor.com/project/punesemu/punes/build/artifacts>')

#FCEUX Emulator Command
@client.command()
async def fceux(ctx):
  """Sends a link to the FCEUX Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**FCEUX Stable Builds:**\n<http://www.fceux.com/web/download.html>\n\n**FCEUX Development Builds:**\n<https://ci.appveyor.com/project/zeromus/fceux/build/artifacts>')

#Mesen Emulator Command
@client.command()
async def mesen(ctx):
  """Sends a link to the Mesen Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Mesen Stable Builds:**\n<https://www.mesen.ca/#Downloads>\n\n**Mesen Development Builds:**\n<https://ci.appveyor.com/project/Sour/mesen/build/artifacts>')

#VirtuaNES Emulator Command
@client.command()
async def virtuanes(ctx):
  """Sends a link to the VirtuaNES Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**VirtuaNES Stable Builds:**\n<http://virtuanes.s1.xrea.com/vnes_dl.php>')

#Nestopia Emulator Command
@client.command()
async def nestopia(ctx):
  """Sends a link to the Nestopia Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Nestopia Stable Builds:**\n<https://sourceforge.net/projects/nestopiaue/files/>')

#Mesen-S Emulator Command
@client.command(aliases=['mesen-s'])
async def mesensnes(ctx):
  """Sends a link to the Mesen-S Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Mesen-S Stable Builds:**\n<https://github.com/SourMesen/Mesen-S/releases>\n\n**Mesen-S Developement Builds:**\n<https://ci.appveyor.com/project/Sour/mesen-s/build/artifacts>')

#bsnes Emulator Command
@client.command()
async def bsnes(ctx):
  """Sends a link to the bsnes Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**bsnes Stable Builds:**\n<https://byuu.org/bsnes#download>\n\n**bsnes Builds Download:**\n<https://cirrus-ci.com/github/bsnes-emu/bsnes/master>')

#ZSNES Emulator Command
@client.command()
async def zsnes(ctx):
  """Sends a link to the zsnes Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**zsnes Stable Builds:**\n<https://www.zsnes.com/index.php?page=files>')

#ZSNES Emulator Command
@client.command()
async def snes9x(ctx):
  """Sends a link to the Snes9x Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Snes9x Stable Builds:**\n<http://www.s9x-w32.de/dl/>\n\n**Snes9x Development Builds:**\n<https://ci.appveyor.com/project/snes9x/snes9x>')

#Project64 Emulator Command
@client.command()
async def project64(ctx):
  """Sends a link to the Project64 Download Page"""
  async with ctx.typing():
      await ctx.send('**Project64 Stable Builds:**\n<https://www.pj64-emu.com/public-releases>\n\n**Project64 Development Builds:**\nPlease Use These, The Stable Builds are Super Old\n<https://www.pj64-emu.com/nightly-builds>')

#Project64 Netplay Emulator Command
@client.command()
async def project64netplay(ctx):
  """Sends a link to the Project64 Netplay Download Page"""
  async with ctx.typing():
      await ctx.send('**Project64 Netplay Stable Builds:**\n<https://pj64netplay-emu.ml/download.html>')

#Mupen64Plus Emulator Command
@client.command(aliases=['mupen64'])
async def mupen64plus(ctx):
  """Sends a link to the Mupen64Plus Download Page"""
  async with ctx.typing():
      await ctx.send('**Mupen64 Stable Builds:**\nNot Recommended For The Average User\n<https://github.com/mupen64plus/mupen64plus-core/releases/>\n\n**m64p (Mupen64 Plus a GUI) Builds**:\nRecommended for its Custom Plugins that fits well with its GUI\n<https://github.com/loganmc10/m64p/releases>\n\n**M64Py (Mupen 64 Python) Builds**:\nHas a Decent GUI and good Plugin Support\n<https://sourceforge.net/projects/m64py/files/>')

#CEN64 Emulator Command
@client.command()
async def cen64(ctx):
  """Sends a link to the CEN64 Download Page"""
  async with ctx.typing():
      await ctx.send('**CEN64 Stable Builds:**\n<https://cen64.com/>\n\n**CEN64-QT Builds:**\nGUI for CEN64\n<https://github.com/dh4/cen64-qt/releases>')

#Nemu64 Emulator Command
@client.command()
async def nemu64(ctx):
  """Sends a link to the Nemu64 Download Page"""
  async with ctx.typing():
      await ctx.send('**Nemu64 0.8 Mirror lInk:**\nOnly Use for Its Extensive Set of Plugins. Offical Website is long dead\n<https://www.majorgeeks.com/files/details/nemu64.html/>')

#Dolphin Emulator Command
@client.command()
async def dolphin(ctx):
  """Sends a link to the Dolphin Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Dolphin Stable 5.0:\n<https://dl-mirror.dolphin-emu.org/5.0/dolphin-x64-5.0.exe>\n\n**Dolphin Development Builds**\n<https://dolphin-emu.org/download/list/master/1/>')

#Cemu Emulator Command
@client.command()
async def cemu(ctx):
  """Sends a link to the Cemu Download Page"""
  async with ctx.typing():
      await ctx.send('**Cemu Stable Build:**\n<http://cemu.info/#download>')
#Run Bot
keepalive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)

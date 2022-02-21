import discord
import shlex
from discord.ext.commands import has_permissions
import requests
import json
from os.path import exists

global started
started = False

print("Starting client...")

client = discord.Client()
@client.event
async def on_ready():
    global started
    if started != True:
        started = True
        global guild
        global channel

        print("Bot ready!")

        for guild in client.guilds:
            print(guild.name)

        guild = discord.utils.get(client.guilds, name=input("Which guild do you want to join? "))

        for channel in guild.channels:
            if str(channel.type) == 'text':
                print(channel.name)

        channel = discord.utils.get(guild.channels, name=input("Which channel do you want to join? "))

        while (1 == 1):
            await channel.send(input("Message: "))


client.run(open('token','r').read())

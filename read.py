import discord
import shlex
from discord.ext.commands import has_permissions
import requests
import json
from os.path import exists

print("Starting client...")

client = discord.Client()

@client.event
async def on_ready():
    print("Bot ready!")

@client.event
async def on_message(message):
    bot_text = ""

    if message.author.bot:
        bot_text = " [bot]"
    
    color = ""
    
    msgcontent = message.content

    for mention in message.mentions:
        endc = "\033[0m"
        if mention.id == client.user.id:
            endc = ""
        msgcontent = msgcontent.replace("<@!" + str(mention.id) + ">", "\033[43m@" + mention.name + "#" + mention.discriminator + endc)
        if mention.id == client.user.id:
            color = "\033[43m"

    print(color + "(" + message.guild.name + " " + "#" + message.channel.name + ") " + message.author.name + "#" + str(message.author.discriminator) + bot_text + ": " + msgcontent + "\033[0m")

client.run(open('token','r').read())

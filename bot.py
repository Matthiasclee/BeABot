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
    global g_id
    global guild

    print("Bot ready!")

    for guild in client.guilds:
        print(guild.name + ": " + str(guild.id))

    g_id = input("Which guild do you want to join? ")
    guild = discord.utils.find(lambda g : g.id == int(g_id), client.guilds)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.guild.id) != g_id:
        return

    bot_text = ""

    if message.author.bot:
        bot_text = " [bot]"
    
    color = ""
    
    msgcontent = message.content

    for mention in message.mentions:
        msgcontent = msgcontent.replace("<@!" + str(mention.id) + ">", "@" + mention.name + "#" + mention.discriminator)
        if mention.id == client.user.id:
            color = "\033[43m"

    print(color + "#" + message.channel.name + " - " + message.author.name + "#" + str(message.author.discriminator) + bot_text + ": " + msgcontent + "\033[0m")

client.run(open('token','r').read())

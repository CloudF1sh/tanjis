import discord
import os

from dotenv import load_dotenv

load_dotenv()
#grab API token from .env
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client=discord.Client()

#Tanjis found the coffee
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#A NEW CHALLENGER APPROCHES!!!
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'HI {member.name}, Welcome to the server!')

#to prevent infinite loops
@client.event
async def on_message(message):
    if message.author == client.user:
        return

#Listener for Channel Messages
@client.event
async def on_message(message):
    if message.content == "Tanjis?":
        await message.channel.send("Hi!")

client.run("OTczNzkxNzI2NjU1NDAxOTk0.Gav4gt.doyGeUqcBxdFH3AfyRpOG0Y4oLEYPxTiFz1a2M")
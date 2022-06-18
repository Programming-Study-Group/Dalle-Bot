# configuration
from settings import settings

# discord
import discord
from requests import post

# regex
import re

# base64
import io
from base64 import b64decode

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!generate:'):
        await message.channel.send("Making the request - it may take a while")
        req = post(url = settings.URL, json = {'prompt': message.content.split("!generate:")[1].strip()})
        await message.channel.send("Result is completed")
        
        images = re.search('\[(.*)\]', req.content.decode("utf-8") ).group(0)
        encodings = [e.replace("\\n", "") for e in re.findall('"([^"]*)"', images)]
        for encoded in encodings:
            with open("image.png", "wb") as fh:
                fh.write(b64decode(encoded))
                await message.channel.send(file = discord.File("image.png"))
        
client.run(settings.TOKEN)

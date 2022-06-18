# configuration
from settings import settings

# discord
import discord
from requests import post

# regex
import re

# base64
import io
from base64 import b64decode, b64encode

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$generate:'):
        await message.channel.send("Making the request - it may take a while")
        req = post(url = settings.URL, json = {'prompt': "yoda"})
        await message.channel.send("Result is completed")
        
        images = re.search('\[(.*)\]', req.content.decode("utf-8") ).group(0)
        encodings = [e.replace("\\n", "%0A") for e in re.findall('"([^"]*)"', images)]
        for encoded in encodings:
            # for the padding
            a = b64decode(encoded + "===")
            print(encoded, "\n\n\n")
            print(b64encode(a), "\n\n\n")
            print(b64encode(a) == encoded) # supposed to return true - but false
            
            with open("imageToSave.png", "wb") as fh:
                fh.write(b64decode(encoded))
                file = discord.File(io.BytesIO(b64decode(encoded)))
                await message.channel.send(file = file)

client.run(settings.TOKEN)

import discord
import random
from bot_logic import gen_pass,game,currency, gen_emoji, flip_coin



intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$8ball'):
       await message.channel.send(game())
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(20))
    elif message.content.startswith('$currency'):
        await message.channel.send(currency())
    elif message.content.startswith("$emoji"):
        await message.channel.send(gen_emoji())
    elif message.content.startswith("$flip"):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)

client.run("token")

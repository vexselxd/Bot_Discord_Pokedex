import discord
import random
import os
from discord.ext import commands 
from bot_logic import gen_pass, game, currency, gen_emoji, flip_coin, pokemonAPI


intents = discord.Intents.default()
intents.members = True 
intents.message_content = True  


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, password_count = 20):
    await ctx.send(gen_pass(password_count))

@bot.command()
async def ball(ctx):
    await ctx.send(game())

@bot.command()
async def currency(ctx):
    await ctx.send(currency())

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin()) 

@bot.command()
async def meme(ctx):
    imagenes = os.listdir("images")
    imagen = random.choice(imagenes)
    with open(f'images/{imagen}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def pokemon(ctx, nombre: str):
    embed = pokemonAPI(nombre)
    if embed:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"No se encontró información para el Pokémon '{nombre}'. Por favor, verifica el nombre.")


bot.run("Token")





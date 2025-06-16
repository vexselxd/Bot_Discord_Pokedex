import random
import requests
import discord

# Generar contraseñas
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

# Juego de respuestas aleatorias
def game():
    answers = [
        "Sigue por este camino y lograrás todo.",
        "Vaya... ¡Qué mala suerte!",
        "Yo digo que sí.",
        "Tengo mis dudas...",
        "La verdad, no lo sé.",
        "Supondremos que sí.",
        "Naaaaaa...",
        "Creo que no.",
        "Supongamos que sí.",
    ]
    return random.choice(answers)

# Moneda aleatoria
def currency():
    results = [
        "¡Y es cara!",
        "¡Y es escudo!",
    ]
    return random.choice(results)

# Generar emojis
def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

# Lanzar moneda
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "CRUZ"

def pokemonAPI(nombre):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        nombre_pokemon = data['name'].capitalize()
        id_pokemon = data['id']
        tipos = ', '.join([t['type']['name'].capitalize() for t in data['types']])
        stats = '\n'.join([f"{s['stat']['name'].capitalize()}: {s['base_stat']}" for s in data['stats']])
        sprite = data['sprites']['front_default']

        embed = discord.Embed(
            title=f"{nombre_pokemon} (ID: {id_pokemon})",
            description=f"**Tipo(s):** {tipos}\n\n**Estadísticas:**\n{stats}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=sprite)
        return embed
    except requests.exceptions.RequestException as e:
        print(f"Error al llamar a la API: {e}")
        return None
    except KeyError:
        return None

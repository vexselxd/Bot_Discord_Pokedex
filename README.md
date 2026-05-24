<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=28&duration=3000&pause=1000&color=F5C842&center=true&vCenter=true&width=600&lines=Discord+Bot+%E2%80%94+Pok%C3%A9dex+API+Call;Built+with+Python+%2B+discord.py" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.x-f5c842?style=for-the-badge&logo=python&logoColor=0a0a2e&labelColor=0a0a2e)
![discord.py](https://img.shields.io/badge/discord.py-2.x-5865f2?style=for-the-badge&logo=discord&logoColor=white&labelColor=0a0a2e)
![PokéAPI](https://img.shields.io/badge/PokéAPI-REST-f5c842?style=for-the-badge&logoColor=0a0a2e&labelColor=0a0a2e)
![License](https://img.shields.io/badge/License-Apache_2.0-f5c842?style=for-the-badge&labelColor=0a0a2e)

<br/>

> A modular Discord bot built in Python that integrates with the **PokéAPI** to deliver real-time Pokémon data as rich embeds, alongside a suite of utility commands.

</div>

---

## ✨ Features

| Command | Description |
|---|---|
| `$pokemon <name>` | Fetches live Pokémon data — name, ID, types, base stats & sprite |
| `$password [length]` | Generates a secure random password (default: 20 chars) |
| `$ball` | Magic 8-ball style random answer |
| `$flip` | Coin flip — cara o cruz |
| `$emoji` | Sends a random emoji |
| `$meme` | Sends a random image from the local `images/` folder |
| `$hello` | Bot greeting |
| `$heh [n]` | Repeats "he" n times (default: 5) |

---

## 📁 Project Structure

```
Bot_Discord_Pokedex/
│
├── main_bot.py        # Bot setup, command prefix, event handlers & command routing
├── main_client.py     # Entry point / client configuration
├── bot_logic.py       # All business logic — API calls, generators, utilities
├── images/            # Local image folder used by $meme command
└── LICENSE            # Apache 2.0
```

The project follows a **separation of concerns** pattern — `main_bot.py` handles Discord events and command definitions, while `bot_logic.py` contains all reusable logic with no Discord dependency.

---

## 🚀 Setup

### 1. Clone the repo

```bash
git clone https://github.com/vexselxd/Bot_Discord_Pokedex.git
cd Bot_Discord_Pokedex
```

### 2. Install dependencies

```bash
pip install discord.py requests
```

### 3. Add your bot token

In `main_bot.py`, replace the placeholder at the bottom:

```python
# Before
bot.run("Token")

# After
bot.run("YOUR_DISCORD_BOT_TOKEN_HERE")
```

> ⚠️ Never commit your real token to a public repo. Use environment variables or a `.env` file with `python-dotenv` for production.

### 4. Run the bot

```bash
python main_bot.py
```

---

## 🔌 How the Pokédex command works

```python
# bot_logic.py — pokemonAPI()
url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
response = requests.get(url)
response.raise_for_status()   # Raises error on 4xx/5xx
```

The function queries the [PokéAPI](https://pokeapi.co/) by name, extracts the Pokémon's name, ID, types, base stats, and official front sprite, then returns a formatted `discord.Embed`. Invalid names return a user-friendly error message instead of crashing.

---

## 📸 Demo

```
User  ›  $pokemon vaporeon
Bot   ›  Vaporeon (ID: 134)
         Tipo(s): Water
         HP: 130 | ATK: 65 | DEF: 60 | SP.ATK: 110 | SP.DEF: 95 | SPD: 65

User  ›  $pokemon charisar
Bot   ›  No se encontró información para el Pokémon 'charisar'. Por favor, verifica el nombre.

User  ›  $password 16
Bot   ›  k#9Ñ2!mQvR@wX$nA
```

---

## 🛠️ Built With

- [discord.py](https://discordpy.readthedocs.io/) — Discord API wrapper for Python
- [PokéAPI](https://pokeapi.co/) — Free RESTful Pokémon data API
- [requests](https://docs.python-requests.org/) — HTTP library for Python

---

## 📄 License

Distributed under the **Apache 2.0 License**. See [`LICENSE`](./LICENSE) for details.

---

<div align="center">

Made by [vexselxd](https://github.com/vexselxd)

</div>

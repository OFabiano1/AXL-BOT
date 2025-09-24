import discord
from discord.ext import commands

from dotenv import load_dotenv
import os
import sys

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Prefixo dos comandos !
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

# bot está online!
@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")

# Comando - Restart
@bot.command()
@commands.is_owner()  # apenas o dono pode usar
async def restart(ctx):
    await ctx.send("Reiniciando o bot... 🔄")
    os.execv(sys.executable, ['python'] + sys.argv)

# Comando - Hello World
@bot.command()
async def axolotl(ctx):
    await ctx.send("Hello World!")

# Token 
bot.run(DISCORD_TOKEN)
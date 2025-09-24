# library
import discord
from discord import app_commands
from discord.ext import commands

from dotenv import load_dotenv
import os
import sys

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Prefixo dos comandos >
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

class AXLbot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()  # Definindo os intents
        super().__init__(command_prefix=">", intents=intents)
        self.tree = app_commands.CommandTree(self)


# bot está online
@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")

# Comando - Restart
@bot.command()
@commands.is_owner()  # apenas o dono pode usar
async def restart(ctx):
    await ctx.send("Reiniciando o bot... 🔄")
    os.execv(sys.executable, ['python'] + sys.argv)

# Comando - Hello World (testes)
@bot.command()
async def axolotl(ctx):
    await ctx.send("Hello World!")


# Token 
bot.run(DISCORD_TOKEN)
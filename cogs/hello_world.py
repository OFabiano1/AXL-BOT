from discord.ext import commands
from discord import app_commands
import discord

class HelloWorld(commands.Cog):
    def __init__(self, client):
        self.client: commands.Bot = client

# commando de teste d

    @app_commands.command(
        name="xD",
        description="Teste"
    )
    async def some(self, interaction: discord.Interaction):
        await interaction.response.send_message("Olá, mundo!")

# Função para adicionar o Cog
async def setup(client: commands.Bot) -> None:
    await client.add_cog(HelloWorld(client))

import nextcord

from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("Botu kullanabilin")

@nextcord.slash_command(name= 'hello', description = 'Replies with hello')
async def hello_com(interaction : Interaction):
    await interaction.response.send_message("Hello")


client.run('TOKEN')

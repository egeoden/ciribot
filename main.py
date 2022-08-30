import nextcord

from nextcord import Interaction
from nextcord.ext import commands

intens = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("Botu kullanabilin")

client.run('TOKEN')

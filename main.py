import disnake
import os
from disnake.ext import commands
from keep_alive import keep_alive




TOKEN= os.environ["TOKEN"]
client = commands.Bot(command_prefix="*", help_command = None, intents= disnake.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user} is ready")

@client.command()
async def hello(ctx):
    await ctx.channel.send(f"selamlar {ctx.author.mention}")

client.run(TOKEN)        

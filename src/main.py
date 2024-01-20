import discord
from discord.ext import commands
from runCommand import runCommand

client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Rose bot at your service...")

@client.command()
async def hello(ctx):
    await ctx.send("Hello chatters")

runCommand(client)
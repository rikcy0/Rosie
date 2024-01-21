import discord
from discord.ext import commands
from runCommand import runCommand
import random

client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Rose bot at your service...")

@client.command()
async def hello(ctx):
    await ctx.send("Hello chatters")

@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000)
    await ctx.send(f"Ping: {bot_latency} ms.")

@client.command(aliases=['motivate'])
async def spread_positivity(ctx):
    quote = ['**You look great today!**', '**Something great will happen today.**', '**Play league of legends!**',
                '**You are awesome!**', '**Thanks for being you!**', '**You have a nice smile.**', '**Bombastic, you are so fantastic.**']
    await ctx.send(random.choice(quote))

runCommand(client)
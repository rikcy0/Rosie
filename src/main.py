import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Rose bot at your service...")

@client.command()
async def hello(ctx):
    await ctx.send("Hello chatters")

client.run('MTE5ODM0MzM3MjAwNDQwNTI2OA.G_cz_W.64iwDSrCa2Wo2fPGPo0opmYWmmySSqM9XL_DPQ')
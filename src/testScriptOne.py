import discord
from discord.ext import commands



client = commands.Bot(command_prefix = ".")

youtube_api_key = "hahahahaha nice try."

@client.event
async def on_ready():
    print("el bot is ready".format(client))

@client.command()
async def say_hello_bot(ctx):
    await ctx.send("what's up?")

@client.command()
async def raise_issue(ctx):
    await ctx.send(str(client.owner_id))

@client.command()
async def do_exit(ctx):
    await ctx.send("want me gone so soon? Alright I'll leave")
    exit(0)

client.run("ENTER TOKEN HERE")

import sys
import discord
from sys import platform
from discord.ext import commands

client = commands.Bot(command_prefix="*")

token = input('bot token:')

@client.event
async def on_ready():
    print('bot online')

@client.command()
async def exec(ctx, *, text):
    import os
    message = ctx.message
    os.system(f"{text}")
    await ctx.send(f'executing the command `{text}`...')

@client.command()
async def os(ctx):
    oschk= sys.platform
    await ctx.send(f'{oschk}')


@client.command()
async def oscmds(ctx):
    await ctx.send('win32 - windows(batch)\nlinux or linux2 - linux(bash)')

@client.command()
async def stopclient(ctx):
    await ctx.send('stopping the bot...')
    try:
        os.system('exit')
    except:
        pass

client.run(''+token)

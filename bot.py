import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(721377459798278196)
    await channel.send(f'睇下, 有個戇鳩{member}入咗黎!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(721377459798278196)
    await channel.send(f'睇下, 有個傻閪{member}走撚咗!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)} ms')

bot.run("NzIxMzY2MzY1NzIxNzIyOTcx.XuTlWQ.Xbo2U6n8PjBbLo2ojTP7KZ3PYe4")
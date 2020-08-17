import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "aso.")

# Print to console when bot is ready
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ASOwnerYT"))
    print("Bot is ready")

# Pong command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# 8ball command
@client.command(aliases=['8ball'])
async def _8ball(ctx):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources echo no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(f'{random.choice(responses)}')

# Clear command (Owner only)
@client.command()
@commands.is_owner()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# Echo command (Owner only)
@client.command()
@commands.is_owner()
async def echo(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()

# Calculator command (calc)
@client.command()
async def calc(ctx, a:int, i, b:int):
    if i == '+':
        await ctx.send(a + b)
    if i == '-':
        await ctx.send(a - b)
    if i == '*' or 'x':
        await ctx.send(a * b)
    if i == '/':
        await ctx.send(a / b)


# Finally, start the bot
client.run('NjQxODc4MjMxNDgxNDUwNDk5.XcOxrw.N5op10TsLP2ijokcQQXeuqKN6hE')
#os.environ['DISCORD_TOKEN']
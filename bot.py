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
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(f'{random.choice(responses)}')

# Clear command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# Say command (Owner only)
@client.command()
@commands.is_owner()
async def say(ctx, *, message):
    await ctx.send(message)

# NOT WORKING - Say command with custom permissions (spesificuser)
#@client.command()
#async def say(ctx, *, message):
#    specificuser=['ASOwnerYT#7799']
#    if ctx.author not in specificuser:
#        return
#    else:
#        ctx.send(str(message))

# Finally, start the bot (Change DISCORD_TOKEN with your bot token)
client.run('NjQxODc4MjMxNDgxNDUwNDk5.XcOxrw.N5op10TsLP2ijokcQQXeuqKN6hE')
# Heroku: os.environ['DISCORD_TOKEN']
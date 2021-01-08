from discord import Client
import config
import messages.general as msg
from discord.ext import commands
import discord

bot = commands.Bot("b!")

# Ready Message Printer
@bot.event
async def on_ready():
    print("Bot is ready as:", bot.user)

# Ping-Pong test Command
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Help Commmand
@bot.command()
async def helpp(ctx):
    await ctx.send(msg.messages['help'])

# Shame Command
@bot.command()
async def shame(ctx, arg):
    await ctx.send(f"Shaming someone is bad. No need to worry {arg}, I'm in no hurry. :D")

@bot.command()
async def who(ctx, *args):
    args = args[0:]
    print(*args)
    if ('i' in args) or ('I' in args):
        print(f"{ctx.author.mention} is the greatest Discorder that's been alive.")
        await ctx.send(f"{ctx.author.mention} is the greatest Discorder that's been alive.")
    else:
        await(f"{', '.join([i for i in str(args).raw_mentions.mention()])}, stop being spherical dumbass")

bot.run(config.TOKEN)
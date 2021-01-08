from discord import Client
import config
import messages.general as msg
from discord.ext import commands

bot = commands.Bot("b!")

@bot.event
async def on_ready():
    print("Bot is ready as:", bot.user)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def helpp(ctx):
    await ctx.send(msg.messages['help'])

bot.run(config.TOKEN)
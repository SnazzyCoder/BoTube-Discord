from discord import Client
import config
import messages.general as msg
from discord.ext import commands
import discord
from discord.ext.commands import CommandNotFound

prefix = 'b!'
bot = commands.Bot(prefix)

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
        await ctx.send(f"{', '.join([str(i) for i in ctx.message.raw_mentions.mention()])}, stop being spherical dumbass")

@bot.command()
async def pre(ctx, new_prefix, *arg):
    if arg:
        await ctx.send(f'This command only requries 1 argument in the manner `{pre}prefix <new prefix>`')
        return
    
    prefix = new_prefix
    bot = commands.Bot(prefix)


# Command not found error!
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f'{ctx.message} is not recognized as a valid command.\n\n Send `{prefix}help` to know what I can do')


bot.run(config.TOKEN)
from discord import Client
import config
import messages.general as msg
from discord.ext import commands
import discord
from discord.ext.commands import CommandNotFound
import random
import json
import praw

prefix = 'b!'
bot = commands.Bot(prefix)

# Reddit PRAW config

reddit = praw.Reddit(client_id='o87yabkXGElJTg',
                     client_secret='4BemiUHbyhoCg5W07yLndQbXLSgy7g',
                     user_agent='BoTube-Discord')

# Ready Message Printer
@bot.event
async def on_ready():
    print("Bot is ready as:", bot.user)

# Ping-Pong test Command
@bot.command()
async def ping(ctx):
    await ctx.send(f"pong {round(bot.latency)}")

# Who is commands
@bot.command()
async def who(ctx, helping_verb, user: discord.User):
    if helping_verb.casefold() == 'i':
        await ctx.send(f"{ctx.author.mention} {random.choice(msg.praises)}")
    else:
        await ctx.send(f"{user.mention} {random.choice(msg.insults)}")

# change prefix Command
@bot.command(description="Change prefix to the prefix passed as an argument.")
async def pre(ctx, new_prefix, *arg):
    if arg:
        await ctx.send(f'This command only requries 1 argument in the manner `{pre}prefix <new prefix>`')
        return
    
    prefix = new_prefix
    bot = commands.Bot(prefix)

    await ctx.send(f"The prefix has not ! been changed to {new_prefix}")

# Insult command
@bot.command(description="Insults someone who is passed in as an argument")
async def insult(ctx, user: discord.User, *args):

    await ctx.send(f'{user.mention} {random.choice(msg.insults)}')

    if type(user) != discord.User:
        await ctx.send(f'command has to be used as ```{prefix}insult <user_mention>```')


# Say command
@bot.command()
async def say(ctx, *, message):
    await ctx.send(f'{ctx.author.mention} says:-\n\n{message}')

# Meme Command
@bot.command(pass_context=True)
async def meme(ctx, number:int=1):
    if number < 10:
        await ctx.send(f'No, {number} is too much memes.')
        return
    for _ in range(number):
        subreddits = ["AdviceAnimals",
                "MemeEconomy",
                "ComedyCemetery",
                "memes",
                "dankmemes",
                "PrequelMemes",
                "terriblefacebookmemes",
                "PewdiepieSubmissions",
                "funny",
                "teenagers"]
        memes_submissions = reddit.subreddit(random.choice(subreddits)).hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)


'''---------Commands-end-here--------'''

# Command not found error!
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f'{ctx.invoked_with} is not recognized as a valid command.\n\n Send `{prefix}help` to know what I can do')

bot.run(config.TOKEN)
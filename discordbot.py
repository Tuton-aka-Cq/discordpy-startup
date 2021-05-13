from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

items = ["<:yashiko_socute:817384253515497492>","<:whoisthis:822198965747187752>","<:soulspark_taki:839227218022367285>"]


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def slot(ctx):
    await ctx.send(':slot_machine:')
    #await ctx.send("<:yashiko_socute:817384253515497492><:whoisthis:822198965747187752><:soulspark_taki:839227218022367285>")
    await random.sample(items, 3)


bot.run(token)

from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

items = ["<:yashiko_socute:817384253515497492>","<:whoisthis:822198965747187752>","<:white_megane:817383772454256650>","<:teppei_with_monkey:817383821485670402>","<:soulspark_taki:839227218022367285>","<:smily_yashi:827608552729870386>","<:schizophrenia_tuton:823636164140597260>","<:sad_kan:820001352473378836>","<:red_tuton:818133947497185301>","<:question_tuton:818514930189205574>","<:psycopath_taki:819145434173538354>","<:otaku_yashi:817383860602011708>","<:naked_taki:820005841792925776>","<:kokujin:818031994121879562>","<:kikoushu_yashi:817383657043394591>","<:ikki_ketu:817383915374247956>","<:ikki_gu:817383959615766578>","<:ikki_choki:817383999742672936>","<:hole:817406396006006844>","<:happy_kan:819976862176116777>","<:gotohell_taki:823927277314244661>","<:gomi:822747433838182400>","<:gaiji_tuton:818514829936820246>","<:emoji_32:841389957276762175>","<:emoji_31:841366035575865344>","<:egatyan:817384063781830656>","<:eaten_taki:817383712534298634>","<:dick_taki:820008398703558676>","<:dare:817384151296245792>","<:brazil:817383680594411583>","<:booboozabeth:833470465552547890>","<:bathup_taki:832675575746527252>"]


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def slot(ctx):
    await ctx.send(':slot_machine:')
    #await ctx.send("<:yashiko_socute:817384253515497492><:whoisthis:822198965747187752><:soulspark_taki:839227218022367285>")
    await ctx.send(random.sample(items, 3))


bot.run(token)

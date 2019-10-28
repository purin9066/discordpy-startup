from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['NjM4MzQ2OTU3NTM4MDY2NDMy.XbbqyQ.mnn9s4EHTfywzalI02PxqDu-tWk']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)

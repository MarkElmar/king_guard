import discord
from discord.ext import commands
from kingdom import kingdom

bot = commands.Bot(command_prefix='k!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def test(ctx):
    print(ctx.message.author.id)

bot.add_cog(kingdom.Kingdom(bot))

bot.run('NzQ3NzgyMzk0MDA1ODE1Mjk2.X0T4nw.mHJe3vpHOywZSUMtinGwtrXejms')

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Testarpresenca(commands.Cog):
    @bot.slash_command(name="online", description="Estou online?")
    async def testarpresenca(self, ctx):
        await ctx.respond('Estou online!')


def setup(bot):
    bot.add_cog(Testarpresenca())
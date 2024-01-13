import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Secret(commands.Cog):
    @bot.command()
    async def secret(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{ctx.author.mention}, olhe a imagem :)",file=discord.File("./images/voce.jpg"))


def setup(bot):
    bot.add_cog(Secret())
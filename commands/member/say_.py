import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Say2(commands.Cog):
    @bot.command(name="say", description="Fala uma mensagem")
    async def say(self, ctx, *, frase=None):
        if frase == None:
            await ctx.reply(f"Você não especificou oque eu tenho que falar!")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(f"{frase}")


def setup(bot):
    bot.add_cog(Say2())
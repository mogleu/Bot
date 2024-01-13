import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Creditos(commands.Cog):
    @bot.command(name="creditos", description="Mostra o criador do bot")
    async def creditos(self, ctx):
        hyperlink = discord.Embed(
            description='''Feito por [**moguel.gg ou moguel#0011**](https://discord.com/users/680737419141971977)\n[Meu canal no YouTube](https://youtube.com/@moguelrato)''',
            color=discord.Colour.blurple()
            )
        hyperlink.set_thumbnail(url="https://yt3.googleusercontent.com/2cUNNSBzAY7OOruznh80dw3ZINZfN4yHY4SxMPsbnSZ-Rsl8lknGbw8xP5f8b3ZIUKk64ZOu8Q=s176-c-k-c0x00ffffff-no-rj")
        hyperlink.set_author(name="Freitas Bot")
        await ctx.send(embed=hyperlink)


def setup(bot):
    bot.add_cog(Creditos())
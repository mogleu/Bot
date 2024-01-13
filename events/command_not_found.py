import discord
from discord.ext import commands

class CommandNotFound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title = "<:freitas_erro:1139732440122933338> **|** Não encontrei esse comando",
                description="Parece que este comando não está no meu banco de dados, consulte os meus comandos usando /help.",
                color=discord.Color(0xFF9090)
            )
            await ctx.reply(embed=embed)
        else:
            raise error  # Here we raise other errors to ensure they aren't ignored


def setup(bot):
    bot.add_cog(CommandNotFound(bot))
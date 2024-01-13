import discord
import numexpr
import asyncio
from discord.ext import commands
from discord import Option

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


class Calculator(commands.Cog):
    @commands.slash_command(name="calculadora", description="Uma calculadora que calcula expressões.")
    # IGNORE SYNTAX ERROR!!!
    # IGNORE SYNTAX ERROR!!!
    # IGNORE SYNTAX ERROR!!!
    # IGNORE SYNTAX ERROR!!!
    async def calculadora(self, interaction: discord.Interaction, *, expressão: Option(description="A expressão a ser calculada.", required=True)):
        await interaction.response.defer()

        await asyncio.sleep(1)
        try:
            answer = numexpr.evaluate(expressão)
            await interaction.followup.send(f"`{expressão}` = `{answer}`")
        except:
            await interaction.followup.send("Erro: `Expressão inválida`")


def setup(bot):
    bot.add_cog(Calculator())
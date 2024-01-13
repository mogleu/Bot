import discord
import wikipediaapi
from discord.ext import commands
from discord import option

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Wikipedia(commands.Cog):
    @commands.slash_command(name="wikipedia", description="Informações sobre algo na Wikipedia")
    @option(name="termo", description="Termo a ser pesquisado")
    async def wikipedia(self, interaction: discord.Interaction, termo):
        await interaction.response.defer()
        wiki = wikipediaapi.Wikipedia('pt')
        page = wiki.page(termo)
        if page.exists():
            await interaction.followup.send(page.summary)
        else:
            await interaction.followup.send(f'Não foi possível encontrar informações sobre "{termo}" na Wikipedia.')


def setup(bot):
    bot.add_cog(Wikipedia())
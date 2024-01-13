import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Moeda(commands.Cog):
    @commands.slash_command(name="moeda", description="Joga uma moeda para cair cara ou coroa!")
    async def moeda_command(self, ctx):
        await ctx.defer()
        r = random.choice(['cara', 'coroa'])
        await ctx.respond(f"Caiu**{r}**")


def setup(bot):
    bot.add_cog(Moeda())
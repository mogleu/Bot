import discord
import random
from discord.ext import commands
from discord import Option

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Dado(commands.Cog):
    @commands.slash_command(name="dado", description="Joga um dado de quantos lados quiser!")
    async def dado(self, ctx, lados: Option(int, description="A quantidade de lados a serem jogadas.", required=True)):
        numero = random.randint(1,lados)
        await ctx.respond(f"Número {numero}")


def setup(bot):
    bot.add_cog(Dado())
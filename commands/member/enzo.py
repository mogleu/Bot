import discord
import requests
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Enzo(commands.Cog):
    @commands.command(name="enzo", description="Manda uma foto do Enzo")
    async def enzo(self, ctx):
        r = requests.get("https://random-d.uk/api/random")
        res = r.json()
        enzofoto = random.randint(1,285)
        url = f"https://random-d.uk/api/{enzofoto}.jpg"
        embed = discord.Embed(
            title="Enzo ai na foto"
            )
        embed.set_image(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Enzo())
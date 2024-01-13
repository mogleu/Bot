import discord
import random
from discord.ext import commands
from discord import Option

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Avaliar(commands.Cog):
    @commands.slash_command(name="avaliar", description="Avalia uma característica de um membro")
    async def avaliar(self, ctx, *, caracteristica: Option(description="Característica a ser avaliada", required=True), membro: Option(discord.Member, description="Membro a ser avaliado", required=False)):
        if not membro:
            membro = ctx.author
        if caracteristica == None:
            await ctx.respond(f"Você não especificou oque eu tenho que avaliar!")
        else:
            await ctx.respond(f"{membro.mention}, você é {random.randrange(101)}% {caracteristica}")

        
def setup(bot):
    bot.add_cog(Avaliar())
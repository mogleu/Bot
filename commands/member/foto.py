import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Foto(commands.Cog):
    @bot.slash_command(name="foto", description="Manda o avatar de um membro que só você vê!")
    async def avatar_command(self, ctx, membro: discord.Member = None):
        if not membro:
            membro = ctx.author

        embed = discord.Embed(
            title=f"Avatar de {membro.name}",
            color=membro.color
            )
        embed.set_image(url=membro.avatar)
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Foto())
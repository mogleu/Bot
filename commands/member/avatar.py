import discord
from discord.ext import commands
from discord import Option

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Avatar(commands.Cog):
    @bot.slash_command(name="avatar", description="Manda um avatar de um membro")
    async def avatar_command(self, ctx, membro: Option(discord.Member, description="O membro a ter o avatar enviado.", required=False)):
        if not membro:
            membro = ctx.author

        embed = discord.Embed(
            title=f"Avatar de {membro.name}",
            color=membro.color
            )
        embed.set_image(url=membro.avatar)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Avatar())
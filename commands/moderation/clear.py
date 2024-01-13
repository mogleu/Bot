import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Clear(commands.Cog):
    @commands.command(name="clear", description="Deleta mensagens")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, quantidade_de_mensagens: int):
        embed = discord.Embed(
            title = "Sucesso!",
            description = f"{quantidade_de_mensagens} mensagens foram deletadas com sucesso!",
            color=discord.Color.random()
            )
        await ctx.channel.purge(limit=quantidade_de_mensagens+1)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Clear())
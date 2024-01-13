import discord
import asyncio
from discord.ext import commands
from main import bot


class VerifyBAmigao(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verificar", style=discord.ButtonStyle.blurple, custom_id="verify:amigao", emoji="<:amigao:1126547005506850867>")
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        guild = interaction.guild
        role = discord.utils.get(guild.roles, name="AMIGÃO")
        user = interaction.user
        await user.add_roles(role)
        embed = discord.Embed(
            title="Sucesso!",
            description=f"Você foi verificado em {guild.name}!",
            color=discord.Color.green()
        )
        await user.send(embed=embed)


class VerifyAmigao(commands.Cog):
    @commands.command(name="amigao1068264825819504802")
    async def setup(self, ctx: commands.Context):
        userid = 680737419141971977
        moguel_gg = bot.get_user(680737419141971977)
        if not (ctx.author.id == userid):
            await ctx.send(f"Você não tem permissão para usar esse comando!")
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=1)
            return
        embed = discord.Embed(
            title="Amigão",
            description="Clique no botão para virar um amigão, AGORA!",
            color=discord.Color.dark_gold()
        )
        embed.set_footer(text="Bot feito pelo moguel", icon_url=moguel_gg.display_avatar)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed, view=VerifyBAmigao())


def setup(bot):
    bot.add_cog(VerifyAmigao())
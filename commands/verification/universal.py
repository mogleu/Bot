import discord
import asyncio
from discord.ext import commands
from main import bot


class VerifyButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verificar", style=discord.ButtonStyle.blurple, custom_id="verify:button", emoji="<:Verificar:1113904486272995460>")
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        guild = interaction.guild
        role = discord.utils.get(guild.roles, name="Membro")
        user = interaction.user
        if role not in [y.id for y in user.roles]:
            await user.add_roles(role)
            embed = discord.Embed(
                title="Sucesso!",
                description=f"Você foi verificado em {guild.name}!",
                color=discord.Color.green()
            )
            await user.send(embed=embed)


class Verify(commands.Cog):
    @commands.command(name="v-setup")
    async def setup(self, ctx: commands.Context):
        userid = 680737419141971977
        if not (ctx.author.id == userid):
            await ctx.send(f"Você não tem permissão para usar esse comando!")
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=1)
            return
        embed = discord.Embed(
            title="Verificação",
            description="Clique no botão abaixo para verificar.",
            color=discord.Color.dark_gold()
        )
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed, view=VerifyButton())


def setup(bot):
    bot.add_cog(Verify())
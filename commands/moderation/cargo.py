import discord
from discord.ext import commands
from discord import Option
from discord.ext.commands import CommandInvokeError

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Cargos(commands.Cog):
    cargo = discord.SlashCommandGroup(name="cargo")

    @cargo.command(name="adicionar", description="Adiciona um cargo à um membro.")
    async def cargo_add(self, interaction: discord.Interaction, cargo: Option(discord.Role, description="O cargo a ser dado ao membro.", required=True), membro: Option(discord.Member, description="O membro a ter o cargo adicionado.", required=True)):
        await interaction.response.defer()
        
        embed = discord.Embed(
            title="Sucesso!",
            description=f"Cargo {cargo.mention} adicionado a {membro.mention}.",
            color=discord.Color.random()
        )
        try:
            await membro.add_roles(cargo)
            await interaction.followup.send(embed=embed)
        except discord.Forbidden:
            await interaction.followup.send(f"Eu não tenho permissões para fazer isso! Este cargo ({cargo.mention}) está acima do meu, um exemplo abaixo. Para resolver este erro, arraste o meu cargo para acima do que está tentando adicionar.", file=discord.File("./images/cargo_acima_add.png"))

    @cargo.command(name="remover", description="Remove um cargo de um membro.")
    async def cargo_del(self, interaction: discord.Interaction, cargo: Option(discord.Role, description="O cargo a ser removido.", required=True), membro: Option(discord.Member, description="O membro a ter o cargo removido.", required=True)):
        await interaction.response.defer()
        
        embed = discord.Embed(
            title="Sucesso!",
            description=f"Cargo {cargo.mention} removido de {membro.mention}.",
            color=discord.Color.random()
        )
        try:
            await membro.remove_roles(cargo)
            await interaction.followup.send(embed=embed)
        except discord.Forbidden:
            await interaction.followup.send(f"Eu não tenho permissões para fazer isso! Este cargo ({cargo.mention}) está acima do meu, um exemplo abaixo. Para resolver este erro, arraste o meu cargo para acima do que está tentando remover.", file=discord.File("./images/cargo_acima_del.png"))
            


def setup(bot):
    bot.add_cog(Cargos())
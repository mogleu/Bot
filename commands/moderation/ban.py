import discord
from discord.ext import commands
from discord import Option

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Ban(commands.Cog):
    @commands.slash_command(name="ban", description="Bane um membro do servidor.")
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: Option(discord.Member, description="O membro a ser banido.", required=True)):
        await ctx.defer()
        try:
            guild = ctx.guild
            embed = discord.Embed(
                title = "Sucesso!",
                description = f"{member} foi banido com sucesso!",
                color=discord.Color.random()
                )
            await ctx.edit(embed=embed)
            await guild.ban(user=member)

        except discord.Forbidden:
            await ctx.edit(content="Eu não tenho permissões para banir este membro!", embed=None)

    @commands.slash_command(name="unban", description="Desbane um membro do servidor.")
    async def unban(self, ctx, member: Option(discord.Member, description="O membro a ser desbanido.", required=True)):
        guild = ctx.guild
        embed = discord.Embed(
            title = "Sucesso!",
            description = f"{member} foi desbanido com sucesso!",
            color=discord.Color.random()
            )
        if ctx.author.guild_permissions.ban_members:
            await ctx.respond(embed=embed)
            await guild.unban(user=member)
        else:
            await ctx.respond("Você não tem a permissão `Banir membros`!", ephemeral=True)
            return

def setup(bot):
    bot.add_cog(Ban())
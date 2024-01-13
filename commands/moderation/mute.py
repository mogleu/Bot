import discord
from discord import Option
from datetime import timedelta
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Mute(commands.Cog):
    @commands.slash_command(name="mute", description="Muta um membro.")
    # IGNORE ESTE ERRO, ELE É SÓ A DESCRIÇÃO DOS ARGUMENTOS!!!
    # IGNORE ESTE ERRO, ELE É SÓ A DESCRIÇÃO DOS ARGUMENTOS!!!
    # IGNORE ESTE ERRO, ELE É SÓ A DESCRIÇÃO DOS ARGUMENTOS!!!
    # IGNORE ESTE ERRO, ELE É SÓ A DESCRIÇÃO DOS ARGUMENTOS!!!
    async def mute(self, ctx, membro: Option(discord.Member, description="O membro a ser mutado.", required=True), razão: Option(str, description="A razão do mute ao membro.", required=False), dias: Option(int, description="A quantidade de dias para o membro ser mutado.", max_value=27, required=False), horas: Option(int, description="A quantidade de horas para o membro ser mutado.", required=False), minutos: Option(int, description="A quantidade de minutos para o membro ser mutado.", required=False), segundos: Option(int, description="A quantidade de segundos para o membro ser mutado.", required=False)):
        try:
            if membro.id == ctx.author.id:
                await ctx.respond("Você não pode se mutar!")
                return
            if membro.guild_permissions.moderate_members:
                await ctx.respond("Você não pode fazer isso, esta pessoa é um moderador/a!", ephemeral=True)
                return
            if dias == None:
                dias = 0
            if horas == None:
                horas = 0
            if minutos == None:
                minutos = 0
            if segundos == None:
                segundos = 0
            duration = timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)
            if razão == None:
                embed = discord.Embed(
                    title="Sucesso!",
                    description=f"O membro <@{membro.id}> foi mutado por:\n\n**{dias}** dias\n\n**{horas}** horas\n\n**{minutos}** minutos\n\n**{segundos}** segundos",
                    color=discord.Color.random()
                )
                await membro.timeout_for(duration)
                await ctx.respond(embed=embed)
            else:
                embed = discord.Embed(
                    title="Sucesso!",
                    description=f"O membro <@{membro.id}> foi mutado por:\n\n**{dias}** dias\n\n**{horas}** horas\n\n**{minutos}** minutos\n\n**{segundos}** segundos\n\n**Razão**: `{razão}`",
                    color=discord.Color.random()
                )
                await membro.timeout_for(duration, reason=razão)
                await ctx.respond(embed=embed)

        except OverflowError:
            embed = discord.Embed(
                description="Você colocou um tempo muito grande!",
                color=discord.Color.brand_green()
            )
            await ctx.respond(embed=embed, ephemeral=True)
        
    @mute.error
    async def time_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("Você não tem permissões para fazer isso!", ephemeral=True)
        else:
            raise error

    @commands.slash_command(name="unmute", description="Desmuta um membro.")
    async def unmute(self, ctx, membro: Option(discord.Member, description="O membro a ser desmutado", required=True)):
        embed = discord.Embed(
            title="Sucesso!",
            description=f"O membro <@{membro.id}> foi desmutado por <@{ctx.author.id}>",
            color=discord.Color.random()
        )
        await membro.remove_timeout()
        await ctx.respond(embed=embed)
        
    @unmute.error
    async def untime_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("Você não tem permissões para fazer isso!", ephemeral=True)
        else:
            raise error




def setup(bot):
     bot.add_cog(Mute())
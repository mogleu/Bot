import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Logs(commands.Cog):
    @commands.slash_command(name='logs', description="Mostra o registro de auditoria do servidor")
    async def logs(self, ctx: commands.Context):
        actions = []

        async for entry in ctx.guild.audit_logs(limit = 5):
            time = entry.created_at.strftime("%d-%m-%Y %H:%M:%S")
            actions.append(f"`{entry.user}` fez `{entry.action}` em `{time}` para `{entry.target}`\n\n")

        embed = discord.Embed(title="Registro de Auditoria", description=''.join(actions), colour=0x000)
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Logs())
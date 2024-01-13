import discord
from discord.ext import commands


class StartSupport(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("[LOGS] - 🛒 Sistema de Suporte carregado! 🛒")


def setup(bot):
    bot.add_cog(StartSupport())
import discord
from discord.ext import commands


class StartEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.Cog.listener()
    async def on_ready(self):
        print("[LOGS] - ✨ Eventos carregados! ✨")


def setup(bot):
    bot.add_cog(StartEvents(bot))
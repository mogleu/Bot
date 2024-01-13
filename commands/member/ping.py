import discord
import time
from discord.ext import commands
from main import bot


class Ping(commands.Cog):
    @commands.slash_command(name="ping", description="Calcula a latência do bot")
    async def _ping(self, ctx: commands.Context):
        start = time.perf_counter()
        await ctx.defer()
        end = time.perf_counter()
        
        duration = (end - start) * 1000
    
        await ctx.respond(f":ping_pong: **Pong!**\n:robot: **Latência do Bot:** {duration:.0f}ms\n:globe_with_meridians: **Latência do WebSocket:** {bot.ws.latency * 1000:.2f}ms")


def setup(bot):
    bot.add_cog(Ping())
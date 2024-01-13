import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Ip(commands.Cog):
    @bot.slash_command(name="ip", description="Pega o IP de algum membro (visual)")
    async def ip(self, ctx, membro: discord.User):
        userid = 680737419141971977
        if not (ctx.author.id == userid):
            await ctx.respond(f"Você não tem o id correspondente a {userid}, tente entrar em contato com o criador do bot para mais informações.")
            return
        if not membro:
            membro = ctx.author
        ip1 = random.randint(1,255)
        ip2 = random.randint(1,255)
        ip3 = random.randint(10,255)
        ip4 = random.randint(100,255)

        await ctx.respond(f"IP de {membro.name}: {ip1}.{ip2}.{ip3}.{ip4}")


def setup(bot):
    bot.add_cog(Ip())
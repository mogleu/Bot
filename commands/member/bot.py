import discord
from discord.ext import commands
from main import bot


class Ondevcfezobot(commands.Cog):    
    @commands.slash_command(name="bot", description="Onde eu fiz o meu bot?")
    async def bot(self, ctx):
        eu = bot.get_user(680737419141971977)
        embed = discord.Embed(
            title="Informações do Freitas",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Programa          ", value="[**VS Code**](<https://code.visualstudio.com/>)", inline=True)
        embed.add_field(name="Linguagem          ", value="[**Python**](<https://www.python.org/downloads/>)", inline=True)
        embed.add_field(name="Bibliotecas", value="[**py-cord**](<https://docs.pycord.dev/en/stable/>)", inline=True)
        embed.add_field(name="Criador", value="[**moguel.gg**](<https://discord.com/users/680737419141971977>)", inline=True)
        embed.add_field(name="Comandos", value=f"Eu tenho {len(bot.all_commands)} comandos.")
        embed.add_field(name="Meu Site", value="[**Clique aqui!**](<https://freitas.moguel.repl.co>)")
        embed.set_thumbnail(url=eu.display_avatar)
        #await ctx.respond('[**Visual Studio Code**](https://code.visualstudio.com/) e uso [**Python**](https://www.python.org/downloads/)!')
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Ondevcfezobot())
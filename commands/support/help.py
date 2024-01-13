import discord
from discord.ext import commands
from discord import Option


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.slash_command(name="help", description="Um comando que mostra todos os comandos disponíveis.")
    async def help(self, interaction: discord.Interaction, página: Option(int, "A página para ser enviada", required=False)):
        if página == None:
            página = 1
      
        def p1():
            embed = discord.Embed(
                title="1. Comandos dos membros",
                color=discord.Color.random()
            )
            embed.add_field(name="/avaliar", value="Uso: /avaliar <membro> <caracteristica>", inline=True)
            embed.add_field(name="/avatar", value="Uso: /avatar <membro>", inline=True)
            embed.add_field(name="/banners", value="Uso: /banners", inline=True)
            embed.add_field(name="/bot", value="Uso: /bot", inline=True)
            embed.add_field(name="/calculadora", value="Uso: /calculadora <expressão>", inline=True)
            embed.add_field(name="/cargo", value="Uso: /cargo <cargo> <user>", inline=True)
            embed.add_field(name="/creditos", value="Uso: /creditos", inline=True)
            embed.add_field(name="/dado", value="Uso: /dado <lados>", inline=True)
            embed.add_field(name="/dm", value="Uso: /dm <membro> <mensagem>", inline=True)
            embed.add_field(name="/dog foto", value="Uso: /dog foto", inline=True)
            embed.add_field(name="/dog falar", value="Uso: /dog falar <texto>", inline=True)
            embed.add_field(name="/enquete", value="Uso: /enquete <emoji1> <emoji2> <pergunta>", inline=True)
            #embed.add_field(name="/enzo", value="Uso: /enzo", inline=True)
            embed.add_field(name="/foto", value="Uso: /foto <membro>", inline=True)
            embed.add_field(name="/imaginar", value="Uso: /imaginar <prompt>", inline=True)
            embed.add_field(name="/info servidor", value="Uso: /info servidor", inline=True)
            embed.add_field(name="/info user", value="Uso: /info user <membro>", inline=True)
            embed.add_field(name="/logs", value="Uso: /logs", inline=True)
            embed.add_field(name="/menu", value="Uso: /menu", inline=True)
            embed.add_field(name="/minecraft skin", value="Uso: /minecraft skin <nickname>", inline=True)
            embed.add_field(name="/moeda", value="Uso: /moeda", inline=True)
            embed.add_field(name="/online", value="Uso: /online", inline=True)
            embed.add_field(name="/ping", value="Uso: /ping", inline=True)
            embed.add_field(name="/say", value="Uso: /say <frase>", inline=True)
            embed.add_field(name="/ship", value="Uso: /ship <usuario1> <usuario2>", inline=True)
            embed.add_field(name="/ticket", value="Uso: /ticket", inline=True)
            return embed

        #def p2():
            #embed = discord.Embed(
              #title="2. Comandos dos membros",
              #color=discord.Color.random()
            #)
            #return embed
    
        def p2():
            embed = discord.Embed(
                title="2. Comandos da moderação",
                color=discord.Color.random()
            )
            embed.add_field(name="/ban", value="Uso: /ban <user>", inline=True)
            embed.add_field(name=".clear", value="Uso: .clear <quantidade_de_mensagens>", inline=True)
            embed.add_field(name="/mute", value="Uso: /mute <membro> <tempo> <porque>", inline=True)
            embed.add_field(name="/unban", value="Uso: /unban <user>", inline=True)
            embed.add_field(name="/unmute", value="Uso: /unmute <membro>", inline=False)
            return embed

        def p3():
            embed = discord.Embed(
                title="3. Comandos com prefixos",
                color=discord.Color.random()
            )
            #embed.add_field(name=".enquete", value="Uso: .enquete <pergunta>", inline=True)
            #embed.add_field(name=".help", value=f"Uso: **.**help <1-{len(pages)}>")
            embed.add_field(name=".enzo", value="Uso: .enzo", inline=True)
            embed.add_field(name=".say", value="Uso: .say <frase>", inline=True)
            return embed

        def p4():
            embed = discord.Embed(
                title="4. Comandos de Música",
                color=discord.Color.random()
            )
            embed.add_field(name="/music play universal", value="Uso: /music play universal <url> <loop>")
            embed.add_field(name="/music play arquivo", value="Uso: /music play arquivo <arquivo>")
            embed.add_field(name="/music pause", value="Uso: /music pause")
            embed.add_field(name="/music stop", value="Uso: /music stop")
            embed.add_field(name="/music retomar", value="Uso: /music retomar")
            embed.add_field(name="/music desconectar", value="Uso: /music desconectar")
            return embed

        def p5():
            embed = discord.Embed(
                title = "5. Comandos de Economia",
                color=discord.Color.random()
            )
            embed.add_field(name="/daily", value="Uso: /daily")
            embed.add_field(name="/economy saldo", value="Uso: /economy saldo <membro>")
            embed.add_field(name="/economy rank", value="Uso: /economy rank")
            embed.add_field(name="/economy shop", value="Uso: /economy shop")
            embed.add_field(name="/economy pix", value="Uso: /economy pix <membro> <valor>")
            embed.add_field(name="/economy depositar", value="Uso: /economy depositar <valor>")
            embed.add_field(name="/economy retirar", value="Uso: /economy retirar <valor>")
            embed.add_field(name="/economy comprar", value="Uso: /economy comprar <item> <quantidade>")
            embed.add_field(name="/economy vender", value="Uso: /economy vender <item> <quantidade>")
            return embed
    
        pages = [p1, p2, p3, p4, p5]


        try:
            embed = pages[página-1]()
            embed.set_footer(text=f"Solicitado por: {interaction.user.name}", icon_url=interaction.user.display_avatar)
            await interaction.response.send_message(embed=embed)
        except:
            embed = pages[0]()
            await interaction.response.send_message(f"Essa página não existe!", ephemeral=True)
            

def setup(bot):
    bot.add_cog(Help(bot))
import discord
import emoji
from discord.ext import commands
from discord import Option

class PossibleErrors(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Erros", style=discord.ButtonStyle.red, custom_id="possible_errors:button")
    async def callback(self, button, interaction: discord.Interaction):
        await interaction.response.defer()
        embed = discord.Embed(
            title="Erros Possíveis",
            description="```Não é um emoji```\n```Não foi possível adicionar a reação```\n```Eu não tenho permissões para adicionar reações```\n```O emoji não foi encontrado```\n```O parâmetro do emoji é inválido```",
            color=discord.Color(0xFF9090)
        )
        await interaction.edit_original_response(embed=embed, view=None)


class Enquete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.lower = "qwertyuiopasdfghjklzxcvbnm"
        self.numbers = "1234567890"
      
  
    @commands.slash_command(name="enquete", description="Faz uma enquete para os membros respondê-la")
    async def enquete(self, interaction: discord.Interaction, emoji1: Option(description="O primeiro emoji a ser colocado na enquete", required=True), emoji2: Option(description="O segundo emoji a ser colocado na enquete", required=True), pergunta: Option(str, description="A pergunta a ser feita para a comunidade", required=True), cor_da_mensagem: Option(description="A cor da mensagem para ser escolhida", choices=['Aleatório', 'Azul', 'Verde', 'Vermelho', 'Azuroxo (Blurple)', 'Roxo', 'Laranja', 'Dourado', 'Magenta', 'Verde-Azulado'], required=False)):
        await interaction.response.defer(ephemeral=True)
        if emoji.is_emoji(emoji1) is False or emoji.is_emoji(emoji2) is False:
            embed = discord.Embed(
                title="Ocorreu um erro!",
                description="Possíveis erros\n```É um emoji customizado (Não existe no Discord por padrão)```\n```Não é um emoji (Letras e/ou números)```",
                color=discord.Color(0xFF9090)
            )
            return await interaction.followup.send(embed=embed)

        if cor_da_mensagem == None:
            cor_da_mensagem = discord.Colour.blue()
      
        if cor_da_mensagem == "Aleatório":
            cor_da_mensagem = discord.Colour.random()
        if cor_da_mensagem == "Azul":
            cor_da_mensagem = discord.Colour.blue()
        if cor_da_mensagem == "Verde":
            cor_da_mensagem = discord.Colour.brand_green()
        if cor_da_mensagem == "Vermelho":
            cor_da_mensagem = discord.Colour.red()
        if cor_da_mensagem == "Azuroxo (Blurple)":
            cor_da_mensagem = discord.Colour.blurple()
        if cor_da_mensagem == "Roxo":
            cor_da_mensagem = discord.Colour.purple()
        if cor_da_mensagem == "Laranja":
            cor_da_mensagem = discord.Colour.orange()
        if cor_da_mensagem == "Dourado":
            cor_da_mensagem = discord.Colour.gold()
        if cor_da_mensagem == "Magenta":
            cor_da_mensagem = discord.Colour.magenta()
        if cor_da_mensagem == "Verde-Azulado":
            cor_da_mensagem = discord.Colour.teal()
      
        #try:
        embed = discord.Embed(
            title="**Enquete**",
            description=f"{pergunta}",
            color=cor_da_mensagem
        )
        channel = self.bot.get_channel(interaction.channel_id)
        await interaction.followup.send("Sua enquete será mandada...", ephemeral=True)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(emoji1)
        await msg.add_reaction(emoji2)

        #except:
            #embed = discord.Embed(
                #title=":sob: **|** Algo deu errado!",
                #description="Clique no botão abaixo para ver os possíveis erros.",
                #color=discord.Color(0xFF9090)
            #)
            #await interaction.followup.send(embed=embed, view=PossibleErrors(), ephemeral=True)
            
            


def setup(bot):
    bot.add_cog(Enquete(bot))
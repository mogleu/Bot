import discord
from discord.ext import commands
from discord import Option

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

class Erros(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Erros", style=discord.ButtonStyle.red, custom_id="erros:dm")
    async def button_callback(self, button, interaction: discord.Interaction):
        embed = discord.Embed(description="```O membro não tem as mensagens diretas ativadas para esse servidor.```", color=discord.Color.red())
        await interaction.response.edit_message(content="", embed=embed, view=None)


class DMs(commands.Cog):
    @commands.slash_command(name="dm", description="Manda uma mensagem direta para um membro.")
    async def dm(self, ctx: commands.Context, membro: Option(discord.Member, description="O membro que recebe a mensagem", required=True), *, mensagem: Option(description="A mensagem que o membro vai receber", required=True)):
        if membro.discriminator == "0":
            member = membro.name
        else:
            member = membro

        if ctx.author.discriminator.endswith("0"):
            ctx.author = ctx.author.name
        else:
            ctx.author = ctx.author

      
        try:      
            await membro.send(f"🛠️ Mensagem de {ctx.author}:\nMensagem: {mensagem}")
            await ctx.respond(f"Mensagem foi enviada com sucesso para {member}!")
        except discord.Forbidden:
            await ctx.respond(f"Não foi possível mandar mensagem para {member}, o código de erro é `discord.Forbidden`. Veja alguns erros clicando no botão abaixo.", view=Erros())
  
    @dm.error
    async def dm_error(self, ctx, error):
      if isinstance(error, discord.Forbidden):
        await ctx.respond(
          "Não foi possível mandar mensagem para {membro}, o código de erro é: `discord.Forbidden`",
          ephemeral=True)
      else:
        raise error


def setup(bot):
  bot.add_cog(DMs())

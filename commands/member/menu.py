import discord
from discord.ext import commands
from discord.ui import View

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


# Classes
class MySelect(View):
    @discord.ui.select(
       placeholder="Menu Principal do Bot",
       options=[
           discord.SelectOption(label="Python", value="1", description="Playlist de bot para iniciantes", emoji=f"<:Python:1076616945069203486>"),
           discord.SelectOption(label="Meu Canal no YouTube", value="2", description="@moguelrato on yt", emoji=f"<:YouTube:1076611782971494410>"),
           discord.SelectOption(label="Por onde começar a fazer um bot?", value="3", description="Primeiras impressões", emoji=f"<:Discord:1076678232788697109>"),
           discord.SelectOption(label="Feito por moguel.ye", value="4", emoji=f"<:Crown:1076621564667244655>")
       ]
    )

    async def select_callback(self, select, interaction):
        select.disabled=True
        if select.values[0] == "1":
            await interaction.response.send_message("https://youtube.com/playlist?list=PL9-YiBpH1Ne7NJlG9wGsEee24koLc8JTT",ephemeral=True)
        if select.values[0] == "2":
            await interaction.response.send_message("https://youtube.com/@moguelrato",ephemeral=True)
        if select.values[0] == "3":
            await interaction.response.send_message("Olá! Pronto para sua jornada?\nVamos começar.\nSe quiser ir direto pra programação sem mais nem menos, clique [**nesse link**](<https://pastebin.com/t5ydcyzB>), ele tem o código inteiro do bot para você copiar.\nSe quiser assistir o vídeo para entender o que eu fiz, clique [**nesse link**](<https://vimeo.com/843344539?share=copy>)",ephemeral=True)
        if select.values[0] == "4":
            await interaction.response.send_message("Dúvidas sobre bots no discord? Chama na dm! mogsdog#0011",ephemeral=True)


class Menu(commands.Cog):
    @bot.slash_command(name="menu", description="Manda um menu com 4 opções de seleções")
    async def menu(self, ctx):
        view = MySelect()
        await ctx.respond(view=view, ephemeral=True)


def setup(bot):
    bot.add_cog(Menu())
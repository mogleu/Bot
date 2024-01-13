import discord
import time
import aiohttp
import base64
from io import BytesIO
from discord.ext import commands
from discord import option
from main import bot


class Dropdown(discord.ui.Select):
    def __init__(self, message, images, user):
        self.message = message
        self.images = images
        self.user = user

        options=[
            discord.SelectOption(label="1"),
            discord.SelectOption(label="2"),
            discord.SelectOption(label="3"),
            discord.SelectOption(label="4"),
            discord.SelectOption(label="5"),
            discord.SelectOption(label="6"),
            discord.SelectOption(label="7"),
            discord.SelectOption(label="8"),
            discord.SelectOption(label="9"),
        ]

        super().__init__(
            placeholder="Selecione a imagem que você quer ver!",
            min_values=1,
            max_values=1,
            options=options
            )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        if not int(self.user) == int(interaction.user.id):
            await interaction.response.send_message("Você não é o autor dessa mensagem!", ephemeral=True)
        selection = int(self.values[0])-1
        image = BytesIO(base64.decodebytes(self.images[selection].encode("utf-8")))
        return await self.message.edit(content="Imagem gerada por **craiyon.com**", file=discord.File(image, "imagemGerada.png"), view=DropdownView(self.message, self.images, self.user))

class DropdownView(discord.ui.View):
    def __init__(self, message, images, user):
        super().__init__()
        self.message = message
        self.images = images
        self.user = user
        self.add_item(Dropdown(self.message, self.images, self.user))


class ImagemAI(commands.Cog):
    @commands.slash_command(name="imaginar", description="O bot cria uma imagem com o prompt descrito.")
    @option(name="prompt", description="O prompt de imagem a ser gerado.")
    async def imaginar_command(self, interaction: discord.Interaction, *, prompt: str):
        await interaction.response.defer()
        ETA = int(time.time() + 60)
        msg = await interaction.followup.send(content=f"Pegue um **>**:cookie:**<**, isso pode demorar um pouco... Tempo estimado de espera: <t:{ETA}:R>")
        async with aiohttp.request("POST", "https://backend.craiyon.com/generate", json={"prompt": prompt}) as resp:
            r = await resp.json()
            images = r['images']
            image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
            return await msg.edit(content="Imagem gerada por **craiyon.com**", file=discord.File(image, "imagemGerada.png"), view=DropdownView(msg, images, interaction.user.id))


def setup(bot):
    bot.add_cog(ImagemAI())
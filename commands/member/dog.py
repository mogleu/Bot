import discord
import requests
from discord.ext import commands

# Dog falar
import textwrap
from PIL import Image, ImageFont, ImageDraw
from discord import File, Option



class DogGroup(commands.Cog):
    dog = discord.SlashCommandGroup(name="dog")

    @dog.command(name='falar', description="Um dog fala o que você quiser (NÃO coloque uma frase longa!)")
    async def dog_falar(self, interaction: discord.Interaction, texto: Option(description="A mensagem que o dog vai falar", required=True)):
        msg ="".join(texto)
        font = ImageFont.truetype("./fonts/Ubuntu-Bold.ttf", 36)
        img = Image.open("./images/dog.jpg")
        cx, cy = (350, 230)

        lines = textwrap.wrap(msg, width=20)
        w, h = font.getsize(msg)
        y_offset = (len(lines)*h)/2
        y_text = cy-(h/2) - y_offset

        for line in lines:
            draw = ImageDraw.Draw(img)
            w, h = font.getsize(msg)
            draw.text((cx-(w/2), y_text), line, (0, 0, 0), font=font)
            img.save("./images/dog-edited.jpg")
            y_text += h

        with open("./images/dog-edited.jpg", "rb") as f:
            img = File(f)
            await interaction.response.send_message(file=img)

    @dog.command(name="foto", description="Manda uma foto aleatória de um cachorro")
    async def dog_foto(self, ctx):
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        res = r.json()
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=res['message'])
        await ctx.respond("Um dog aleatório da internet",embed=embed)


def setup(bot):
    bot.add_cog(DogGroup())
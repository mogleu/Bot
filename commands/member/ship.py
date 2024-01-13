import discord
import random
import io
from discord.ext import commands
from discord import Option
from PIL import Image, ImageFont, ImageDraw





class Ship(commands.Cog):
    @commands.slash_command(name="ship", description="Cheque se alguém é sua alma gêmea")
    async def ship(self, interaction: discord.Interaction, usuario1: Option(discord.Member, description="Primeiro usuário a shippar", required=True), usuario2: Option(discord.Member, description="Segundo usuário a shippar", required=True)):
        porcentagem = random.randint(0,100)
        metade1 = usuario1.name[:len(usuario1.name)//2]
        metade2 = usuario2.name[len(usuario2.name)//2:]
        nomeship = metade1 + metade2

        imagem1 = await usuario1.avatar.read()
        avatar1 = Image.open(io.BytesIO(imagem1))
        avatar1 = avatar1.resize((250,250))

        imagem2 = await usuario2.avatar.read()
        avatar2 = Image.open(io.BytesIO(imagem2))
        avatar2 = avatar2.resize((250,250))

        planodefundo = Image.new("RGB",(500,300),(56,56,56))
        planodefundo.paste(avatar1,(0,0))
        planodefundo.paste(avatar2,(250,0))

        fundodraw = ImageDraw.Draw(planodefundo)
        fundodraw.rounded_rectangle(((0,250),(500*(porcentagem/100),300)),fill=(207, 13, 48),radius=5)

        fonte = ImageFont.truetype("./fonts/RobotoMono-Bold.ttf", 32)
        fundodraw.text((230,255),f"{porcentagem}%",font=fonte)

        buffer = io.BytesIO()
        planodefundo.save(buffer,format="PNG")
        buffer.seek(0)

        if porcentagem <= 35:
            mensagem_extra = "😅 Não parece dar muito bem, mas quem sabe...?"
        elif porcentagem > 35 and porcentagem <= 65:
            mensagem_extra = "😀 Essa combinação tem potencial, que tal um jantar?"
        elif porcentagem > 65:
            mensagem_extra = "😍 Combinação perfeita! Quando será o casamento?"
    
        await interaction.response.send_message(content=f"<:coracao:1093536945335980164> **Hmm... Será que vamos ter um novo casal por aqui?** <:coracao:1093536945335980164>\n<:coracao2:1093538633304264785> {usuario1.mention} + {usuario2.mention} = ✨ `{nomeship}` ✨\n{mensagem_extra}", file=discord.File(fp=buffer,filename="file.png"))


def setup(bot):
    bot.add_cog(Ship())
import discord
from discord.ext import commands
from discord import File
from easy_pil import Editor, load_image_async, Font


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.discriminator == "0":
            membro = member.name

        else:
            membro = member
      
        channel = member.guild.system_channel
        
        background = Editor("./images/welcome/pic2.jpg")
        profile_image = await load_image_async(str(member.display_avatar))
        
        profile = Editor(profile_image).resize((150, 150)).circle_image()
        poppins = Font.poppins(size=50, variant="bold")
        
        poppins_small = Font.poppins(size=20, variant="light")

        background.paste(profile, (325, 90))
        background.ellipse((325, 90), 150, 150, outline="white", stroke_width=5)

        background.text((400, 260), f"BEM-VINDO EM {member.guild.name}!", color="white", font=poppins, align="center")
        background.text((400, 325), f"{membro}", color="white", font=poppins_small, align="center")

        file = File(fp=background.image_bytes, filename="./images/welcome/well.jpg")
        await channel.send(f"{member.mention}", file=file)


def setup(bot):
    bot.add_cog(Welcome(bot))
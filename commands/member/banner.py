import discord
from discord.ext import commands

class BannerButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Pack", style=discord.ButtonStyle.green, custom_id="pack:button", emoji="<:freitas_discord:1121476283273052171>")
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send(content="Se divirta! Neste momento há 68 banners dentro desse pack!", file=discord.File(fp="./banners/Banners.zip"))


class Banner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.slash_command(name="banners", description="Um pack de banners oficiais do Discord!")
    async def banners(self, ctx: commands.Context):
        class BannerButton(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
        
            @discord.ui.button(label="Pack", style=discord.ButtonStyle.green, custom_id="pack:button", emoji="<:freitas_discord:1121476283273052171>")
            async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.defer()
                #await msg.edit_original_response(content="Se divirta! Neste momento há 68 banners dentro desse pack!", file=discord.File(fp="./banners/Banners.zip"), embed=None, view=None)
                await msg.edit_original_response(content="Se divirta! Neste momento há 68 banners dentro desse pack!\nPara baixá-lo é só clicar na mensagem a seguir: [**O melhor pack de banners!**](<https://download942.mediafire.com/zbdi18nqkumgQsh5ALPExUhZ5Dz1X5ZstvAGkJyHXuqBwHLBRTUIUMFm_vYdK8CIAyu1wKWdal45ljVv0qrDGMg9775yLa8VPmXg1s2kQPefHGxEBDbt4tHWpltq-ec1KnnBM4rECGRNx49rBAhXWO2tqaOLueHc4HDNUtY6tEWdZlM/q3j62yvrntx7jb6/Banners.zip>)\n\nOBS: Se o Discord falar que é um arquivo malicioso, ignore, é um [**falso positivo**](<https://prnt.sc/21zIcEAcBMFE>)", embed=None, view=None)

        
        embed = discord.Embed(
            title="Banners",
            description="Clique no botão abaixo para baixar este pack com banners oficiais do Discord!",
            color=discord.Color.blurple()
        )
        msg = await ctx.respond(embed=embed, view=BannerButton())


def setup(bot):
    bot.add_cog(Banner(bot))
import discord
from discord.ext import commands
from discord import SlashCommandGroup, Option


class MCSkinView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
    
    @discord.ui.button(label="Download", style=discord.ButtonStyle.green, custom_id="download:button")
    async def button_download(self, button: discord.ui.Button, interaction: discord.Interaction, nickname):
        global user_id
        user_id = interaction.user.id
        await interaction.response.defer()
        embed = discord.Embed(
            title="**Skin Downloader**",
            description=f"Clique [**aqui**](https://mineskin.eu/download/{nickname}) para baixar a skin!",
            color=0x008525
        )
        await interaction.edit_original_response(embed=embed)


class MinecraftCommand(commands.Cog):
    minecraft = SlashCommandGroup("minecraft", "minecraft it cool")

    @minecraft.command(name="skin", description="Manda a skin de um player de Minecraft!")
    async def minecraft_skin(self, interaction: discord.Interaction, *, nickname: Option(description="O nickname do player para a skin ser mandada.", required=True)):
        global user_id
        user_id = interaction.user.id
        class MCSkinView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
                self.value = None
    
            @discord.ui.button(label="Download", style=discord.ButtonStyle.green)
            async def button_download(self, button: discord.ui.Button, interaction: discord.Interaction, nickname=nickname):
                await interaction.response.defer()
                if interaction.user.id == user_id:
                    embed = discord.Embed(
                        title="**Skin Downloader**",
                        description=f"Clique [**aqui**](https://mineskin.eu/download/{nickname}) para baixar a skin!",
                        color=0x008525
                    )
                    embed.set_thumbnail(url=f"https://mineskin.eu/helm/{nickname}/100.png")
                    embed.set_image(url=f"https://mineskin.eu/armor/body/{nickname}/100.png")
                    await interaction.edit_original_response(embed=embed, view=None)
                else:
                    #await interaction.followup.send(content=f"<:freitas_warn:1121106484646916117> **|** Ei, você não é <@{user_id}>! Saia daqui!", ephemeral=True)
                    await interaction.followup.send(content=f"<:freitas_warn:1121109353097871500> **|** Ei, você não é <@{user_id}>! Saia daqui!", ephemeral=True)
        
        
        nick_img = f"https://mineskin.eu/armor/body/{nickname}/100.png"
        embed = discord.Embed(
            title=f"Skin de `{nickname}`",
            color=discord.Color.random()
        )
        embed.set_image(url=nick_img)
        await interaction.response.send_message(embed=embed, view=MCSkinView())


def setup(bot):
    bot.add_cog(MinecraftCommand())
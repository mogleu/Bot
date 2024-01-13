import discord
import asyncio
from discord.ext import commands
from discord import Option
from discord.commands import SlashCommandGroup

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Infos(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    info = SlashCommandGroup("info", "Mostra informações sobre esse servidor")

    @info.command(name="servidor", description="Mostra informações sobre esse servidor")
    async def s(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=interaction.guild.name,
            color=discord.Color.blurple()
        )
        canais = len(interaction.guild.text_channels + interaction.guild.voice_channels)
        texto = len(interaction.guild.text_channels)
        voz = len(interaction.guild.voice_channels)
        users = len(interaction.guild.members)
    
        if interaction.user.discriminator == "0":
            autor = interaction.user.name
            a = interaction.user
        else:
            autor = interaction.user
            a = interaction.user
    
        embed.add_field(name=f"<:id_emoji:1119308368096538644> Identidade", value=f"```{interaction.guild.id}```")
        embed.add_field(name=f"<:Categoria:1119306847489376267> Canais: {canais}", value=f"<:CanaldeTexto:1119308816236957706> Texto: {texto}\n<:CanaldeVoz:1119309146550968360> Voz: {voz}")
        embed.add_field(name="<:members:1107438592466366517> Usuários", value=f"```{users} membros```")
        created = interaction.guild.created_at.timestamp()
        embed.add_field(name="<:IconCalendar:1114388877789122570> Servidor Criado", value=f"<t:{int(created)}:F> (<t:{int(created)}:R>)")
        joined = a.joined_at.timestamp()
        embed.add_field(name=f":rocket: {autor} entrou em", value=f"<t:{int(joined)}:F> (<t:{int(joined)}:R>)")
        embed.add_field(name="<:Coroa:1119309990369431623> Dono", value=f"{interaction.guild.owner.mention}\n`{interaction.guild.owner_id}`")
    
        await interaction.response.send_message(embed=embed)

    @info.command(name="user", description="Mostra informações sobre um usuário.")
    async def info_user(self, interaction: discord.Interaction, membro: Option(discord.Member, description="O membro que recebe a mensagem", required=False)):
        membro = membro or interaction.user
      
        if membro.discriminator == "0":
            member = membro.name
        else:
            member = membro

        
        info_embed = discord.Embed(color=discord.Color.blurple())
        info_embed.set_thumbnail(url=membro.display_avatar)
        info_embed.add_field(name="<:members:1107438592466366517> Nome", value=f"```{member}```", inline=True)
        info_embed.add_field(name="<:id_emoji:1119308368096538644> Identidade", value=f"```{membro.id}```", inline=True)
        info_embed.add_field(name="<:mencao:1107427357750476810> Menção", value=f"{membro.mention}", inline=True)
        created = membro.created_at.timestamp()
        info_embed.add_field(name="<:IconCalendar:1114388877789122570> Conta Criada", value=f'<t:{int(created)}:F> (<t:{int(created)}:R>)', inline=True)
        joined = membro.joined_at.timestamp()
        info_embed.add_field(name="<:IconEvent:1107439463862378516> Entrou em", value=f'<t:{int(joined)}:F> (<t:{int(joined)}:R>)', inline=False)
    
        await interaction.response.send_message(embed=info_embed)



def setup(bot):
    bot.add_cog(Infos(bot))
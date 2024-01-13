import discord
import uuid
from discord.ext import commands
from discord import Option
from discord.commands import SlashCommandGroup


class Key(commands.Cog):
    gerar = SlashCommandGroup("gerar", "Key")
    resgatar = SlashCommandGroup("resgatar", "Key System")

    @gerar.command(name="key", description="Um comando que gera quantas keys você quiser!")
    @commands.is_owner()
    async def gerar_key(self, interaction: discord.Interaction, quantidade: Option(int, description="A quantidade de keys a serem geradas.", required=True)):
        await interaction.response.defer(ephemeral=True)
      
        message = await interaction.followup.send(content="Key está sendo gerada, por favor espere...")
        
        key_amt = range(int(quantidade))
        f = open("./keys/keys.txt", "a")
        show_key = ''
        for x in key_amt:
            key = str(uuid.uuid4())
            show_key += "\n" + key
            f.write(key)
            f.write("\n")
    
        if len(str(show_key)) == 37:
            show_key = show_key.replace('\n', '')
            await interaction.user.send(content=f"Key: {show_key}")
            await message.edit(content="A key foi mandada em suas mensagens diretas!")
            return 0
        if len(str(show_key)) > 37:
            await interaction.user.send(content=f"Keys: {show_key}")
            await message.edit(content="A key foi mandada em suas mensagens diretas!")
            return 0
        else:
            await message.edit(content="Algo deu errado.", ephemeral=True)
            return 0

    @resgatar.command(name="key", description="Um comando que resgata keys")
    async def resgatar_key(self, interaction: discord.Interaction, key: Option(description="Insira sua key aqui para resgatá-la!", required=True)):
        await interaction.response.defer()
        if len(key) == 36:
            with open("keys/used keys.txt") as f:
                if key in f.read():
                    em = discord.Embed(color=0xff0000)
                    em.add_field(name="Key inválida", value="A key introduzida já foi regatada ou é inválida.")
                    await interaction.followup.send(embed=em)
                    return 0
            with open("keys/keys.txt") as f:
                if key in f.read():
                    role = discord.utils.get(interaction.guild.roles, name='Semi Co-Dono')
                    try:
                        await interaction.user.add_roles(role)
                    except discord.Forbidden:
                        await interaction.followup.send("Eu não tenho permissões para fazer isso! Este cargo do sorteio está acima do meu, para receber o seu cargo contate o dono (moguel.gg / moguel#0011) ou informe o seu problema ao staff.", file=discord.File("./images/key_cargo.png"), ephemeral=True)
                    em = discord.Embed(color=0x008525)
                    em.add_field(name="Key resgatada!", value="A sua key foi resgatada com sucesso!")
                    await interaction.followup.send(embed=em)
                    f = open("keys/used keys.txt", "a")
                    f.write(key)
                    f.write('\n')
                else:
                    em = discord.Embed(color=0xff0000)
                    em.add_field(name="Key inválida", value="A key introduzida já foi regatada ou é inválida.")
                    await interaction.followup.send(embed=em)
        else:
            em = discord.Embed(color=0xff0000)
            em.add_field(name="Key inválida", value="A key introduzida já foi regatada ou é inválida.")
            await interaction.followup.send(embed=em)

    @gerar_key
    async def gen_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("Você não tem permissões para fazer isso!", ephemeral=True)
        elif isinstance(error, commands.NotOwner):
            await ctx.respond("Você não pode usar esse comando! O seu id não corresponde a `680737419141971977`!", ephemeral=True)

    @resgatar.error
    async def res_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.respond("Eu não tenho permissões para fazer isso!", ephemeral=True)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.respond("Você não tem permissões para fazer isso!", ephemeral=True)


def setup(bot):
    bot.add_cog(Key())
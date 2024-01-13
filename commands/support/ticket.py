import discord
import os
from discord.ext import commands



class AddUser(discord.ui.Modal):
    def __init__(self, channel):
        super().__init__(
            title="Adicionar usuário ao ticket",
            timeout=None
        )
        self.channel = channel

        self.user = discord.ui.InputText(
            label="ID",
            min_length=2,
            max_length=30,
            required=True,
            placeholder="ID do Usuário (Precisa ser INT)"
        )
        self.add_item(self.user)

    async def callback(self, interaction: discord.Interaction) -> None:
        user = interaction.guild.get_member(int(self.user.value))
        if user is None:
            return await interaction.send(f"ID do usuário inválido, verifique-se se o usuário está neste servidor!")
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = True
        await self.channel.set_permissions(user, overwrite=overwrite)
        await interaction.response.send_message(content=f"O usuário: {user.mention} foi adicionado a esse ticket!")


class RemoveUser(discord.ui.Modal):
    def __init__(self, channel):
        super().__init__(
            title="Remover usuário do ticket",
            timeout=None
        )
        self.channel = channel

        self.user = discord.ui.InputText(
            label="ID",
            min_length=2,
            max_length=30,
            required=True,
            placeholder="ID do Usuário (Precisa ser INT)"
        )
        self.add_item(self.user)

    async def callback(self, interaction: discord.Interaction) -> None:
        user = interaction.guild.get_member(int(self.user.value))
        if user is None:
            return await interaction.send(f"ID do usuário inválido, verifique-se se o usuário está neste servidor!")
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = False
        await self.channel.set_permissions(user, overwrite=overwrite)
        await interaction.response.send_message(content=f"O usuário {user.mention} foi removido desse ticket!")


class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(
        label="Criar Ticket", style=discord.ButtonStyle.blurple, custom_id="criar_ticket", emoji="✉"
    )
    async def create_ticket(self, button: discord.ui.Button, interaction: discord.Interaction):
        global user_id
        user_id = interaction.user.id
        try:
            msg = await interaction.response.send_message("Criando ticket...", ephemeral=True)
            guild = interaction.guild
            role = discord.utils.get(guild.roles, name="Admin")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True),
                role: discord.PermissionOverwrite(view_channel=True)
                
            }
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name} ({interaction.user.id})", overwrites=overwrites)
            await msg.edit_original_response(content=f"Canal criado com sucesso! {channel.mention}")
            embed = discord.Embed(title=f"Ticket Criado", description=f"{interaction.user.mention} criou um ticket! Clique em algum botão abaixo para mudar as configurações.")
            await channel.send(embed=embed, view=TicketSettings())
        except AttributeError:
            await msg.edit_original_response(content="Você precisa ter um cargo com o nome de `Admin` criado!")
            #pass


class TicketSettings(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Adicionar Usuário", style=discord.ButtonStyle.green, custom_id="add_user", emoji="➕"
    )
    async def add_user(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(AddUser(interaction.channel))

    @discord.ui.button(
        label="Remover Usuário", style=discord.ButtonStyle.gray, custom_id="remove_user", emoji="❌"
    )
    async def remove_user(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(RemoveUser(interaction.channel))

    @discord.ui.button(
        label="Fechar Ticket", style=discord.ButtonStyle.red, custom_id="fechar_ticket", emoji="🔒"
    )
    async def close_ticket(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == user_id:
            messages = await interaction.channel.history(limit=None, oldest_first=True).flatten()
            contents = [message.content for message in messages]
            final = ""
            for msg in contents:
                msg = msg + "\n"
                final = final + msg
            with open('transcrição.txt', 'w') as f:
                f.write(final)
            await interaction.response.send_message("Fechando ticket...", ephemeral=True)
            await interaction.channel.delete()
            await interaction.user.send(f"Ticket fechado com sucesso! Aqui abaixo está o histórico de mensagens.", file=discord.File(r'transcrição.txt'))
            os.remove("transcrição.txt")
        else:
            await interaction.response.send_message(content="Você não pode fechar este ticket, só a pessoa que abriu pode fechá-lo!", ephemeral=True)


class Ticket(commands.Cog):
    @commands.slash_command(name='ticket', description="Um comando que cria um ticket de suporte")
    @commands.has_permissions(manage_guild=True)
    async def ticket(self, ctx: commands.Context):
        class TicketSettings(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
        
            @discord.ui.button(
                label="Adicionar Usuário", style=discord.ButtonStyle.green, custom_id="add_user", emoji="➕"
            )
            async def add_user(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.send_modal(AddUser(interaction.channel))
        
            @discord.ui.button(
                label="Remover Usuário", style=discord.ButtonStyle.gray, custom_id="remove_user", emoji="❌"
            )
            async def remove_user(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.send_modal(RemoveUser(interaction.channel))
        
            @discord.ui.button(
                label="Fechar Ticket", style=discord.ButtonStyle.red, custom_id="fechar_ticket", emoji="🔒"
            )
            async def close_ticket(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == user_id:
                    messages = await interaction.channel.history(limit=None, oldest_first=True).flatten()
                    contents = [message.content for message in messages]
                    final = ""
                    for msg in contents:
                        msg = msg + "\n"
                        final = final + msg
                    with open('transcrição.txt', 'w') as f:
                        f.write(final)
                    await interaction.response.send_message("Fechando ticket...", ephemeral=True)
                    await interaction.channel.delete()
                    await interaction.user.send(f"Ticket fechado com sucesso! Aqui abaixo está o histórico de mensagens.", file=discord.File(r'transcrição.txt'))
                    os.remove("transcrição.txt")
                else:
                    await interaction.response.send_message(content="Você não pode fechar este ticket, só a pessoa que abriu pode fechá-lo!", ephemeral=True)

        # ---------------------------
        # ---------------------------
        # ---------------------------
        embed = discord.Embed(
            title="Crie um ticket!",
            description='Clique no botão `Criar Ticket` abaixo para criar um ticket. Os admins irão ser notificados e vão te atender resolvendo o seu problema.',
        )
        await ctx.respond(embed=embed, view=CreateTicket())

    
def setup(bot):
    bot.add_cog(Ticket())
import discord
import json
import random
import os
from commands.economy.economy_functions import *
from discord.ext import commands
from discord import Option

os.chdir("./")

mainshop = [{"name": "Relógio de Pulso", "price": 100, "description": "Tempo"},
            {"name": "Laptop", "price": 1000, "description": "Trabalho"},
            {"name": "PC", "price": 10000, "description": "Jogos"},
            {"name": "Pizza", "price": 15, "description": "Comida"},
            {"name": "Boneco", "price": 20, "description": "Brincar"}]

intervals = (
    ('semanas', 604800),  # 60 * 60 * 24 * 7
    ('dias', 86400),    # 60 * 60 * 24
    ('horas', 3600),    # 60 * 60
    ('minutos', 60),
    ('segundos', 1),
)

leaderboard = ['1', '5', '10', '15', '20', '25']

# Database
from discord_cooldown.modules import SQlite
from discord_cooldown import cooldown
from datetime import timedelta

db = SQlite(filename="./commands/cooldowns/economy.db")
timezone = +timedelta(hours=-3, minutes=0)

def daily():
    return cooldown.Cooldown(database=db, timezone=timezone)

class Saldo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    economy = discord.SlashCommandGroup(name="economy")
  
    @economy.command(name="saldo", description="Um comando que mostra o seu saldo.")
    async def balance(self, ctx: commands.Context, membro: Option(discord.Member, description="O membro a ter as informações do Freitas Banco enviadas.", required=False)):
        user = membro or ctx.author
        await open_account(user)
        #await open_account(ctx.author)
        #await open_account(member)
        users = await get_bank_data()
    
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
    
        em = discord.Embed(title=f"Saldo de {user.name}", color=discord.Color.brand_green())
        em.add_field(name="Carteira", value=wallet_amt)
        em.add_field(name="Banco", value=bank_amt)
        await ctx.respond(embed=em)

    @commands.slash_command(name="daily", description="Um comando que você trabalha e ganha dinheiro.")
    #@work().cooldown(5, 86400)
    @daily().cooldown(1, 86400)
    async def daily_coins(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        
        #earnings = random.randint(10, 300)
        earnings = random.randint(1000, 1500)
        
        await ctx.respond(f":tada: **|** Você trabalhou e ganhou {earnings} <:freitascoin:1121957639522373724> **Freitas Coins**!")
        
        users[str(user.id)]["wallet"] += earnings
        
        with open("./commands/economy/bank.json", "w") as f:
            json.dump(users, f)

    @daily_coins.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            # Crusty function management
            global workuser
            if ctx.author.discriminator == "0":
                workuser = ctx.author.name + " (Pomelo)"

            else:
                workuser = ctx.author
            # End Crusty function management
            
            total = display_time(round(error.retry_after, 2), granularity=4)
            await ctx.respond(content=f'Este comando está em cooldown (O cooldown desse comando é de 1 dia, ou seja, você só pode usar o comando cinco vezes a cada um dia), tente novamente em {total}', ephemeral=True)
            print(f"[LOGS] - Economy cooldown check: {workuser}")
        else:
            return await daily().reset_cooldown(ctx.author, ctx.command.name)
            raise error
            

    @economy.command(name="retirar", description="Um comando que retira dinheiro do banco para a sua carteira.")
    async def withdraw(self, interaction: discord.Interaction, valor: Option(description="O valor para retirar.", required=True)):
        await open_account(interaction.user)
        if valor == None:
            await interaction.response.send_message("Por favor, coloque um valor.", ephemeral=True)
            return
                
            
        bal = await update_bank(interaction.user)
        
        valor = int(valor)
        if valor>bal[1]:
            await interaction.response.send_message("Você não tem todo este dinheiro!", ephemeral=True)
            return
            
        if valor<0:
            await interaction.response.send_message("O valor precisa ser positivo!", ephemeral=True)
            return
            
        await update_bank(interaction.user, valor)
        await update_bank(interaction.user, -1*valor, "bank")
        await interaction.response.send_message(f"Você retirou {valor} <:freitascoin:1121957639522373724> **Freitas Coins**!")

    @economy.command(name="depositar", description="Um comando que deposita seu dinheiro da carteira para o banco.")
    async def deposit(self, interaction: discord.Interaction, valor: Option(description="O valor a depositar.", required=True)):
        await open_account(interaction.user)
        if valor == None:
            await interaction.response.send_message("Por favor, coloque um valor.", ephemeral=True)
            return
                
            
        bal = await update_bank(interaction.user)
        
        valor = int(valor)
        if valor > bal[0]:
            await interaction.response.send_message("Você não tem todo este dinheiro!", ephemeral=True)
            return
            
        if valor < 0:
            await interaction.response.send_message("O valor precisa ser positivo!", ephemeral=True)
            return
            
        await update_bank(interaction.user, -1*valor)
        await update_bank(interaction.user, valor, "bank")
        await interaction.response.send_message(f"Você depositou {valor} <:freitascoin:1121957639522373724> **Freitas Coins**!")
      
    @economy.command(name="pix", description="Um comando que dá dinheiro para outro membro")
    async def give(self, interaction: discord.Interaction, membro: Option(discord.Member, description="O membro a ter os Freitas Coins recebidos.", required=True), valor: Option(description="O valor a ser dado ao membro.", required=True)):
        await open_account(interaction.user)
        await open_account(membro)
        if valor == None:
            await interaction.response.send_message("Por favor, coloque um valor.", ephemeral=True)
            return
        
            
        bal = await update_bank(interaction.user)
        
        valor = int(valor)
        if valor > bal[1]:
            await interaction.response.send_message("Você não tem todo este dinheiro ou ele não está no seu banco!", ephemeral=True)
            return
            
        if valor < 0:
            await interaction.response.send_message("O valor precisa ser positivo!", ephemeral=True)
            return
            
        await update_bank(interaction.user, -1*valor, "bank")
        await update_bank(membro, valor, "bank")
        embed = discord.Embed(
            title="<:freitas_pix:1123036824160436244> **|** Pix Enviado!",
            description=f"<:freitas_verified:1123399129851236433> **|** Sua transferência foi enviada com sucesso!\n\n> <:freitas_trade:1123037007908708452> **|** Remetente: {interaction.user.mention}\n\n> <:freitas_destinatario:1123037067451043840> **|** Destinatário: {membro.mention}\n\n> <:freitascoin:1121957639522373724> **|** Quantia recebida: `{valor}` Freitas Coins",
            color=discord.Color(0x11E1DA)
        )
        #await interaction.response.send_message(f"Você deu {valor} <:freitascoin:1121957639522373724> **Freitas Coins** para {membro.mention}!")
        await interaction.response.send_message(embed=embed)

    @economy.command(name="shop", description="Um comando que manda a loja do Freitas.")
    async def shop(self, interaction: discord.Interaction):
        em = discord.Embed(title="Freitas Shop", color=discord.Color.blurple())
        
        for item in mainshop:
            name = item["name"]
            price = item["price"]
            description = item["description"]
            em.add_field(name=name, value=f"${price} | {description}")
        
        await interaction.response.send_message(embed=em)

    @economy.command(name="comprar", description="Um comando que compra itens da loja.")
    async def buy(self, interaction: discord.Interaction, item: Option(description="O item a ser comprado.", required=True), valor: Option(description="A quantidade de itens a ser comprados.", required=False)):
        await open_account(interaction.user)
        valor=1
        
        res = await buy_this(interaction.user,item,valor)
        
        if not res[0]:
            if res[1]==1:
                await interaction.response.send_message("Esse item não está na loja!", ephemeral=True)
                return
            if res[1]==2:
                await interaction.response.send_message(f"Você não tem todo esse dinheiro para comprar {item}!", ephemeral=True)
                return
        
        
        await interaction.response.send_message(f"Você comprou {valor} {item}")

    @economy.command(name="inventario", description="Um comando que mostra o seu inventário.")
    async def bag(self, interaction: discord.Interaction, membro: Option(discord.Member, description="O membro a ter o inventário visualizado.", required=False)):
        user = membro or interaction.user
        #await open_account(ctx.author)
        await open_account(user)
        users = await get_bank_data()
        
        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = None

        if bag == None:
            em = discord.Embed(
                title=f"Inventário de {user.name}",
                description="Nada aqui.",
                color=discord.Color.brand_green()
            )

        else:
            em = discord.Embed(title = f"Inventário de {user.name}", color=discord.Color.brand_green())
            for item in bag:
                name = item["item"]
                amount = item["amount"]

                if amount == 0:
                    em = discord.Embed(
                        title=f"Inventário de {user.name}",
                        description="Nada aqui.",
                        color=discord.Color.brand_green()
                    )

                else:
                    em.add_field(name=name, value=amount)

        await interaction.response.send_message(embed = em)

    @economy.command(name="vender", description="Um comando que vende itens do seu inventário.")
    async def sell(self, interaction: discord.Interaction, item: Option(description="O item a ser vendido", required=True), valor: Option(description="A quantidade do item a ser vendido.", required=False)):
        await open_account(interaction.user)
        valor=1
        
        res = await sell_this(interaction.user,item,valor)
        
        if not res[0]:
            if res[1]==1:
                await interaction.response.send_message("Esse item não está na loja!", ephemeral=True)
                return
            if res[1]==2:
                await interaction.response.send_message(f"Você não tem {valor} {item} no seu inventário!", ephemeral=True)
                return
            if res[1]==3:
                await interaction.response.send_message(f"Você não tem {item} no seu inventário!", ephemeral=True)
                return
        
        await interaction.response.send_message(f"Você acabou de vender {valor} {item}")

    @economy.command(name="rank", description="Um comando que mostra o rank do servidor em base na economia.")
    async def leaderboard(self, interaction: discord.Interaction):
        await interaction.response.defer()
        x = 10
      
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)
    
        total = sorted(total,reverse=True)    
    
        em = discord.Embed(title = f"Top {x} pessoas mais ricas" , description = "Isso é decidido pela soma dos FC no banco e na carteira.",color = discord.Color(0xfa43ee))
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = self.bot.get_user(id_)
            name = member.name
            em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
            if index == x:
                break
            else:
                index += 1
    
        await interaction.followup.send(embed = em)


def setup(bot):
    bot.add_cog(Saldo(bot))
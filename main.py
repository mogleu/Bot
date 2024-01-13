import discord
import os
import shutil
from website.website import keep_alive
from discord.ext import commands
from dotenv import load_dotenv


# DotEnv
load_dotenv()


# Classes
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            # Ticket
            self.add_view(CreateTicket())
            self.add_view(TicketSettings())
            # Minecraft
            self.add_view(MCSkinView())
            # Verify
            self.add_view(VerifyButton())
            self.add_view(VerifyBAmigao())
            # Music
            self.add_view(YTError())
            self.persistent_views_added = True

        print(f"[LOGS] - Conectado em {self.user}")
        print(f"[LOGS] - ID: {self.user.id}")
        print(f"[LOGS] - 🔮 Views persistentes ativadas! 🔮")
        #await bot.change_presence(activity=discord.Game(name='.help'))
        
        # Poetry
        try:
            os.remove("pyproject.toml")
        except FileNotFoundError:
            pass
      
        # Music
        try:
            shutil.rmtree('./music')
            os.mkdir("./music")
        except FileNotFoundError:
            pass
          
        # Economy
        os.chdir("./")


# Definir
TOKEN = os.getenv("DISCORD_TOKEN")

ID = os.getenv("DISCORD_ID")

bot = Bot(command_prefix=".", intents=discord.Intents.all(), help_command=None, owner_id=680737419141971977, application_id=ID)

bot.remove_command('help')

# For and Import Commands
#For
for fn in os.listdir("./commands/member"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.member.{fn[:-3]}")

for fn in os.listdir("./commands/moderation"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.moderation.{fn[:-3]}")

for fn in os.listdir("./commands/music"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.music.{fn[:-3]}")

for fn in os.listdir("./commands/level"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.level.{fn[:-3]}")

for fn in os.listdir("./commands/economy"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.economy.{fn[:-3]}")

for fn in os.listdir("./commands/verification"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.verification.{fn[:-3]}")

for fn in os.listdir("./commands/support"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.support.{fn[:-3]}")

for fn in os.listdir("./events"):
    if fn.endswith(".py"):
        bot.load_extension(f"events.{fn[:-3]}")


# Import Commands
from commands.support.ticket import CreateTicket, TicketSettings
from commands.member.minecraft import MCSkinView
from commands.verification.universal import VerifyButton
from commands.verification.amigao import VerifyBAmigao
from commands.music.music import YTError

# Essential commands
@bot.command(name="load", description="Um comando que carrega outros comandos")
async def load(ctx, grupo, extensão):
    userid = 680737419141971977
    if not (ctx.author.id == userid):
        await ctx.send(f"Você não tem permissão para usar esse comando!")
        return
    bot.load_extension(f"commands.{grupo}.{extensão}")
    await ctx.send("Comando carregado!")


@bot.command(name="reload", description="Um comando que recarrega outros comandos")
async def reload(ctx, grupo, extensão):
    userid = 680737419141971977
    if not (ctx.author.id == userid):
        await ctx.send(f"Você não tem permissão para usar esse comando!")
        return
    bot.reload_extension(f"commands.{grupo}.{extensão}")
    await ctx.send("Comando recarregado!")


@bot.command(name="unload", description="Um comando que descarrega outros comandos")
async def unload(ctx, grupo, extensão):
    userid = 680737419141971977
    if not (ctx.author.id == userid):
        await ctx.send(f"Você não tem permissão para usar esse comando!")
        return
    bot.unload_extension(f"commands.{grupo}.{extensão}")
    await ctx.send("Comando descarregado!")


keep_alive()
  
bot.run(TOKEN)
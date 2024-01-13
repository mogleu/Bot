from discord.ext import commands

# Classes
class StartVerification(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("[LOGS] - ✔️  Sistema de Verificação carregado! ✔️")
        

def setup(bot):
    bot.add_cog(StartVerification())
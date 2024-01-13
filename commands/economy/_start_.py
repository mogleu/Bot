from discord.ext import commands

# Classes
class StartEconomy(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("[INFO] - Carregando economy...")
        print("[LOGS] - 📦 Database carregada! 📦")
        

def setup(bot):
    bot.add_cog(StartEconomy())
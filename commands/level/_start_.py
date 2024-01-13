from discord.ext import commands

# Classes
class StartLevel(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("[INFO] - Carregando level...")
        

def setup(bot):
    bot.add_cog(StartLevel())
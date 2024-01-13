from discord.ext import commands

# Classes
class StartDead(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("[INFO] - Carregando music...")
        

def setup(bot):
    bot.add_cog(StartDead())
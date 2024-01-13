from discord.ext import commands

# Classes
class StartMember(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("[INFO] - Carregando member...")
        

def setup(bot):
    bot.add_cog(StartMember())
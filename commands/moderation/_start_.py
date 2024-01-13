from discord.ext import commands

# Classes
class StartModeration(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print("[INFO] - Carregando moderation...")
        

def setup(bot):
    bot.add_cog(StartModeration())
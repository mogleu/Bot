import discord
from discord.ext import commands

class WhenMentioned(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
  
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mention in message.content.split():
            embed = discord.Embed(
                description=":wave: **|** Olá! Eu sou o **Freitas Bot**, o bot **perfeito** para a sua comunidade. O meu prefixo é **.** Precisa de ajuda? Use o comando /help",
                color=discord.Color(0xFF9090)
            )
            #await message.channel.send("You can type `!vx help` for more info")
            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(WhenMentioned(bot))
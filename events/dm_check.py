import discord
from discord.ext import commands
from main import bot


class Events(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild:
            if message.author == bot.user:
                return
              
            msg = str(message)
            if message.author.id == bot.owner_id and msg.startswith("."):
                return 0
            else:
                # Pomelo check
                if message.author.discriminator == "0" or "0000":
                    user = message.author.name

                else:
                    user = message.author
              
                embed = discord.Embed(
                    description="Hey! Eu não consigo ver sua mensagem porque eu sou um bot! Se quiser falar ou entrar em contato comigo, mande mensagem para o meu dono. Discord do meu dono: `moguel.gg` **ou** `moguel#0011`\n\nOBS: **Isso é uma mensagem automática!**",
                    color=discord.Color.brand_green()
                )
                #await message.channel.send("Hey! Eu não consigo ver sua mensagem porque eu sou um bot! Se quiser falar ou entrar em contato comigo, mande mensagem para o meu dono. Discord do meu dono: `moguel.gg` **ou** `moguel#0011`")
                await message.author.send(embed=embed)
                print(f"[LOGS] - DM Check para {user}")


def setup(bot):
    bot.add_cog(Events())
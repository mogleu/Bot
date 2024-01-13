import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Say(commands.Cog):
    @bot.slash_command(name="say", description="Falo a mensagem que você quiser!")
    async def say(self, ctx, *, frase=None):
        if frase == None:
            await ctx.respond(f"Você não especificou o que eu tenho que falar!", ephemeral=True)
        else:
            await ctx.respond(f"{frase}")


def setup(bot):
    bot.add_cog(Say())
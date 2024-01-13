import discord
import requests
from discord.ext import commands
from discord import Option

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


class Clima(commands.Cog):
    @commands.slash_command(name="clima", description="Mostra informações sobre o clima de uma cidade")
    async def clima(self, ctx, *, cidade: Option(description="A cidade a ter as informações enviadas.", required=True)):
        api_key = '7dad1ecb6a4987c31e8df0b1c430c150'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            clima = data['weather'][0]['description']
            temperatura = data['main']['temp']
            umidade = data['main']['humidity']
            mensagem = f'O clima em {cidade} é {clima}, a temperatura é {temperatura:.1f} °C e a umidade é {umidade}%'
            await ctx.respond(mensagem)
        else:
            await ctx.respond(f'Não foi possível obter informações sobre o clima em {cidade}')


def setup(bot):
    bot.add_cog(Clima())
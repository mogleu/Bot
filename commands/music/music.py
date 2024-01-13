import discord
import yt_dlp
import re
import datetime
import asyncio
from discord.ext import commands
from discord import Option

url_correction = re.compile(r'https?://(?:www\.)?.+')


class YTError(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Erros", style=discord.ButtonStyle.red, custom_id="erros:button")
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        embed = discord.Embed(
            title="Erros Possíveis",
            description="```É uma livestream```\n```Não foi possível fazer o download da música```\n```O formato não é suportado. Formatos suportados: 𝗠𝗣𝟰, 𝗙𝗟𝗩 e 𝗪𝗲𝗯𝗠```\n```O URL/Link é inválido```\n```O site não é suportado```",
            color=discord.Color.dark_red()
        )
        await interaction.edit_original_response(embed=embed, view=None)

class PlayDownload(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Download", style=discord.ButtonStyle.green, custom_id="play:button")
    async def play_button(self, button: discord.ui.Button, interaction: discord.Interaction, attachment):
        await interaction.response.defer()
        embed = discord.Embed(
                title="File Music Downloader",
                description=f"Clique [**aqui**]({attachment.url}) para fazer o download dessa música.",
                color=discord.Color.blurple()
            )
        await interaction.followup.send(embed=embed)
        #await interaction.followup.send(f"Clique [**aqui**]({filename}) para fazer o download dessa música.")


class Music(commands.Cog):
    def __init__(self):
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'quiet': True, 'socket_timeout': 10, 'nocheckcertificate': True, 'logtostderr': False, 'cachedir': False, 'extractor_args': {
        'youtube': {
            'skip': [
                'hls',
                'dash'
            ],
            'player_skip': [
                'js',
                'configs',
                'webpage'
            ]
        }}}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        self.is_playing = False
        self.loop = False

    async def after_playing(self, voice_client):
        self.is_playing = False
        self.loop = False

    async def play_loop(self, ctx, url, loop: bool):
        if self.is_playing is False or self.loop is False:
            return
        else:
            with yt_dlp.YoutubeDL(self.YDL_OPTIONS) as ydl:
                song = ydl.extract_info(url, download=False)
    
            vc = ctx.voice_client
            url2 = song['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **self.FFMPEG_OPTIONS)
            vc.play(source, after=lambda e: asyncio.run(self.play_loop(ctx, url, loop=True)))
            self.loop = True
  
    music = discord.SlashCommandGroup(name="music")
    play = music.create_subgroup(name="play")

    @commands.command(name="yt-test")
    async def yt_test(self, ctx):
        await ctx.send(view=YTError())

    @play.command(name="universal", description="Um comando que toca músicas de várias plataformas.")
    async def play_universal(self, ctx: commands.Context, url: Option(description="O URL/Link da música.", required=True), loop: Option(description="O modo do loop da música. O padrão se não selecionado é desligado.", choices=['Ligado', 'Desligado'], required=False)):
        if loop == None:
            loop = "Desligado"
      
        await ctx.defer()
        try:
            voiceChannel = ctx.author.voice.channel
            if not ctx.voice_client:
                await voiceChannel.connect()
            if ctx.author.voice is None:
                embed = discord.Embed(
                    description="Para tocar uma música, primeiro se conecte a um canal de voz.",
                    color=discord.Color.brand_green()
                )
                #await ctx.edit(content="Você não está em um canal de voz!")
                await ctx.edit(embed=embed)
            else:
                pass

            if self.is_playing is True:
                embed = discord.Embed(
                    title="Erro!",
                    description="Uma música já está sendo tocada, espere por sua vez.",
                    color=discord.Color.brand_green(),
                )
                #await ctx.edit(content="Uma música já está sendo tocada, espere por sua vez.")
                return await ctx.edit(embed=embed)

            if "tiktok" in url:
                embed = discord.Embed(
                    title="Mãos na cabeça!",
                    description="EI! Pare agora mesmo! Eu não posso tocar links do TikTok se não eu sou deletado :(\nFica só entre nós dois viu?!",
                    color=discord.Color.brand_green()
                )
                return await ctx.edit(content="", embed=embed)
          
            with yt_dlp.YoutubeDL(self.YDL_OPTIONS) as ydl:
                song = ydl.extract_info(url, download=False)
                video_duration = song.get('duration', None)
        
            vc = ctx.voice_client
            url2 = song['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **self.FFMPEG_OPTIONS)
            #vc.play(await discord.FFmpegOpusAudio.from_probe(song["url"], **FFMPEG_OPTIONS))
            embed = discord.Embed(
                color=discord.Color.red(),
                description=f"> [**{song['title']}**]({url})"
            )
            embed.set_author(name="Tocando Agora:", icon_url="https://cdn.discordapp.com/attachments/480195401543188483/895862881105616947/music_equalizer.gif")
            embed.set_thumbnail(url=song['thumbnail'])
            embed.set_image(url="https://cdn.discordapp.com/attachments/554468640942981147/1095082863843627153/rainbow_bar.gif")
          
            if "twitch" in url:
                duration = "`?:??:??`"
            else:  
                duration = str(datetime.timedelta(seconds=video_duration))
          
            embed2 = discord.Embed(
                description=f"> ⏰ **⠂Duração:** `{duration}`\n> 💠 **⠂Uploader**: `{song['uploader']}`\n> 🎧 **⠂Pedido por:** {ctx.author.mention}",
                color=discord.Color.red()
            )
            #await ctx.edit(content=f'Tocando agora: [**Solicitado por {ctx.author}**]({url})')
            ##vc.play(source, after=lambda e: await self.after_playing(vc))
            if loop == "Ligado":
                vc.play(source, after=lambda e: asyncio.run(self.play_loop(ctx, url, loop=True)))
                self.loop = True
            else:
                vc.play(source, after=lambda e: asyncio.run(self.after_playing(vc)))
            self.is_playing = True
            await ctx.edit(embed=embed)
            await ctx.channel.send(embed=embed2)
        except yt_dlp.DownloadError:
            vc = ctx.voice_client
            await vc.disconnect()
            embed = discord.Embed(
                title="Ocorreu um erro!",
                description="Verifique abaixo interagindo com o botão `Erros` para saber se seu erro aparece.",
                color=discord.Color.dark_red()
            )
            await ctx.edit(embed=embed, view=YTError())
        #except AttributeError:
            #embed = discord.Embed(
                #description="Para tocar uma música, primeiro se conecte a um canal de voz.",
                #color=discord.Color.brand_green()
            #)
            #######await ctx.edit(content="Você não está em um canal de voz!")
            #await ctx.edit(embed=embed)

        # ---------------------------------------------------
        # ---------------------------------------------------
        # ---------------------------------------------------
        # ---------------------------------------------------
        # ---------------------------------------------------  
        # ---------------------------------------------------

    @play.command(name="arquivo", description="Um comando que toca músicas de um arquivo.")
    async def play_file(self, ctx, arquivo: discord.Attachment):
        await ctx.defer()
        class PlayDownload(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
            
            @discord.ui.button(label="Download", style=discord.ButtonStyle.green, custom_id="play:button")
            async def play_button(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.defer()
                embed = discord.Embed(
                    title="File Music Downloader",
                    description=f"Clique [**aqui**]({arquivo.url}) para fazer o download dessa música.",
                    color=discord.Color.brand_green()
                )
                #await interaction.followup.send(f"Clique [**aqui**](<{attachment.url}>) para fazer o download dessa música.")
                await interaction.followup.send(embed=embed)

        if arquivo.filename.endswith(".mp3"):
            path = "./music/song.mp3"
            x = ".mp3"
        if arquivo.filename.endswith(".mp4"):
            path = "./music/song.mp4"
            x = ".mp4"

        voiceChannel = ctx.author.voice.channel
        try:
           await voiceChannel.connect()
        except discord.errors.ClientException:
            pass
        if ctx.author.voice == None:
            embed = discord.Embed(
                    description="Para tocar uma música, primeiro se conecte a um canal de voz.",
                    color=discord.Color.brand_green()
                )
                #await ctx.edit(content="Você não está em um canal de voz!")
            await ctx.edit(embed=embed)

        if self.is_playing is True:
            embed = discord.Embed(
                    title="Erro!",
                    description="Uma música já está sendo tocada, espere por sua vez.",
                    color=discord.Color.brand_green(),
                )
            #await ctx.edit(content="Uma música já está sendo tocada, espere por sua vez.")
            return await ctx.edit(embed=embed)
        
        await arquivo.save(fp=path)
        source = discord.FFmpegOpusAudio(path)
        vc = ctx.voice_client
        vc.play(source, after=lambda e: asyncio.run(self.after_playing(vc)))
        embed = discord.Embed(
            #title=f"> [**{filename.title()}{x}**]({attachment.url})",
            #description=f"> [**{filename.title()}{x}**]({attachment.url})"
            description=f"> [{arquivo.filename}]({arquivo.url})",
            color=discord.Color.red()
        )
        embed.set_author(name="Tocando Agora:", icon_url="https://cdn.discordapp.com/attachments/480195401543188483/895862881105616947/music_equalizer.gif")
        #await ctx.respond(f"Tocando agora [**{filename.title()}{x}**]({attachment.url})")
        await ctx.edit(embed=embed, view=PlayDownload())

    # ---------------------------------------------------
    # ---------------------------------------------------
    # ---------------------------------------------------
    # ---------------------------------------------------
    # ---------------------------------------------------  
    # ---------------------------------------------------

    @music.command(name="pause", description="Um comando que pausa músicas que estão tocando.")
    async def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = discord.Embed(
                description="Eu não estou em um canal de voz!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)
      
        if self.is_playing is False:
            embed = discord.Embed(
                description="Nenhuma música está tocando no momento!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)
        vc = ctx.voice_client
        embed = discord.Embed(
            color=ctx.me.color,
            description="> **A sua música foi pausada.**"
        )
        embed.set_author(name="Em pausa", icon_url="https://cdn.discordapp.com/attachments/480195401543188483/896013933197013002/pause.png")
        vc.pause()
        self.is_playing = False
        #await ctx.respond("A música foi pausada.")
        await ctx.respond(embed=embed)

    @music.command(name="retomar", description="Um comando que retoma músicas que estão pausadas.")
    async def resume(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = discord.Embed(
                description="Eu não estou em um canal de voz!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)

        if self.is_playing is True:
            embed = discord.Embed(
                    description="Uma música já está tocando, não consigo retomar ela!",
                    color=discord.Color.brand_green(),
                )
            #await ctx.edit(content="Uma música já está sendo tocada, espere por sua vez.")
            return await ctx.respond(embed=embed)
        vc = ctx.voice_client
        embed = discord.Embed(
            description="> **A sua música foi retomada.**",
            color=ctx.me.color
        )
        embed.set_author(name="De volta!", icon_url="https://cdn.icon-icons.com/icons2/3641/PNG/512/play_blue_button_icon_227848.png")
        vc.resume()
        self.is_playing = True
        #await ctx.respond("A música foi retomada.")
        await ctx.respond(embed=embed)

    @music.command(name="stop", description="Um comando que para a música tocando.")
    async def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = discord.Embed(
                description="Eu não estou em um canal de voz!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)

        if not self.is_playing:
            embed = discord.Embed(
                description="Nenhuma música está tocando no momento!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)
        vc = ctx.voice_client
        embed = discord.Embed(
            description="> **A sua música foi parada.**",
            color=ctx.me.color
        )
        embed.set_author(name="Acabar música, câmbio!", icon_url="https://cdn.icon-icons.com/icons2/3641/PNG/512/stop_red_button_icon_227856.png")
        vc.stop()
        await self.after_playing(vc)
        #await ctx.respond("A música foi parada.")
        await ctx.respond(embed=embed)

    @music.command(name="desconectar", description="O bot desconecta do canal de voz.")
    async def disconnect(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = discord.Embed(
                description="Eu não estou em um canal de voz!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)
        vc = ctx.voice_client
        embed = discord.Embed(
            description="> **Espero te ver novamente!**",
            color=ctx.me.color
        )
        embed.set_author(name="Tchau tchau!", icon_url="https://cdn.discordapp.com/emojis/1117261832814600305.webp?size=128&quality=lossless")
        await vc.disconnect()
        self.is_playing = False
        #await ctx.respond("Tchau tchau!")
        await ctx.respond(embed=embed)

    @commands.command(name="volume", description="Um comando que altera o volume da música atual.")
    async def volume(self, ctx: commands.Context, volume: Option(int, description="A quantidade de volume para alterar.", required=True)):
        if not ctx.voice_client:
            embed = discord.Embed(
                description="Eu não estou em um canal de voz!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)

        if not self.is_playing:
            embed = discord.Embed(
                    description="Nenhuma música está tocando no momento, não consigo alterar o volume!",
                    color=discord.Color.brand_green(),
                )
            #await ctx.edit(content="Uma música já está sendo tocada, espere por sua vez.")
            return await ctx.respond(embed=embed)

        if volume > 100 or volume < 0:
            embed = discord.Embed(
                description="O volume precisa ser entre 0 e 100!",
                color=discord.Color.brand_green()
            )
            return await ctx.respond(embed=embed)

        vc = ctx.voice_client
        embed = discord.Embed(
            description=f"O volume foi alterado para {volume}%",
            color=discord.Color.brand_green()
        )
        vc.volume = float(volume) / 100
        self.is_playing = True
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Music())
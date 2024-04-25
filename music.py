import discord
from discord.ext import commands
import youtube_dl
import urllib.parse
import urllib.request
import json
import re

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_client = None
        self.queue = []

    @commands.command(name="join", help="Faz o Biscatinho entrar no canal de voz em que você está.")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Você não está em um canal de voz.")
            return
        if self.voice_client is not None and self.voice_client.is_connected():
            await self.voice_client.move_to(ctx.author.voice.channel)
        else:
            self.voice_client = await ctx.author.voice.channel.connect()
        await ctx.send(f"Biscatinho entrou no canal de voz {ctx.author.voice.channel}.")

    @commands.command(name="leave", help="Faz o Biscatinho sair do canal de voz.")
    async def leave(self, ctx):
        if self.voice_client is not None and self.voice_client.is_connected():
            await self.voice_client.disconnect()
            self.voice_client = None
            self.queue = []
            await ctx.send("Biscatinho saiu do canal de voz.")
        else:
            await ctx.send("Biscatinho não está em nenhum canal de voz.")

    @commands.command(name="play", help="Toca uma música do YouTube.")
    async def play(self, ctx, *, query: str):
        if self.voice_client is None or not self.voice_client.is_connected():
            await ctx.send("Biscatinho não está em nenhum canal de voz.")
            return

        # Busca o vídeo no YouTube com base no nome da música
        query_string = urllib.parse.urlencode({"search_query": query})
        html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        url = "https://www.youtube.com/watch?v=" + search_results[0]

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2)

        if self.voice_client.is_playing():
            self.queue.append(source)
            await ctx.send("Música adicionada à fila.")
        else:
            self.voice_client.play(source)
            await ctx.send("Tocando música.")

    @commands.command(name="skip", help="Pula a música atual.")
    async def skip(self, ctx):
        if self.voice_client is not None and self.voice_client.is_playing():
            self.voice_client.stop()
            await ctx.send("Música pulada.")
        else:
            await ctx.send("Biscatinho não está tocando nada.")

    @commands.command(name="queue", help="Mostra a fila de músicas.")
    async def queue(self, ctx):
        if len(self.queue) > 0:
            queue_str = "Fila de músicas:\n"
            for i, song in enumerate(self.queue):
                queue_str += f"{i + 1}: {song}\n"
            await ctx.send(queue_str)
        else:
            await ctx.send("Não há músicas na fila.")

    @commands.command(name="clear", help="Limpa a fila de músicas.")
    async def clear(self, ctx):
        self.queue = []
        await ctx.send("Fila de músicas limpa.")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.bot.user and after.channel is None and self.voice_client is not None:
            self.voice_client = None
            self.queue = []

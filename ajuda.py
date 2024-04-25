import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
intents.message_content = True

class ajuda_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """

```
Comandos disponíveis:
!help = Mostra todos os comandos disponíveis.
!toca <nomedamusica> - Toca uma música do YouTube no seu canal atual.
!listarmusica- Mostra a música atual.
!tocaproxima - Pula para a próxima música.
!limpa - Para a música e limpa a fila.
!sai - Remove Biscatinho da chamada de voz.
!para - Pausa a música atual ou retoma a reprodução se já estiver pausada.
!despausar - Despausa a musica atual
```
"""
        self.text_channel_list = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)
        await self.send_to_all(self.help_message)        

    @commands.command(name="help", aliases=["ajudabiscatinho", "comandos", "biscatinhohelp", "ajuda"], help="Mostra todos os comandos disponíveis.")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
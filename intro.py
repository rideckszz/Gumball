import discord
import asyncio
from discord.ext import commands

class intro_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mensagens = {
            '!gumball': 'Oi, no que posso te ajudar?',
            '!seapresente': 'Oiers, eu sou o Gumball, o bot do servidor. No que posso te ajudar?',
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        mensagem = message.content
        if mensagem in self.mensagens:
            await message.channel.send(self.mensagens[mensagem])

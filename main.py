# Imports de libs e afins
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


# Imports de comandos
from intro import intro_cog
from ajuda import ajuda_cog
from music import music_cog
from produtos import produtos_cog
#

# Intents 
intents = discord.Intents.all()
intents.messages = True

# Código
bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command('help') 

@bot.event
async def on_ready ():
    await bot.add_cog(ajuda_cog(bot))
    await bot.add_cog(intro_cog(bot))
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(produtos_cog(bot))

load_dotenv()
TOKEN = os.getenv('TOKEN')

if TOKEN:
    bot.run(TOKEN)
else:
    print("TOKEN is not set in the .env file.")

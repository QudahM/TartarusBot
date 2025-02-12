import discord, os, asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

initial_extensions = ['cogs.events', 'cogs.commands', 'cogs.tasks']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(TOKEN)
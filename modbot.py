import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

# Correct paths for extensions
initial_extensions = ['cogs.events', 'cogs.commands', 'cogs.tasks']

class MyBot(commands.Bot):
    async def setup_hook(self):
        for ext in initial_extensions:
            try:
                await self.load_extension(ext)  # Load extensions inside setup_hook
                print(f"✅ Loaded {ext}")
            except Exception as e:
                print(f"❌ Failed to load {ext}: {type(e).__name__} - {e}")

bot = MyBot(command_prefix="&", intents=intents)  # Define bot BEFORE using it

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

if __name__ == "__main__":
    bot.run(TOKEN)  # Use bot.run() instead of asyncio.run()
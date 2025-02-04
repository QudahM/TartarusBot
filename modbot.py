import discord
from discord.ext import commands, tasks
import pytz
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_USER_ID = int(os.getenv("DISCORD_TARGET", 0))
GUILD_ID = int(os.getenv("DISCORD_GUILD", 0))

intents = discord.Intents.default()
intents.members = True  # Required for accessing members
intents.guilds = True  # Ensure guild access
#interesting intents
intents.presences = True
intents.messages = True
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

async def timeout_member():
    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(TARGET_USER_ID)
    duration = timedelta(seconds=1800)
    reason = "COMEBACK TO HELL MY SON"
    await member.timeout(duration, reason=reason)
    print(f"Timed out {member.display_name} at {datetime.now()}")

@tasks.loop(minutes=1)
async def daily_timeout():
    est = pytz.timezone('US/Eastern')
    now = datetime.now(est)

#someone is getting timed out at 10:29 PM EST
    if now.hour == 22 and now.minute == 29:
        await timeout_member()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    daily_timeout.start()

@daily_timeout.error
async def timeout_error(error):
    print(f"An error occurred: {error}")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def manual_timeout(ctx):
    await timeout_member()
    await ctx.send("Timed out user")

if __name__ == '__main__':
    bot.run(TOKEN)
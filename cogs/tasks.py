from discord.ext import commands, tasks
import pytz
from datetime import datetime
from utils.timeout_member import timeout_member  # Ensure this import is correct
import os

try:
    DISCORD_CHANNEL = [int(ch.strip()) for ch in os.getenv('DISCORD_CHANNEL', "").split(',') if ch.strip().isdigit()]
    DISCORD_TARGET = [int(uid.strip()) for uid in os.getenv('DISCORD_TARGET', "").split(',') if uid.strip().isdigit()]
except ValueError as e:
    print(f"❌ ERROR: Invalid environment variable format: {e}")
    DISCORD_CHANNEL = []
    DISCORD_TARGET = []

print(f"Loaded DISCORD_TARGET: {DISCORD_TARGET}")  # Debugging
print(f"Loaded DISCORD_CHANNEL: {DISCORD_CHANNEL}")  # Debugging

class BackgroundTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_timeout.start()  # Ensure the task starts when the bot loads

    @tasks.loop(minutes=1)
    async def daily_timeout(self):
        est = pytz.timezone('US/Eastern')
        now = datetime.now(est)

        if now.hour == 5 and now.minute == 36:  # Adjusted for testing
            print(f"Executing daily_timeout at {now.hour}:{now.minute} EST")
            await self.process_guilds()

    async def process_guilds(self):
        print(f"Processing guilds...")  # Debugging
        for guild in self.bot.guilds:
            print(f"Processing guild: {guild.name}")  # Debugging
            await self.process_users_and_channels(guild)

    async def process_users_and_channels(self, guild):
        print(f"Processing users and channels in {guild.name}...")  # Debugging
        for user_id, channel_id in zip(DISCORD_TARGET, DISCORD_CHANNEL):
            print(f"Processing user {user_id} in channel {channel_id}...")  # Debugging
            await self.timeout_user_in_channel(guild, user_id, channel_id)

    async def timeout_user_in_channel(self, guild, user_id, channel_id):
        member = guild.get_member(user_id)
        channel = guild.get_channel(channel_id)

        if not member:
            print(f"❌ ERROR: Could not find member with ID {user_id} in {guild.name}")
            return

        if not channel:
            print(f"❌ ERROR: Could not find channel with ID {channel_id} in {guild.name}")
            return

        print(f"Attempting to timeout {member.display_name} in {channel.name}")  # Debugging
        await timeout_member(member, channel)  # Call the function directly

async def setup(bot):
    await bot.add_cog(BackgroundTasks(bot))
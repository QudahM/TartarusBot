from discord.ext import commands, tasks
import pytz
from datetime import datetime
from utils.timeout_utils import timeout_member
import os

TARGET_CHANNELS = list(map(int, os.getenv('TARGET_CHANNELS').split(',')))
TARGET_USERS = list(map(int, os.getenv('TARGET_USERS').split(',')))

class BackgroundTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=1)
    async def daily_timeout(self):
        est = pytz.timezone('US/Eastern')
        now = datetime.now(est)

        if now.hour == 0 and now.minute == 0:
            for guild in self.bot.guilds:
                for user_id, channel_id in zip(TARGET_USERS, TARGET_CHANNELS):
                    memeber = guild.get_member(user_id)
                    channel = guild.get_channel(channel_id)

                    if memeber and channel and channel.permissions_for(memeber).send_messages:
                        await timeout_member(memeber, channel)
                        print(f"Successfully timed out {memeber} in {channel}")
                    else:
                        print(f"Could not timeout {memeber} in {channel}")

def setup(bot):
    bot.add_cog(BackgroundTasks(bot))

daily_timeout = BackgroundTasks.daily_timeout
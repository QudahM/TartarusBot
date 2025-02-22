from discord.ext import commands
import asyncio

# from utils.timeout_member import timeout_member

class EventHandlers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has connected to Discord!')

        while not self.bot.get_cog('BackgroundTasks'):
            print("Waiting for BackgroundTasks to load...")
            await asyncio.sleep(2)

        background_tasks = self.bot.get_cog('BackgroundTasks')

        if hasattr(background_tasks, "daily_timeout") and not background_tasks.daily_timeout.is_running():
            background_tasks.daily_timeout.start()
            print("✅ Started daily timeout task")

async def setup(bot):
    await bot.add_cog(EventHandlers(bot))

from discord.ext import commands
from cogs.tasks import daily_timeout

class EventHandlers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has connected to Discord!')
        daily_timeout.start(self.bot)

    @daily_timeout.error
    async def timeout_error(self, error):
        print(f"An error occurred: {error}")

def setup(bot):
    bot.add_cog(EventHandlers(bot))
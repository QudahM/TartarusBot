import discord
from discord.ext import commands
from utils.timeout_utils import timeout_member

class TimeoutCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='manual_timeout')
    @commands.has_permissions(moderate_messages=True)
    async def manual_timeout(self, ctx, member_name: str, channel_name: str):
        member = discord.utils.find(lambda m: m.name == member_name or m.display_name == member_name, ctx.guild.members)
        channel = discord.utils.find(ctx.guild.channels, name=channel_name)

        if member and channel:
            await timeout_member(member, channel)
            await ctx.send(f"Successfully timed out {member_name} in {channel_name}")
        else:
            if not member:
                await ctx.send(f"Could not find member {member_name}")
            if not channel:
                await ctx.send(f"Could not find channel {channel_name}")

def setup(bot):
    bot.add_cog(TimeoutCommands(bot))
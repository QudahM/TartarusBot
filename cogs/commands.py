import discord
from discord.ext import commands
from utils.timeout_member import timeout_member  # Ensure this import is correct

class TimeoutCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='manual_timeout')
    @commands.has_permissions(moderate_members=True)
    async def manual_timeout(self, ctx, member_name: str, channel_name: str):
        member = discord.utils.find(lambda m: m.name == member_name or m.display_name == member_name, ctx.guild.members)
        channel = discord.utils.find(lambda c: c.name == channel_name, ctx.guild.channels)

        if member is None:
            await ctx.send(f"❌ ERROR: Could not find member `{member_name}`")
            return
        if channel is None:
            await ctx.send(f"❌ ERROR: Could not find channel `{channel_name}`")
            return

        await timeout_member(member, channel)  # Call the function directly
        await ctx.send(f"✅ Successfully timed out {member.mention} in {channel.mention}")

async def setup(bot):
    await bot.add_cog(TimeoutCommands(bot))  # DO NOT AWAIT THIS
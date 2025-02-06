import discord 
from discord.ext import commands, tasks # Needed for bot
import pytz # Needed for timezone
from datetime import datetime, timedelta # Needed for time
import asyncio # Needed for sleep
import os # Needed for environment variables
from dotenv import load_dotenv 

# Load the environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL", 0))  # Keep the channel ID you want to target
TARGET_USER_ID = int(os.getenv("DISCORD_TARGET", 0))  # Keep the user ID you want to target

# Create a bot instance with the necessary intents
intents = discord.Intents.default() 
intents.members = True # Member object
intents.guilds = True # Guild object
intents.presences = True # Presence object
intents.messages = True # Message object
intents.message_content = True # Message content

# Create a bot instance with the necessary intents and command prefix (&)
bot = commands.Bot(command_prefix='&', intents=intents)

async def timeout_member(member, channel):

    try:
        # Send a message to the channel before timing out the user
        await channel.send(f"The shadows of Tartarus whisper your name {member.mention} 3...")
        await asyncio.sleep(1)
        await channel.send("Say your goodbyes 2...")
        await asyncio.sleep(1)
        await channel.send("Or not 1...")
        await asyncio.sleep(1)
        await channel.send("HAHAHAHAHA 🔥🔥🔥")

        # Timeout the user
        duration = timedelta(seconds=43)
        reason = "COMEBACK TO HELL MY SON"
        
        # Timeout the user
        await member.timeout(duration, reason=reason)
        print(f"Timed out {member.display_name} in {member.guild.name} at {datetime.now()}")
    except Exception as e:
        print(f"Failed to timeout {member.display_name} in {member.guild.name}: {e}")

@tasks.loop(minutes=1)
async def daily_timeout():
    est = pytz.timezone('US/Eastern')
    now = datetime.now(est)

    # Trigger at 10:29 PM EST
    if now.hour == 5 and now.minute == 8:
        for guild in bot.guilds:
            # Get the member and channel
            member = guild.get_member(TARGET_USER_ID)
            channel = guild.get_channel(TARGET_CHANNEL_ID)
            
            # Check if the member is in the guild and if the bot has permissions to send messages in the channel
            if member and channel and channel.permissions_for(guild.me).send_messages:
                await timeout_member(member, channel)
            else:
                print(f"Failed to find channel or send message in {guild.name}")

# Event to print the bot's name when it connects to Discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    daily_timeout.start()

# Event to handle errors
@daily_timeout.error
async def timeout_error(error):
    print(f"An error occurred: {error}")

# Command to manually timeout a user
@bot.command()
@commands.has_permissions(moderate_members=True)
async def manual_timeout(ctx):
    # Get the member and channel
    member = ctx.guild.get_member(TARGET_USER_ID)
    channel = ctx.guild.get_channel(TARGET_CHANNEL_ID)
    if member and channel:
        # Timeout the user from the whole server 
        await timeout_member(member, channel)
        await ctx.send(f"Timed out {member.display_name}")
    else:
        await ctx.send("User not found in this server.")

if __name__ == '__main__':
    bot.run(TOKEN)

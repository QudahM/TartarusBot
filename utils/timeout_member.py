import asyncio, discord
from datetime import datetime, timedelta, timezone

async def timeout_member(member, channel):
    try:
        # Check if the bot has the 'moderate_members' permission
        if not member.guild.me.guild_permissions.moderate_members:
            print("❌ ERROR: Bot lacks `moderate_members` permission!")
            return

        # Send countdown messages
        countdown_message = [
            f"The shadows of Tartarus whisper your name {member.mention} 3...",
            "Say your goodbyes 2...",
            "Or not 1...",
            "HAHAHAHAHA 🔥🔥🔥"
        ]
        for message in countdown_message:
            try:
                await channel.send(message)
                await asyncio.sleep(1)
            except discord.Forbidden:
                print(f"❌ ERROR: Bot does not have permission to send messages in {channel.name}!")
                return
            except discord.HTTPException as e:
                print(f"❌ ERROR: Failed to send message in {channel.name}. Error: {e}")
                return

        # Timeout the member
        utc_now = datetime.now(timezone.utc)
        duration = timedelta(seconds=8)  # Adjusted for testing
        reason = "COMEBACK TO ME MY SON"

        try:
            await member.edit(timed_out_until=utc_now + duration, reason=reason)
            print(f"✅ Timed out {member.display_name} in {member.guild.name} at {datetime.now()}")
        except discord.Forbidden:
            print(f"❌ ERROR: Bot does not have permission to timeout {member.display_name}!")
        except discord.HTTPException as e:
            print(f"❌ ERROR: Failed to timeout {member.display_name}. Error: {e}")

    except Exception as e:
        print(f"❌ Failed to timeout {member.display_name} in {member.guild.name}. Error: {e}")
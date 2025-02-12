import asyncio # asyncio is a library to write concurrent code using the async/await syntax.
from datetime import timedelta, datetime

async def timeout_member(member, channel):
    try:
        countdown_message = [
            f"The shadows of Tartarus whisper your name {member.mention} 3...",
            "Say your goodbyes 2...",
            "Or not 1...",
            "HAHAHAHAHA 🔥🔥🔥"
        ]
        for message in countdown_message:
            await channel.send(message)
            await asyncio.sleep(1)
        
        duration = timedelta(hours=8)
        reason = "COMEBACK TO ME MY SON"

        await member.timeout(duration=duration, reason=reason)
        print(f"Timed out {member.display_name} in {member.guild.name} at {datetime.now()}")
    except Exception as e:
        print(f"Failed to timeout {member.display_name} in {member.guild.name}. Error: {e}")
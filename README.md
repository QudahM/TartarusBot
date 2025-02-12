# TartarusBot

Summoned from the depths of Greek mythology, TartarusBot is no ordinary Discord bot—it's the warden of your server's underworld. Inspired by the ancient abyss where the Titans were imprisoned, this bot ensures no mischief goes unpunished. Built using `modbot.py`, TartarusBot combines playful theatrics with powerful moderation, delivering scheduled timeouts and custom commands worthy of the gods themselves.

## Features

- **Scheduled Timeouts**: Automatically times out a specified user daily at a set time.
- **Manual Timeout Command**: Manually trigger a timeout for a targeted user with the `&manual_timeout` command.
- **Customizable Messages**: Sends dramatic, themed messages before timing out a user.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/QudahM/TartarusBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd TartarusBot
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory and add your bot token, target channel ID, and target user ID:
    ```env
    DISCORD_TOKEN=your_bot_token_here
    DISCORD_CHANNEL=target_channel_id_here
    DISCORD_TARGET=target_user_id_here
    ```

2. **DISCORD_TOKEN**: Your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. **DISCORD_CHANNEL**: The ID of the channel where the bot will send messages.
4. **DISCORD_TARGET**: The ID of the user to be timed out.

## Usage

Run the bot using the following command:
```bash
python modbot.py
```

### Commands

- `&manual_timeout`: Manually triggers a timeout for the specified user.

### Scheduled Timeout

The bot automatically times out the specified user every day at **5:08 AM EST** with dramatic countdown messages.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please open an issue on the GitHub repository.


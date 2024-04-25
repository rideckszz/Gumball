
# Gumball Discord Bot

Gumball is a Discord bot developed using Python and the Discord.py library. This bot provides various features including playing music from YouTube, searching for products, initiating chat with an AI, and more.

## Features

- **Music Player**: Gumball can join a voice channel and play music from YouTube. You can queue up multiple songs and manage the playback.
- **Product Listing**: Gumball allows users to list products and make purchases using Pix as the payment method.
- **Chat with AI**: Initiate a conversation with the ChatGPT AI directly within your Discord server. Currently off for maintenance
- **Command Aliases**: Gumball understands multiple command names for the same action to provide a more user-friendly experience.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain API keys as needed (e.g., OpenAI for chat functionality, Discord Token for music functionality) and update the configuration accordingly.

## Usage

1. Run the bot script:

    ```bash
    python bot.py
    ```

2. Invite Gumball to your Discord server using the OAuth2 URL generated after running the bot script.
3. Use the available commands to interact with Gumball and enjoy its features!

## Commands

- `!join`: Makes Gumball join the voice channel you're currently in.
- `!leave`: Makes Gumball leave the voice channel.
- `!play <song_name>`: Plays a song from YouTube based on the provided song name.
- `!skip`: Skips the currently playing song.
- `!queue`: Shows the current queue of songs.
- `!clear`: Clears the song queue.
- `!list_products`: Lists the available products for purchase.
- `!buy <product_name>`: Buys the specified product using Pix as the payment method.
- `!chat <message>`: Initiates a chat with the ChatGPT AI.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or new features to propose, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

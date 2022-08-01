# discord-bot-template
Simple reply discord bot template using discord's python library

# Requirements:
## Dependencies
It requires [`python 3.10.5`](https://www.python.org/downloads/) or newer. Using [pip](https://pip.pypa.io/en/stable/installation/), install the discord python library:
```shell
pip3 install discord
```

## Set up a bot account
1. Follow the steps [**here**](https://docs.pycord.dev/en/master/discord.html) to setup and invite a discord bot
2. Copy bot token and paste the token on the `discord_bot.py`
```python
import random
import discord

# Initialize discord client object
client = discord.Client()

# Paste your bot token here
TOKEN = 'TOKEN_HERE'
# Customize here the words that will trigger the bot
key_words = ["funny", "example1", "example2"]
```

Here, you can also modify the words that will trigger your bot. 
The file `quotes.txt` is what the bot reads when searching for a response. Modify this file accordingly.

## Finally, run your discord bot:
```shell
python3 discord_bot.py
```

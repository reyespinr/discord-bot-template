#!/usr/bin/env python3
"""
Simple reply discord bot template using discord's python library
"""
__author__ = "Nathan Reyes"
__version__ = "0.1.0"
__license__ = "MIT"

import random
import discord

# Initialize discord client object
client = discord.Client()

# Paste your bot token here
TOKEN = 'TOKEN_HERE'
# Customize here the words that will trigger the bot
key_words = ["funny", "example1", "example2"]


def get_quote():
    with open("quotes.txt", 'r') as file:
        quotes = file.readlines()
    quote = random.choice(quotes)
    return quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore all of its own messages
    if message.author == client.user:
        return

    # Checks if message contains any of the trigger words
    # if so, it picks a random quote from the txt file
    if any(word in message.content for word in key_words):
        response = get_quote()
        await message.channel.send(response)

    # Special word trigger example
    if "secret message" in message.content: 
        await message.channel.send("Hilarious response :sob:")

    # Make bot join ur channel
    if message.author.voice: 
        if "join me" in message.content: 
            await message.author.voice.channel.connect()
        if "leave now" in message.content: 
            await message.guild.voice_client.disconnect()

def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()


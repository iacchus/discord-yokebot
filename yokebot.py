#!/usr/bin/env python

import os

import discord

YOKEBOT_TOKEN = os.getenv("DISCORD_TOKEN") or exit(1)

intents = discord.Intents.default()

yokebot = discord.Client(intents=intents)

@yokebot.event
async def on_ready():
    print('logged as', yokebot.user)

@yokebot.event
async def on_message(message):
    print('new message from', message.author, "on", message.channel)
    if message.author != yokebot.user:
        await message.channel.send(f'hey, {message.author}!')

yokebot.run(token=YOKEBOT_TOKEN)



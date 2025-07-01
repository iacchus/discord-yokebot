#!/usr/bin/env python

import os

import discord

YOKEBOT_TOKEN = os.getenv("DISCORD_TOKEN") or exit(1)

intents = discord.Intents.default()


class YokeBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('logged as', self.user)

    async def on_message(self, message):
        print('new message from', message.author, "on", message.channel.name)
        if message.author != self.user:
            await message.channel.send(f'hey, {message.author}!')

yokebot = YokeBot(intents=intents)

yokebot.run(token=YOKEBOT_TOKEN)



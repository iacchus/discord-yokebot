#!/usr/bin/env python

import datetime
import os

import discord

from discord.ext import tasks

YOKEBOT_TOKEN = os.getenv("DISCORD_TOKEN") or exit(1)

intents = discord.Intents.default()

BRT = datetime.timezone(offset=-datetime.timedelta(hours=3))
hours = [0, 6, 12, 18]
times = [datetime.time(hour=hour, tzinfo=BRT) for hour in hours]
times.append(datetime.time(hour=18, minute=54, tzinfo=BRT))


class YokeBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        self.my_bg_task.start()

    @tasks.loop(time=times)
    async def my_bg_task(self):
        await self.channel.send(f'time is come')  # pyright: ignore

    @my_bg_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

    async def on_ready(self):
        self.channel = self.get_channel(1389484905951658067)
        print('logged as', self.user)

    async def on_message(self, message):
        print('new message from', message.author, "on", message.channel.name)
        if message.author != self.user:
            await message.channel.send(f'hey, {message.author}!')

yokebot = YokeBot(intents=intents)

yokebot.run(token=YOKEBOT_TOKEN)



#!/usr/bin/env python

import datetime
import json
import os
import random

import discord

from discord.ext import tasks

from functions import get_dhammapada

#  SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
#  DHAMMAPADA_JSON_FILEPATH = f"{SCRIPT_PATH}/dhammapada.json"

YOKEBOT_TOKEN = os.getenv("DISCORD_TOKEN") or exit(1)

intents = discord.Intents.default()

BRT = datetime.timezone(offset=-datetime.timedelta(hours=3))
hours = [0, 6, 12, 18]
times = [datetime.time(hour=hour, tzinfo=BRT) for hour in hours]
times.append(datetime.time(hour=23, minute=56, tzinfo=BRT))


#  def get_dhammapada_verse():
#      with open(DHAMMAPADA_JSON_FILEPATH, "r") as dhammapada_json_file:
#          dhammapada_json = json.load(dhammapada_json_file)
#
#      keys = dhammapada_json.keys()
#      random_choice = random.choice(list(keys))
#
#      return dhammapada_json[random_choice]


class YokeBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        self.dhammapada_task.start()

    @tasks.loop(time=times)
    async def dhammapada_task(self):
        dhammapada = get_dhammapada(as_codeblock=False, no_line_breaks=True)
#          verse_numbers, verse = get_dhammapada_verse()
#          verses = ", ".join([str(verse_number) for verse_number in verse_numbers])
#          signature = f"— Dhammapada {verses}"
#
#          message = f"""\
#  ```
#  {verse}
#
#  {signature}
#  ```\
#  """
        #  await self.channel.send(f'time is come')  # pyright: ignore
        #  await self.channel.send(message)  # pyright: ignore
        await self.channel.send(dhammapada)  # pyright: ignore

    @dhammapada_task.before_loop
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



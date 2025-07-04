import json
import os
import random
import re

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
DHAMMAPADA_JSON_FILEPATH = f"{SCRIPT_PATH}/dhammapada.json"

dhammapada_message = """\
{codeblock}\
{verse}

{signature}
{codeblock}\
"""

def get_dhammapada(as_codeblock=True, no_line_breaks=True):
    with open(DHAMMAPADA_JSON_FILEPATH, "r") as dhammapada_json_file:
        dhammapada_json = json.load(dhammapada_json_file)

    keys = dhammapada_json.keys()
    random_choice = random.choice(list(keys))

    verse_numbers, verse = dhammapada_json[random_choice]
    verses = ", ".join([str(verse_number) for verse_number in verse_numbers])
    signature = f"— Dhammapada {verses}"

    codeblock = "```" if as_codeblock else ""  # or just remove newline

    message = dhammapada_message.format(verse=verse,
                                        signature=signature,
                                        codeblock=codeblock)

    dhammapada = re.sub('(.)\n(?!\n)', r'\1 ', message) \
                 if no_line_breaks \
                 else message

    dhammapada = "\n".join([f"> {line}" for line in dhammapada.splitlines()])

    return dhammapada

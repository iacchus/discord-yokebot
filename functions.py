import json
import os
import random

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
DHAMMAPADA_JSON_FILEPATH = f"{SCRIPT_PATH}/dhammapada.json"

dhammapada_message = """\
```
{verse}

{signature}
```\
"""

def get_dhammapada():
    with open(DHAMMAPADA_JSON_FILEPATH, "r") as dhammapada_json_file:
        dhammapada_json = json.load(dhammapada_json_file)

    keys = dhammapada_json.keys()
    random_choice = random.choice(list(keys))

    #  return dhammapada_json[random_choice]
    verse_numbers, verse = dhammapada_json[random_choice]
    verses = ", ".join([str(verse_number) for verse_number in verse_numbers])
    signature = f"— Dhammapada {verses}"

    return dhammapada_message.format(verse=verse, signature=signature)


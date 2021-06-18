import random
import requests
from BackgroundsJSON import backgrounds

def get_random_background():
    imported_backgrounds = backgrounds

    base_backgrounds = []

    for background in imported_backgrounds["results"]:
        base_backgrounds.append(background["name"])

    random_background = random.choice(base_backgrounds)

    return random_background


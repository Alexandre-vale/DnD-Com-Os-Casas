import random
import requests


def get_random_background():
    base_url_backgrounds = "http://127.0.0.1:5000/backgrounds"

    base_url_background = "http://127.0.0.1:5000/"

    background_api = requests.get(base_url_backgrounds)

    background_json = background_api.json()

    base_backgrounds = {}

    for background in background_json["results"]:
        base_backgrounds[background["name"]] = base_url_background + background["url"]

    random_background = random.choice(list(base_backgrounds.items()))

    return random_background

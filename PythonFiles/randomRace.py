import requests
import random


def get_random_race():
    base_url_race = "https://www.dnd5eapi.co/api/races/"

    base_url_subrace = "https://www.dnd5eapi.co"

    all_races_api = requests.get(base_url_race)

    all_races_json = all_races_api.json()

    base_races = {}

    for race in all_races_json["results"]:
        base_races[race["name"]] = base_url_race + race["index"]

    random_race = random.choice(list(base_races.items()))

    random_race_info_api = requests.get(random_race[1])

    random_race_info_json = random_race_info_api.json()

    if len(random_race_info_json["subraces"]) == 0:
        return random_race
    else:
        all_races = {random_race[0]: random_race[1]}
        for subraces in random_race_info_json["subraces"]:
            all_races[subraces["name"]] = base_url_subrace + subraces["url"]
        return random.choice(list(all_races.items()))
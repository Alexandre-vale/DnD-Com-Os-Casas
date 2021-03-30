import requests
import random


def get_random_race():
    base_url = "https://www.dnd5eapi.co/api/races/"

    base_url_subrace = "https://www.dnd5eapi.co"

    all_base_races = requests.get(base_url)

    base_races_json = all_base_races.json()

    base_races = {}

    for race in base_races_json["results"]:
        base_races[race["name"]] = base_url + race["index"]

    random_race = random.choice(list(base_races.items()))

    race_info_api = requests.get(random_race[1])

    race_info_json = race_info_api.json()

    if len(race_info_json["subraces"]) == 0 :
        return random_race
    else:
        all_races = {random_race[0]: random_race[1]}

        for subraces in race_info_json["subraces"]:
            all_races[subraces["name"]] = base_url_subrace + subraces["url"]

        return random.choice(list(all_races.items()))


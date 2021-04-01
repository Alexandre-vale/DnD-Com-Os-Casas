import requests


def get_race_info(race_url):
    race_info_api = requests.get(race_url)

    race_info_json = race_info_api.json()

    if race_info_json["index"] == "human" or race_info_json["index"] == "half-elf":
        race_info = {"Speed": 0, "Size": 0,
                     "Ability_Bonuses": 0,
                     "Languages": 0, "Language_Options": 0,
                     "Traits": 0,
                     "Starting_Proficiencies": 0}
    else:
        if "starting_proficiency_options" in race_info_json:
            race_info = {"Speed": 0, "Size": 0,
                         "Ability_Bonuses": 0,
                         "Languages": 0,
                         "Traits": 0,
                         "Starting_Proficiencies": 0, "Starting_Proficiency_Options": 0}
        else:
            race_info = {"Speed": 0, "Size": 0,
                         "Ability_Bonuses": 0,
                         "Languages": 0,
                         "Traits": 0,
                         "Starting_Proficiencies": 0}

    for keys in race_info:
        race_info[keys] = race_info_json[keys.lower()]

    return race_info

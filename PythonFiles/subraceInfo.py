import requests
import random


def get_subrace_info(subrace_url):
    subrace_info_api = requests.get(subrace_url)

    subrace_info_json = subrace_info_api.json()

    original_race_url = "https://www.dnd5eapi.co" + subrace_info_json["race"]["url"]

    original_race_info_api = requests.get(original_race_url)

    original_race_info_json = original_race_info_api.json()

    if "racial_trait_options" in subrace_info_json:
        random_racial_trait_options = random.choice(subrace_info_json['racial_trait_options']['from'])
        subrace_info = {"Speed": original_race_info_json["speed"], "Size": original_race_info_json["size"],
                        "Ability_Bonuses": subrace_info_json["ability_bonuses"] + original_race_info_json["ability_bonuses"],
                        "Languages": original_race_info_json["languages"],
                        "Language_Options": 0,
                        "Traits": original_race_info_json["traits"] + subrace_info_json["racial_traits"] + [random_racial_trait_options],
                        "Starting_Proficiencies": original_race_info_json["starting_proficiencies"] + subrace_info_json["starting_proficiencies"]}
    else:
        if "starting_proficiency_options" in original_race_info_json:
            random_proficiency_options = random.choice(original_race_info_json['starting_proficiency_options']['from'])
            subrace_info = {"Speed": original_race_info_json["speed"], "Size": original_race_info_json["size"],
                            "Ability_Bonuses": subrace_info_json["ability_bonuses"] + original_race_info_json["ability_bonuses"],
                            "Languages": original_race_info_json["languages"],
                            "Language_Options": 0,
                            "Traits": original_race_info_json["traits"] + subrace_info_json["racial_traits"],
                            "Starting_Proficiencies": original_race_info_json["starting_proficiencies"] + subrace_info_json["starting_proficiencies"] + [{"name":random_proficiency_options["name"]}]}
        else:
            subrace_info = {"Speed": original_race_info_json["speed"], "Size": original_race_info_json["size"],
                            "Ability_Bonuses": subrace_info_json["ability_bonuses"] + original_race_info_json["ability_bonuses"],
                            "Languages": original_race_info_json["languages"],
                            "Language_Options": 0,
                            "Traits": original_race_info_json["traits"] + subrace_info_json["racial_traits"],
                            "Starting_Proficiencies": original_race_info_json["starting_proficiencies"] + subrace_info_json["starting_proficiencies"]}
    if "language_options" in subrace_info_json:
        subrace_info["Language_Options"] = subrace_info_json["language_options"]

    return subrace_info

import requests
import random
import numpy as np
from BackgroundsJSON import backgrounds

def get_background_info(background_name):
    selected_background = next(back for back in backgrounds["results"] if back["name"] == background_name)
    #print(selected_background)

def get_background_info(background_url, imported_languages):
    background_info_api = requests.get(background_url)

    background_info_json = background_info_api.json()

    background_info_from_api = {"Language_Options": None,
                                "Starting_Proficiencies": None,
                                "Starting_Proficiencies_Options": None,
                                "Starting_Equipment": None,
                                "Starting_Equipment_Options": None,
                                "Gold": None}

    background_info = {}

    for keys in background_info_from_api:
        if keys.lower() not in selected_background:
            background_info_from_api[keys] = None
        else:
            background_info_from_api[keys] = selected_background[keys.lower()]

    # Language Info
    if background_info_from_api["Language_Options"] != None:
        number_of_random_languages = background_info_from_api["Language_Options"]["choose"]
        background_language_raw = background_info_from_api["Language_Options"]["from"]
        background_language_pool = [x for x in background_language_raw if x not in imported_languages]
        random_languages = np.random.choice(background_language_pool,
                                            size=number_of_random_languages,
                                            replace=False)
        # random_languages = random.choices(list(background_info_from_api["Language_Options"]["from"]),
                                          # k=number_of_random_languages)

        background_info["Languages"] = [random_language["name"] for random_language in random_languages]
    else:
        background_info["Languages"] = []

    # Starting Proficiencies Info
    if background_info_from_api["Starting_Proficiencies"] != None:
        background_info["Starting_Proficiencies"] = [proficiency["name"] for proficiency in
                                                     background_info_from_api["Starting_Proficiencies"]]
    else:
        background_info["Starting_Proficiencies"] = []

    # Starting Proficiencies Options Info
    base_url_prof_options = "https://www.dnd5eapi.co/api/equipment-categories/"
    if background_info_from_api["Starting_Proficiencies_Options"] != None:
        url_prof_option = base_url_prof_options + background_info_from_api["Starting_Proficiencies_Options"][0]["from"]["index"]
        prof_option_api = requests.get(url_prof_option)
        prof_option_json = prof_option_api.json()
        random_prof_option = random.choice(list(prof_option_json["equipment"]))
        background_info["Starting_Proficiencies_Options"] = [random_prof_option["name"]]
    else:
        background_info["Starting_Proficiencies_Options"] = []

    # Starting Equipment Info
    if background_info_from_api["Starting_Equipment"] != None:
        background_info["Starting_Equipment"] = [equipment["equipment"]["name"] for equipment in
                                                 background_info_from_api["Starting_Equipment"]]
    else:
        background_info["Starting_Equipment"] = []


    # Starting Equipment Options Info
    base_url_equip_options = "https://www.dnd5eapi.co/api/equipment-categories/"
    if background_info_from_api["Starting_Equipment_Options"] != None:
        url_equip_options = base_url_equip_options + background_info_from_api["Starting_Equipment_Options"][0]["from"]["index"]
        equip_option_api = requests.get(url_equip_options)
        equip_option_json = equip_option_api.json()
        random_equip_option = random.choice(list(equip_option_json["equipment"]))
        background_info["Starting_Equipment_Options"] = [random_equip_option["name"]]
    else:
        background_info["Starting_Equipment_Options"] = []

    # Gold
    background_info["Gold"] = [background_info_from_api["Gold"]]

    '''
    # Skills
    background_info["Skills"] = []
    for skill in background_info["Starting_Proficiencies"]:
        print("SKILL:", skill)
        if "Skill" in skill:
            print("IF-SKILL:", skill)
            background_info["Skills"].append(skill)
    for skill in background_info["Skills"]:
        if "Skill" in skill:
            background_info["Starting_Proficiencies"].remove(skill)
    '''

    '''
        if "Skill" in skill:
            background_info["Starting_Proficiencies"].remove(skill)
            background_info["Skills"] = skill
    '''

    return background_info

#print(get_background_info("Acolyte"))

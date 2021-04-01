import requests
import random


def get_class_features(class_url):

    if "bard" in class_url:
        return ["Bardic Inspiration (D6)", "Spellcasting: Bard"]

    class_features_url = class_url + "/" + "features"

    class_features_api = requests.get(class_features_url)

    class_features_json = class_features_api.json()

    class_features = class_features_json["results"]

    links = []

    expertises = []

    for features in class_features:
        feature_url = "https://www.dnd5eapi.co" + features["url"]
        feature_api = requests.get(feature_url)
        feature_json = feature_api.json()

        if "Expertise" in features["name"]:
            expertises.append(feature_json["name"])

        elif feature_json["level"] == 1:
            links.append(features["name"])

    if "Choose" in links[0]:
        fighter_choice = random.choice(links[1:])
        links.append(fighter_choice)
        return links[-2:]

    if len(expertises) > 0:
        rogue_choice = random.choice(expertises[1:])
        links.append(rogue_choice)

    return links


print(get_class_features('https://www.dnd5eapi.co/api/classes/wizard'))
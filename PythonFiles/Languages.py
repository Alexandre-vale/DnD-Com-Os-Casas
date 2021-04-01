import random


def get_race_languages(race_info):
    languages = []

    for language in race_info["Languages"]:
        languages.append(language["name"])

    if "Language_Options" in race_info:
        random_optional_language = random.choice(race_info['Language_Options']['from'])
        languages.append(random_optional_language['name'])
        return languages
    else:
        return languages

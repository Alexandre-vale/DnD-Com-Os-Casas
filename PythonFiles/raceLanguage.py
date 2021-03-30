import random


def get_race_languages(race_stats):
    languages = []
    for language in race_stats["Languages"]:
        languages.append(language["name"])

    if "Language_Options" in race_stats:
        random_secondary_language = random.choice(race_stats['Language_Options']['from'])
        return languages[0],random_secondary_language['name']
    else:
        return languages[0], languages[1]

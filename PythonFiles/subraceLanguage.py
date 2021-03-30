import random


def get_subrace_languages(race_stats):
    languages = []
    for language in race_stats["Languages"]:
        languages.append(language["name"])

    if ("Language_Options" in race_stats) and (race_stats["Language_Options"] != 0):
        random_secondary_language = random.choice(race_stats['Language_Options']['from'])
        return languages[0], languages[1], random_secondary_language['name']
    else:
        return languages[0], languages[1]
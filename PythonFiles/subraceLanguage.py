import random


def get_subrace_languages(subrace_stats):
    languages = []
    for language in subrace_stats["Languages"]:
        languages.append(language["name"])

    if ("Language_Options" in subrace_stats) and (subrace_stats["Language_Options"] != 0):
        random_optional_language = random.choice(subrace_stats['Language_Options']['from'])
        languages.append(random_optional_language["name"])
        return languages
    else:
        return languages
import random


def get_race_proficiency(race_stats):
    proficiencies = []

    for proficiency in race_stats["Starting_Proficiencies"]:
        proficiencies.append(proficiency["name"])

    if "Starting_Proficiency_Options" in race_stats:
        random_proficiency = random.choice(race_stats['Starting_Proficiency_Options']['from'])
        proficiencies.append(random_proficiency["name"])
        return proficiencies
    else:
        return proficiencies
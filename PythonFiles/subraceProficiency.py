import random

def get_subrace_proficiency(race_stats):
    proficiencies = []
    for proficiency in race_stats["Starting_Proficiencies"]:
        proficiencies.append(proficiency["name"])

    return proficiencies
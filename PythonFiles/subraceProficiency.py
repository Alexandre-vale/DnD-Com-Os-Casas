import random

def get_subrace_proficiency(subrace_stats):
    proficiencies = []
    for proficiency in subrace_stats["Starting_Proficiencies"]:
        proficiencies.append(proficiency["name"])

    return proficiencies
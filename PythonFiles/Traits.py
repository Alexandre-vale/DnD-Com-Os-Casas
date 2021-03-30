

def get_race_traits(race_stats):
    traits = []
    for trait in race_stats["Traits"]:
        traits.append(trait["name"])
    return traits


def get_subrace_traits(race_stats):
    traits = []
    for trait in race_stats["Traits"]:
        traits.append(trait["name"])
    return traits
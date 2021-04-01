def get_race_traits(race_info):
    traits = []
    for trait in race_info["Traits"]:
        traits.append(trait["name"])
    return traits


def get_subrace_traits(subrace_info):
    traits = []
    for trait in subrace_info["Traits"]:
        traits.append(trait["name"])
    return traits

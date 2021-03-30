from randomName import get_random_name
from randomAbilityScore import get_random_ability_score
from randomRace import get_random_race
from subraceInfo import get_subrace_info
from raceInfo import get_race_info
from raceLanguage import get_race_languages
from subraceLanguage import get_subrace_languages
from Traits import get_race_traits, get_subrace_traits
from randomClass import get_random_class
from raceProficiency import get_race_proficiency
from subraceProficiency import get_subrace_proficiency


name = get_random_name()
ability_score = get_random_ability_score()
race = get_random_race()
_class = get_random_class()

if "subraces" in race[1]:
    race_info = get_subrace_info(race[1])
    languages = get_subrace_languages(race_info)
    traits = get_subrace_traits(race_info)
    proficiencies = get_subrace_proficiency(race_info)
else:
    race_info = get_race_info(race[1])
    languages = get_race_languages(race_info)
    traits = get_race_traits(race_info)
    proficiencies = get_race_proficiency(race_info)

for keys in ability_score:
    for ability_score_bonus in race_info["Ability_Bonuses"]:
        if ability_score_bonus['ability_score']['name'].title() == keys[:3]:
            ability_score[keys] += ability_score_bonus['bonus']


print("Name:", name)
print("Race:", race[0])
print("Race Info:", race_info)
print("Class:", _class[0])
print("Traits:", traits)
print("Proficiencies:", proficiencies)
print("Ability Score:", ability_score)
print("Languages:", languages)


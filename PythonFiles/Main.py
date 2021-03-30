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
from classInfo import get_class_info
from classProficiency import get_class_proficiency
from SavingThrows import get_saving_throws
from ClassEquipment import get_starting_equipment

ModDic = {
    6:-2,
    7:-2,
    8:-1,
    9:-1,
    10:0,
    11:0,
    12:1,
    13:1,
    14:2,
    15:2,
    16:3,
    17:3,
    18:4,
    19:4,
    20:5
}


name = get_random_name()
ability_score = get_random_ability_score()
race = get_random_race()
print(race)
_class = get_random_class()
class_info = get_class_info(_class[1])

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

hp = class_info["Hit_Die"] + ModDic[ability_score["Constitution"]]

print("Name:", name)
print("Race:", race[0])
print("Speed:", race_info["Speed"])
print("Size:", race_info["Size"])
print("Class:", _class[0])
#print("Class Info:", class_info)
print("HP:", hp)
print("Saving Throws:", get_saving_throws(class_info))
print("Traits:", traits)
print("Proficiencies:", get_class_proficiency(class_info, proficiencies))
print("Ability Score:", ability_score)
print("Languages:", languages)
print("Equipment:", get_starting_equipment(class_info))

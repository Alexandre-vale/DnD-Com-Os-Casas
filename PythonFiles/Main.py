from randomName import get_random_name
from randomBackground import get_random_background
from backgroundInfo import get_background_info
from randomAbilityScore import get_random_ability_score
from randomRace import get_random_race
from subraceInfo import get_subrace_info
from raceInfo import get_race_info
from Languages import get_race_languages
from subraceLanguage import get_subrace_languages
from Traits import get_race_traits, get_subrace_traits
from randomClass import get_random_class
from raceProficiency import get_race_proficiency
from subraceProficiency import get_subrace_proficiency
from classInfo import get_class_info
from classFeature import get_class_features
from classProficiency import get_class_proficiency
from SavingThrows import get_saving_throws
from ClassEquipment import get_starting_equipment
from pdfFiller import fill_pdf
from formatPDF import abilities_modifiers, check_saving_throws, proficiencies_and_languages, check_skills, \
    get_formatted_equipment, get_formatted_traits, get_formatted_features

from ClassSpells import find_class_spells
# Ability modifier
ModDic = {6: -2,
          7: -2,
          8: -1,
          9: -1,
          10: 0,
          11: 0,
          12: 1,
          13: 1,
          14: 2,
          15: 2,
          16: 3,
          17: 3,
          18: 4,
          19: 4,
          20: 5}


background = get_random_background()
#background_info = get_background_info(background)


ability_score = get_random_ability_score()
print("Pegou Abilidades")
IntForSpells = ModDic[ability_score["Intelligence"]]
WisForSpells = ModDic[ability_score["Wisdom"]]
if WisForSpells < 1:
    WisForSpells = 1
if IntForSpells < 1:
    IntForSpells = 1



race = get_random_race()
print("Pegou Raça")
_class = get_random_class()
print("Pegou classe")
class_info = get_class_info(_class[1])
class_features = get_class_features(_class[1])
#print("FEATURES:", class_features)
print("Vai pegar magias")
jooj = find_class_spells(_class[0], WisForSpells, IntForSpells)
print("pegou magias")
#print(jooj)
SpellDic = jooj[0]
SpellSlot= jooj[1]
SpellMod = jooj[2]

if "subraces" in race[1]:
    race_info = get_subrace_info(race[1])
    languages = get_subrace_languages(race_info)
    #languages += background_info["Languages"]
    traits = get_subrace_traits(race_info)
    proficiencies = get_subrace_proficiency(race_info)
else:
    race_info = get_race_info(race[1])
    languages = get_race_languages(race_info)
    #languages += background_info["Languages"]
    traits = get_race_traits(race_info)
    proficiencies = get_race_proficiency(race_info)


background = get_random_background()
print("pegou background")
background_info = get_background_info(background, languages)
gold = background_info["Gold"][0]
languages += background_info["Languages"]
traits = get_race_traits(race_info)
proficiencies = get_race_proficiency(race_info)

for keys in ability_score:
    for ability_score_bonus in race_info["Ability_Bonuses"]:
        if ability_score_bonus['ability_score']['name'].title() == keys[:3]:
            ability_score[keys] += ability_score_bonus['bonus']


hp = class_info["Hit_Die"] + ModDic[ability_score["Constitution"]]

equipment = get_starting_equipment(class_info) + background_info["Starting_Equipment"] +  \
            background_info["Starting_Equipment_Options"]



print("proficiencies - ATENÇÃO")
proficiencies += background_info["Starting_Proficiencies"] + background_info["Starting_Proficiencies_Options"]
proficiencies = get_class_proficiency(class_info, proficiencies, proficiencies)

# PDF
name = get_random_name()
ability_modifier = abilities_modifiers(ability_score, ModDic)
saving_throws = get_saving_throws(class_info)
check_saving_throws = check_saving_throws(saving_throws, ability_modifier)
proficiencies_and_languages = proficiencies_and_languages(languages, proficiencies)
check_skills = check_skills(proficiencies, ability_modifier)
equipment_formatted = get_formatted_equipment(equipment)
traits_formatted = get_formatted_traits(traits)
features_formatted = get_formatted_features(class_features)


print("Name:", name)
print("Background:", background)
print("Background Info:", background_info)
print("Gold:", gold)
print("Race:", race[0])
print("Speed:", race_info["Speed"])
print("Size:", race_info["Size"])
print("Class:", _class[0])
#print("Class Info:", class_info)
print("HP:", hp)
print("Saving Throws:", saving_throws)
print("Traits:", traits)
print("Proficiencies:", proficiencies)
print("Ability Score:", ability_score)
print("Languages:", languages)
print("Equipment:", equipment)
print("Spells:", find_class_spells(_class[0], WisForSpells, IntForSpells))


data_dict = {
    'PlayerName': 'Rogério rei delas',
    'CharacterName' : name,
    'CharacterName 2': name,
    'Background': background[0],
    'GP': gold,
    'Equipment': equipment_formatted,
    "Features and Traits": traits_formatted + features_formatted,
    'Race ': race[0],
    'Speed': race_info['Speed'],
    'Height': race_info['Size'],
    'ClassLevel': _class[0],
    'HPMax': hp,
    'HPCurrent': hp,
    'STR': ability_score['Strength'],
    'DEX': ability_score['Dexterity'],
    'CON': ability_score['Constitution'],
    'INT': ability_score['Intelligence'],
    'WIS': ability_score['Wisdom'],
    'CHA': ability_score['Charisma'],
    'STRmod': ability_modifier['Strength'],
    'DEXmod ': ability_modifier['Dexterity'],
    'CONmod': ability_modifier['Constitution'],
    'INTmod': ability_modifier['Intelligence'],
    'WISmod': ability_modifier['Wisdom'],
    'CHamod': ability_modifier['Charisma'],
    'ST Strength': check_saving_throws['Strength']['Modifier'],
    'ST Dexterity': check_saving_throws['Dexterity']['Modifier'],
    'ST Constitution': check_saving_throws['Constitution']['Modifier'],
    'ST Intelligence': check_saving_throws['Intelligence']['Modifier'],
    'ST Wisdom': check_saving_throws['Wisdom']['Modifier'],
    'ST Charisma': check_saving_throws['Charisma']['Modifier'],
    'Check Box 11': check_saving_throws['Strength']['Check_Box'],
    'Check Box 18': check_saving_throws['Dexterity']['Check_Box'],
    'Check Box 19': check_saving_throws['Constitution']['Check_Box'],
    'Check Box 20': check_saving_throws['Intelligence']['Check_Box'],
    'Check Box 21': check_saving_throws['Wisdom']['Check_Box'],
    'Check Box 22': check_saving_throws['Charisma']['Check_Box'],
    'Acrobatics': check_skills['Acrobatics']['Value'],
    'Animal': check_skills['Animal']['Value'],
    'Arcana': check_skills['Arcana']['Value'],
    'Athletics': check_skills['Athletics']['Value'],
    'Deception ': check_skills['Deception']['Value'],
    'History ': check_skills['History']['Value'],
    'Insight' : check_skills['Insight']['Value'],
    'Intimidation': check_skills['Intimidation']['Value'],
    'Investigation ': check_skills['Investigation']['Value'],
    'Medicine': check_skills['Medicine']['Value'],
    'Nature': check_skills['Nature']['Value'],
    'Perception ': check_skills['Perception']['Value'],
    'Performance': check_skills['Performance']['Value'],
    'Persuasion': check_skills['Persuasion']['Value'],
    'Religion': check_skills['Religion']['Value'],
    'SleightofHand': check_skills['SleightofHand']['Value'],
    'Stealth ': check_skills['Stealth']['Value'],
    'Survival': check_skills['Survival']['Value'],
    'ProficienciesLang': proficiencies_and_languages,
    'Check Box 23': check_skills['Acrobatics']['Check_Box'],
    'Check Box 24': check_skills['Animal']['Check_Box'],
    'Check Box 25': check_skills['Arcana']['Check_Box'],
    'Check Box 26': check_skills['Athletics']['Check_Box'],
    'Check Box 27': check_skills['Deception']['Check_Box'],
    'Check Box 28': check_skills['History']['Check_Box'],
    'Check Box 29': check_skills['Insight']['Check_Box'],
    'Check Box 30': check_skills['Intimidation']['Check_Box'],
    'Check Box 31': check_skills['Investigation']['Check_Box'],
    'Check Box 32': check_skills['Medicine']['Check_Box'],
    'Check Box 33': check_skills['Nature']['Check_Box'],
    'Check Box 34': check_skills['Perception']['Check_Box'],
    'Check Box 35': check_skills['Performance']['Check_Box'],
    'Check Box 36': check_skills['Persuasion']['Check_Box'],
    'Check Box 37': check_skills['Religion']['Check_Box'],
    'Check Box 38': check_skills['SleightofHand']['Check_Box'],
    'Check Box 39': check_skills['Stealth']['Check_Box'],
    'Check Box 40': check_skills['Survival']['Check_Box'],
    'ProfBonus': '+2'

}


#Bug do item e bug do half-elf language gerar duas skills iguais

fill_pdf(data_dict)

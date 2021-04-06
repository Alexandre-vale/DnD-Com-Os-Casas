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
from flask import Flask, send_file

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


app = Flask(__name__)
def make_new_ficha():
    name = get_random_name()
    print("Pegou nome")
    # background = get_random_background()
    # background_info = get_background_info(background[1])
    # gold = background_info["Gold"][0]

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
    background_info = get_background_info(background[1], languages)
    languages += background_info["Languages"]
    gold = background_info["Gold"][0]

    proficiencies += background_info["Starting_Proficiencies_Options"] + background_info["Starting_Proficiencies"]
    #print("proficiencies: " + str(proficiencies))

    skills = [x for x in proficiencies if "Skill" in x]
    #print("Skills: " + str(skills))

    for keys in ability_score:
        for ability_score_bonus in race_info["Ability_Bonuses"]:
            if ability_score_bonus['ability_score']['name'].title() == keys[:3]:
                ability_score[keys] += ability_score_bonus['bonus']


    hp = class_info["Hit_Die"] + ModDic[ability_score["Constitution"]]

    equipment = get_starting_equipment(class_info) + background_info["Starting_Equipment"] +  \
                background_info["Starting_Equipment_Options"]

    proficiencies = get_class_proficiency(class_info, proficiencies, skills)


    print("BO")
    # PDF
    ability_modifier = abilities_modifiers(ability_score, ModDic)
    saving_throws = get_saving_throws(class_info)
    Icheck_saving_throws = check_saving_throws(saving_throws, ability_modifier)
    Iproficiencies_and_languages = proficiencies_and_languages(languages, proficiencies)
    Icheck_skills = check_skills(proficiencies, ability_modifier)
    equipment_formatted = get_formatted_equipment(equipment)
    traits_formatted = get_formatted_traits(traits)
    features_formatted = get_formatted_features(class_features)


    # print("Name:", name)
    # print("Background:", background[0])
    # #print("Background Info:", background_info)
    # print("Gold:", gold)
    # print("Race:", race[0])
    # print("Speed:", race_info["Speed"])
    # print("Size:", race_info["Size"])
    # print("Class:", _class[0])
    # #print("Class Info:", class_info)
    # print("HP:", hp)
    # print("Saving Throws:", saving_throws)
    # print("Traits:", traits)
    # print("Proficiencies:", proficiencies)
    # print("Ability Score:", ability_score)
    # print("Languages:", languages)
    # print("Equipment:", equipment)
    # print("Spells:", SpellDic)


    data_dict = {
        'PlayerName': 'Your name goes here',
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
        'ST Strength': Icheck_saving_throws['Strength']['Modifier'],
        'ST Dexterity': Icheck_saving_throws['Dexterity']['Modifier'],
        'ST Constitution': Icheck_saving_throws['Constitution']['Modifier'],
        'ST Intelligence': Icheck_saving_throws['Intelligence']['Modifier'],
        'ST Wisdom': Icheck_saving_throws['Wisdom']['Modifier'],
        'ST Charisma': Icheck_saving_throws['Charisma']['Modifier'],
        'Check Box 11': Icheck_saving_throws['Strength']['Check_Box'],
        'Check Box 18': Icheck_saving_throws['Dexterity']['Check_Box'],
        'Check Box 19': Icheck_saving_throws['Constitution']['Check_Box'],
        'Check Box 20': Icheck_saving_throws['Intelligence']['Check_Box'],
        'Check Box 21': Icheck_saving_throws['Wisdom']['Check_Box'],
        'Check Box 22': Icheck_saving_throws['Charisma']['Check_Box'],
        'Acrobatics': Icheck_skills['Acrobatics']['Value'],
        'Animal': Icheck_skills['Animal']['Value'],
        'Arcana': Icheck_skills['Arcana']['Value'],
        'Athletics': Icheck_skills['Athletics']['Value'],
        'Deception ': Icheck_skills['Deception']['Value'],
        'History ': Icheck_skills['History']['Value'],
        'Insight' : Icheck_skills['Insight']['Value'],
        'Intimidation': Icheck_skills['Intimidation']['Value'],
        'Investigation ': Icheck_skills['Investigation']['Value'],
        'Medicine': Icheck_skills['Medicine']['Value'],
        'Nature': Icheck_skills['Nature']['Value'],
        'Perception ': Icheck_skills['Perception']['Value'],
        'Performance': Icheck_skills['Performance']['Value'],
        'Persuasion': Icheck_skills['Persuasion']['Value'],
        'Religion': Icheck_skills['Religion']['Value'],
        'SleightofHand': Icheck_skills['SleightofHand']['Value'],
        'Stealth ': Icheck_skills['Stealth']['Value'],
        'Survival': Icheck_skills['Survival']['Value'],
        'ProficienciesLang': Iproficiencies_and_languages,
        'Check Box 23': Icheck_skills['Acrobatics']['Check_Box'],
        'Check Box 24': Icheck_skills['Animal']['Check_Box'],
        'Check Box 25': Icheck_skills['Arcana']['Check_Box'],
        'Check Box 26': Icheck_skills['Athletics']['Check_Box'],
        'Check Box 27': Icheck_skills['Deception']['Check_Box'],
        'Check Box 28': Icheck_skills['History']['Check_Box'],
        'Check Box 29': Icheck_skills['Insight']['Check_Box'],
        'Check Box 30': Icheck_skills['Intimidation']['Check_Box'],
        'Check Box 31': Icheck_skills['Investigation']['Check_Box'],
        'Check Box 32': Icheck_skills['Medicine']['Check_Box'],
        'Check Box 33': Icheck_skills['Nature']['Check_Box'],
        'Check Box 34': Icheck_skills['Perception']['Check_Box'],
        'Check Box 35': Icheck_skills['Performance']['Check_Box'],
        'Check Box 36': Icheck_skills['Persuasion']['Check_Box'],
        'Check Box 37': Icheck_skills['Religion']['Check_Box'],
        'Check Box 38': Icheck_skills['SleightofHand']['Check_Box'],
        'Check Box 39': Icheck_skills['Stealth']['Check_Box'],
        'Check Box 40': Icheck_skills['Survival']['Check_Box'],
        'ProfBonus': '+2',
        'SlotsTotal 19' : str(SpellSlot),
        'SlotsRemaining 19' : '0'
    }
    Traduct = {
        'cantrip 1' : 'Spells 1014',
        'cantrip 2' : 'Spells 1016',
        'cantrip 3' : 'Spells 1017',
        'cantrip 4' : 'Spells 1018',
        'cantrip 5' : 'Spells 1019',
        'cantrip 6' : 'Spells 1020',
        'cantrip 7' : 'Spells 1021',
        'cantrip 8' : 'Spells 1022',
        'Spell_1 1' : 'Spells 1015',
        'Spell_1 2' : 'Spells 1023',
        'Spell_1 3' : 'Spells 1024',
        'Spell_1 4' : 'Spells 1025',
        'Spell_1 5' : 'Spells 1026',
        'Spell_1 6' : 'Spells 1027',
        'Spell_1 7' : 'Spells 1028',
        'Spell_1 8' : 'Spells 1029',
        'Spell_1 9' : 'Spells 1030',
        'Spell_1 10' : 'Spells 1031',
        'Spell_1 11' : 'Spells 1032',
        'Spell_1 12' : 'Spells 1033',
        'Checkbox_1 1' : 'Check Box 251',
        'Checkbox_1 2' : 'Check Box 309',
        'Checkbox_1 3' : 'Check Box 3010',
        'Checkbox_1 4' : 'Check Box 3011',
        'Checkbox_1 5' : 'Check Box 3012',
        'Checkbox_1 6' : 'Check Box 3013',
        'Checkbox_1 7' : 'Check Box 3014',
        'Checkbox_1 8' : 'Check Box 3015',
        'Checkbox_1 9' : 'Check Box 3016',
        'Checkbox_1 10' : 'Check Box 3017',
        'Checkbox_1 11' : 'Check Box 3018',
        'Checkbox_1 12' : 'Check Box 3019',
        'Spellcasting Class 2' : 'foda',
        'SpellcastingAbility 2' : SpellMod,
        'SpellSaveDC  2' : ability_modifier[SpellMod] + 10,
        'SpellAtkBonus 2' : ability_modifier[SpellMod]
    }
    #Comeca lista cantrip
    for i in range(len(SpellDic["cantrips"])):
        data_dict[Traduct[f'cantrip {i+1}']] = SpellDic["cantrips"][i]
    #Termina lista contrip
    #Começa lista de magia
    for i in range(len(SpellDic["Level_1"])):
        data_dict[Traduct[f'Spell_1 {i+1}']] = SpellDic["Level_1"][i]["Spell_Name"]
        data_dict[Traduct[f'Checkbox_1 {i+1}']] = SpellDic["Level_1"][i]["Prepared"]

    #Bug do item e bug do half-elf language gerar duas skills iguais
    print("Montando pdf...")
    fill_pdf(data_dict)

@app.route("/ficha", methods=["GET"])
def downloadficha():
    print("Usuario pediu uma ficha")
    make_new_ficha()
    path = "C:/Users/Alexandre/DnD-Com-Os-Casas/Versao_final.pdf"
    return send_file(path, as_attachment=True)

#make_new_ficha()

if __name__ == '__main__':
    print("Ouvindo em port 8000")
    app.run(port=8000,debug=True) 
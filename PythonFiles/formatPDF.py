def abilities_modifiers(ability_score, mod_dict):
    abilities_mod_dict = {}
    for ability in ability_score:
        abilities_mod_dict[ability] = mod_dict[ability_score[ability]]

    return abilities_mod_dict


def check_saving_throws(saving_throws, ability_score):
    saving_dict = {}
    for keys in ability_score:
        if keys in saving_throws:
            saving_dict[keys] = {}
            saving_dict[keys]['Check_Box'] = True
            saving_dict[keys]['Modifier'] = ability_score[keys] + 2

        else:
            saving_dict[keys] = {}
            saving_dict[keys]['Check_Box'] = False
            saving_dict[keys]['Modifier'] = ability_score[keys]

    return saving_dict


print(check_saving_throws(['Constitution', 'Charisma'], {'Strength': 11, 'Dexterity': 13, 'Constitution': 16, 'Intelligence': 11, 'Wisdom': 14, 'Charisma': 8}))


def proficiencies_and_languages(languages, proficiencies):
    final_result_language = 'Languages: '
    final_result_proficiency = 'Proficiencies: '
    for language in languages:
        final_result_language += language + ', '
    for proficiency in proficiencies:
        if 'Skill:' not in proficiency:
            final_result_proficiency += proficiency + ', '

    return final_result_language[:-2] + '\n\n' + final_result_proficiency[:-2]


def check_skills(proficiencies, ability_modifier):
    final_result_skill = {
    'Acrobatics':{'Check_Box': False, 'Modifier': 'Dexterity', 'Value': 0},
    'Animal': {'Check_Box': False, 'Modifier': 'Wisdom', 'Value': 0},
    'Arcana': {'Check_Box': False, 'Modifier': 'Intelligence', 'Value': 0},
    'Athletics': {'Check_Box': False, 'Modifier': 'Strength', 'Value': 0},
    'Deception': {'Check_Box': False, 'Modifier': 'Charisma', 'Value': 0},
    'History': {'Check_Box': False, 'Modifier': 'Intelligence', 'Value': 0},
    'Insight' : {'Check_Box': False, 'Modifier': 'Wisdom', 'Value': 0},
    'Intimidation': {'Check_Box': False, 'Modifier': 'Charisma', 'Value': 0},
    'Investigation': {'Check_Box': False, 'Modifier': 'Intelligence', 'Value': 0},
    'Medicine': {'Check_Box': False, 'Modifier': 'Wisdom', 'Value': 0},
    'Nature': {'Check_Box': False, 'Modifier': 'Intelligence', 'Value': 0},
    'Perception': {'Check_Box': False, 'Modifier': 'Wisdom', 'Value': 0},
    'Performance':{'Check_Box': False, 'Modifier': 'Charisma', 'Value': 0},
    'Persuasion': {'Check_Box': False, 'Modifier': 'Charisma', 'Value': 0},
    'Religion': {'Check_Box': False, 'Modifier': 'Intelligence', 'Value': 0},
    'SleightofHand':{'Check_Box': False, 'Modifier': 'Dexterity', 'Value': 0},
    'Stealth': {'Check_Box': False, 'Modifier': 'Dexterity', 'Value': 0},
    'Survival': {'Check_Box': False, 'Modifier': 'Wisdom', 'Value': 0}
    }

    for keys in final_result_skill:
        for skill in proficiencies:
            if 'Skill' in skill:
                if skill.split(' ')[1] in keys:
                    final_result_skill[keys]['Check_Box'] = True
                    final_result_skill[keys]['Value'] = ability_modifier[final_result_skill[keys]['Modifier']] + 2
    for keys in final_result_skill:
        if final_result_skill[keys]['Value'] == 0:
            final_result_skill[keys]['Value'] = ability_modifier[final_result_skill[keys]['Modifier']]

    return final_result_skill


def get_formatted_equipment(equipments):
    final_result = ''
    for equipment in equipments:
        if type(equipment) == str:
            final_result += "\n - " + equipment
        else:
            for equipment_inside_list in equipment:
                final_result += "\n - " + equipment_inside_list
    return final_result


def get_formatted_traits(traits):
    final_result = ''
    for trait in traits:
        final_result += "\n - " + trait
    return final_result


def get_formatted_features(features):
    final_result = ''
    for feature in features:
        final_result += "\n - " + feature
    return final_result


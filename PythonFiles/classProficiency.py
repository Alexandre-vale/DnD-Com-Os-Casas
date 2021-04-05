import random
import numpy as np


def get_class_proficiency(class_info, proficiencies, imported_skills):
    for proficiency in class_info["Proficiencies"]:
        proficiencies.append(proficiency["name"])

    # proficiencies_to_add = random.choices(class_info['Proficiency_Choices'][0]['from'], k=class_info['Proficiency_Choices'][0]['choose'])
    proficiency_pool = class_info['Proficiency_Choices'][0]['from']
    proficiency_choices = np.random.choice(class_info['Proficiency_Choices'][0]['from'],
                                            size=class_info['Proficiency_Choices'][0]['choose'],
                                            replace=False)
    proficiency_pool = [x for x in proficiency_pool if x not in proficiency_choices]
    for skill in proficiency_choices:
        if skill in imported_skills:
            skill = random.choice(proficiency_pool)
    
    for proficiency_to_add in proficiency_choices:
        proficiencies.append(proficiency_to_add["name"])

    return proficiencies

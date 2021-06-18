import random
import numpy as np


def get_class_proficiency(class_info, proficiencies, imported_skills):
    for proficiency in class_info["Proficiencies"]:
        proficiencies.append(proficiency["name"])

    # proficiencies_to_add = random.choices(class_info['Proficiency_Choices'][0]['from'], k=class_info['Proficiency_Choices'][0]['choose'])
    proficiency_raw = class_info['Proficiency_Choices'][0]['from']
    #print("Adoleta: " + str(proficiency_raw))
    proficiency_pool = [x['name'] for x in proficiency_raw if x['name'] not in imported_skills]
    #print("Adoleta: " + str(proficiency_pool))
    proficiency_choices = np.random.choice(proficiency_pool,
                                            size=class_info['Proficiency_Choices'][0]['choose'],
                                            replace=False)
    
    for proficiency_to_add in proficiency_choices:
        proficiencies.append(proficiency_to_add)

    return proficiencies

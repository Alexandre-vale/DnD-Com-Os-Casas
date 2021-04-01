import random
import numpy as np


def get_class_proficiency(class_info, proficiencies):
    for proficiency in class_info["Proficiencies"]:
        proficiencies.append(proficiency["name"])

    # proficiencies_to_add = random.choices(class_info['Proficiency_Choices'][0]['from'], k=class_info['Proficiency_Choices'][0]['choose'])

    proficiencies_to_add = np.random.choice(class_info['Proficiency_Choices'][0]['from'],
                                            size=class_info['Proficiency_Choices'][0]['choose'],
                                            replace=False)

    for proficiency_to_add in proficiencies_to_add:
        proficiencies.append(proficiency_to_add["name"])

    return proficiencies

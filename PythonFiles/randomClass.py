import requests
import random


def get_random_class():
    base_url_class = "https://www.dnd5eapi.co/api/classes"

    all_classes_api = requests.get(base_url_class)

    all_classes_json = all_classes_api.json()

    base_classes = {}

    for classes in all_classes_json["results"]:
        base_classes[classes["name"]] = base_url_class + '/' + classes['index']

    random_class = random.choice(list(base_classes.items()))

    '''
    subclass_info = requests.get(random_class[1])

    subclass_info_json =  subclass_info.json()

    base_subclass = [random_class[0]]

    for subclass in subclass_info_json["subclasses"]:
        base_subclass.append(random_class[0] + '-' + subclass["name"])

    random_classes = random.choice(base_subclass)
    '''

    return random_class

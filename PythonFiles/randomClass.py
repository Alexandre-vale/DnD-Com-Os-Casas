import requests
import random


def get_random_class():
    class_url = "https://www.dnd5eapi.co/api/classes"

    class_info_api = requests.get(class_url)

    class_info_json = class_info_api.json()

    base_class = {}

    for classes in class_info_json["results"]:
        base_class[classes["name"]] = class_url + '/' + classes['index']

    random_class = random.choice(list(base_class.items()))
    #
    subclass_info = requests.get(random_class[1])

    subclass_info_json =  subclass_info.json()

    base_subclass = [random_class[0]]

    for subclass in subclass_info_json["subclasses"]:
        base_subclass.append(random_class[0] + '-' + subclass["name"])

    random_classes = random.choice(base_subclass)
    # cagada marcada
    return [random_classes, random_class[1]]

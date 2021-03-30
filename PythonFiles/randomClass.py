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

    return random_class

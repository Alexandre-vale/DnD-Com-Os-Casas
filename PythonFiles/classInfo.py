import requests


def get_class_info(class_url):
    class_info_api = requests.get(class_url)

    class_info_json = class_info_api.json()

    class_info = {"Hit_Die": 0, "Proficiencies": 0, "Proficiency_Choices": 0}

    for keys in class_info:
        class_info[keys] = class_info_json[keys.lower()]

    return class_info

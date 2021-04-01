convert = {
    "STR": "Strength",
    "CON": "Constitution",
    "DEX": "Dexterity",
    "INT": "Intelligence",
    "WIS": "Wisdom",
    "CHA": "Charisma"
}


def get_saving_throws(class_info):
    saves = []
    for throws in class_info["Saving_throws"]:
        #input so recebe as 3 primeiras letras, então fiz um dicionario pra ficar bonito
        full_name = convert[throws["name"]]
        saves.append(full_name)
    return saves

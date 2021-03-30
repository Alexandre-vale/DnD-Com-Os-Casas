import requests
import random

# Analyze_equip foi uma saída semi recursiva(o laço deve se repetir no maximo 2 vezes)
# para resolver o problema de escolhas dentro de escolhas que algumas classes possuiam
def analyze_equip(equip):
    #Aqui é o unico ponto de recursividade da função
    if "0" in equip:
        item = []
        item1 = analyze_equip(equip["0"])
        item.append(item1)
        item2 = analyze_equip(equip["1"])
        item.append(item2)
        if "2" in equip:
            item3 = analyze_equip(equip["2"])
            item.append(item3)
    #Aqui analizamos se devemos escolher entre uma lista de equipamentos
    elif "equipment_option" in equip:
        url = equip["equipment_option"]["from"]["equipment_category"]["url"]
        raw_list_of_gear = requests.get("https://www.dnd5eapi.co" + url)
        list_of_gear = raw_list_of_gear.json()
        gear_to_add = random.choices(list_of_gear["equipment"], k=equip["equipment_option"]["choose"])
        for gear in gear_to_add:
            outro_sinonimo_de_item = gear["name"]
            item = f"{outro_sinonimo_de_item} x{gear_to_add.count(gear)}"
            gear_to_add.remove(gear)
    #mesma coisa que a anterior, mas por algum motivos existem dois tipos nesta api para a mesma coisa
    elif "equipment_category" in equip:
        url = equip["equipment_category"]["url"]
        raw_list_of_gear = requests.get("https://www.dnd5eapi.co" + url)
        list_of_gear = raw_list_of_gear.json()
        gear = random.choice(list_of_gear["equipment"])
        outro_sinonimo_de_item = gear["name"]
        item = f"{outro_sinonimo_de_item} x1"
    #Aqui é o mais simples, o algoritmo escolhe um random e a gente guarda
    else:
        gear = equip["equipment"]["name"]
        if "quantity" in equip:
            quantity = equip["quantity"]
        else:
            quantity = 1
        item = f"{gear} x{quantity}"
    return item

#Equipamentos tem duas categorias, normal e options, normal é garantido portanto não temos que ler, e tambem não temos que analizar por padroes mais absurdos
def get_starting_equipment(classinfo):
    Equipment = []
    for gear in classinfo["Starting_Equipment"]:
        item = gear["equipment"]["name"] + " x" + str(gear["quantity"])
        Equipment.append(item)

    for categories in classinfo["Starting_Equipment_Options"]:
        equip = random.choice(categories["from"])
        item = analyze_equip(equip)
        Equipment.append(item)


    return Equipment
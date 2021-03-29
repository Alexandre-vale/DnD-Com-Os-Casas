import requests
# este aquivo serve como para olharmos no api certas informações e como elas são devolvidas em json


def encontremagias():
    print("Digite o nome da magia")
    entrada = input()

    entrada = entrada.lower()
    entrada = entrada.replace(" ", "-")


    print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/spells/{entrada}/...\n')
    proto = requests.get(f'https://www.dnd5eapi.co/api/spells/{entrada}/')

    proto = proto.json()
    print(proto)

def encontreraca():
    print("Digite o nome da raça")
    entrada = input()

    entrada = entrada.lower()
    entrada = entrada.replace(" ", "-")


    print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/races/{entrada}/...\n')
    proto = requests.get(f'https://www.dnd5eapi.co/api/races/{entrada}/')

    proto = proto.json()
    print(proto)

def encontreclasse():
    print("Digite o nome da classe")
    entrada = input()

    entrada = entrada.lower()
    entrada = entrada.replace(" ", "-")


    print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/class/{entrada}/...\n')
    proto = requests.get(f'https://www.dnd5eapi.co/api/class/{entrada}/')

    proto = proto.json()
    print(proto)

def encontreesquipamento():
    print("Digite o nome do equipamento")
    entrada = input()

    entrada = entrada.lower()
    entrada = entrada.replace(" ", "-")


    print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/spells/{entrada}/...\n')
    proto = requests.get(f'https://www.dnd5eapi.co/api/spells/{entrada}/')

    proto = proto.json()
    print(proto)

def encontrebackground():
    print("Digite o nome do antecedente")
    entrada = input()

    entrada = entrada.lower()
    entrada = entrada.replace(" ", "-")


    print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/spells/{entrada}/...\n')
    proto = requests.get(f'https://www.dnd5eapi.co/api/spells/{entrada}/')

    proto = proto.json()
    print(proto)
    

print("O que deseja procurar?\n1-magias\n2-raças\n3-classes\n4-equipamentos\n5-Antecedente")

choice = input()


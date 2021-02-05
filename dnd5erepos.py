import requests

def encontremagias():
    print("Digite o nome da magia")
    entrada = input()

    entrada = entrada.lower()
    entrada = entrada.replace(" ", "-")


    print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/spells/{entrada}/...\n')
    proto = requests.get(f'https://www.dnd5eapi.co/api/spells/{entrada}/')

    proto = proto.json()

    for entry in proto:
        print(f'{entry} : {proto[entry]}\n')

encontremagias()

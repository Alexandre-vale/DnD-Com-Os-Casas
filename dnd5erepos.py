import requests

def listalljson(proto):
    for entry in proto:
        if isinstance(proto[entry], list):
            for entry2 in proto[entry]:
                for entry3 in entry2:
                    if entry3 == "url":
                        print(f'https://www.dnd5eapi.co{entry2[entry3]}/')
        elif isinstance(proto[entry], dict):
            listalljson(proto[entry])
        else:
            if entry == "url":
                print(f'https://www.dnd5eapi.co{proto[entry]}/')
            else:
                print(f'{entry} : {proto[entry]}\n')

def encontremagias():
    print("Digite o nome da magia")
    entrada = input()

    entrada = entrada.lower()
    entrada = entrada.replace(" ", "-")


    print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/spells/{entrada}/...\n')
    proto = requests.get(f'https://www.dnd5eapi.co/api/spells/{entrada}/')

    proto = proto.json()
    listalljson(proto)
    

encontremagias()

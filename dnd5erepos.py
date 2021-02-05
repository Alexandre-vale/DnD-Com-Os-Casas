import requests

print("Digite o nome da magia")
entrada = input()

entrada = entrada.lower()
entrada = entrada.replace(" ", "-")


print(f'Procurando nos grimorios pela magia {entrada} em https://www.dnd5eapi.co/api/spells/{entrada}/...\n')
proto = requests.get(f'https://www.dnd5eapi.co/api/spells/{entrada}/')

proto = proto.json()

if "damage_at_slot_level" in proto:
    print(f'dano por level de spell slot: {proto["damage"]["damage_at_slot_level"]}')
else:
    print(f'dano por level do personagem: {proto["damage"]["damage_at_character_level"]}')

print(proto["damage"]["damage_type"]["name"])

print(f'https://www.dnd5eapi.co/api{proto["damage"]["damage_type"]["url"]}/')
desc = requests.get(f'https://www.dnd5eapi.co{proto["damage"]["damage_type"]["url"]}/')

desc = desc.json()

print(desc["desc"])

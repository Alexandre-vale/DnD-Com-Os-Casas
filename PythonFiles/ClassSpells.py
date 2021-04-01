import requests
import random
import numpy as np

# Algumas classes dependem de sabedoria para quantificar a quantidade de magias, por isso o input da função deve contar o nome da classe(pra procurarmos que magia ela pode usar)
# E modificador de sabedoria, para no caso de que a classe precisa do modificador podemos providenciar
def find_class_spells(ClassName, WisdomMod):
    ClassSpells = {
                    "Bard" : {"cantrips": 2, "Known Spells": 4},
                    "Warlock" : {"cantrips": 2, "Known Spells": 2},
                    "Cleric" : {"cantrips": 3, "Known Spells": WisdomMod + 1},
                    "Druid" : {"cantrips": 2, "Known Spells": WisdomMod + 1},
                    "Sorcerer" : {"cantrips": 4, "Known Spells": 2},
                    "Wizard" : {"cantrips": 3, "Known Spells": 6}
                }
    if ClassName not in ClassSpells:
        return []
    else:
        base_url = "https://www.dnd5eapi.co"
            #Esse metodo funciona, mas é estremamente lento, tipo, beeem lento, cerca de dois minutos pra achar do mago. não incorporei ainda no codigo principal pra vermos um jeito de resolver
            # Minha ideia é implementar um dicionario fixo que podemos salvar todas as magias(mais ou menos o que o loop abaixo faz mas em algo permanente)
            # assim podemos procurar na faixa de nivel certa.
        spells = {}

        spells["cantrips"] = []

        spells["Level_1"] = []

        AccessClass = ClassSpells[ClassName]

        spells_raw = requests.get("https://www.dnd5eapi.co/api/spells/")

        spells_json = spells_raw.json()

        all_spells = spells_json["results"]
        list_of_cantrips = []
        list_of_level_1_spells = []
        list_of_any_other_spell = []

            # for check in all_spells:
            #     to_add_spell = requests.get(base_url + check["url"])
            #     to_add_spell_json = to_add_spell.json()
            #     if to_add_spell_json["level"] == 0:
            #         print("Added " + to_add_spell_json["name"] + " to cantrips")
            #         list_of_cantrips.append(check)
            #     elif to_add_spell_json["level"] == 1:
            #         print("Added " + to_add_spell_json["name"] + " to level 1")
            #         list_of_level_1_spells.append(check)
            #     else:
            #         list_of_any_other_spell.append(check)
            #         print("Added " + to_add_spell_json["name"] + " to else")
            

        for i in range(0,AccessClass["cantrips"]):
            conditions_met = False

            while conditions_met == False:
                Spell_classes = []

                Spell_Found = np.random.choice(all_spells,replace=False)
                                        

                Spell_Candidate_Raw = requests.get(base_url + Spell_Found["url"])

                Spell_Candidate = Spell_Candidate_Raw.json()

                #print("Trying Spell named", Spell_Candidate["name"])

                for possible_classes in Spell_Candidate["classes"]:

                    Spell_classes.append(possible_classes["name"])
                        
                #print(Spell_classes, Spell_Candidate["level"])

                if Spell_Candidate["level"] == 0 and  ClassName in Spell_classes:

                    #print("Spell fits! Appending...")
                    spells["cantrips"].append(Spell_Candidate["name"])
                    conditions_met = True


        for i in range(0, AccessClass["Known Spells"]):
            conditions_met = False

            while conditions_met == False:
                Spell_classes = []
                Spell_Found = np.random.choice(all_spells,replace=False)

                Spell_Candidate_Raw = requests.get(base_url + Spell_Found["url"])

                Spell_Candidate = Spell_Candidate_Raw.json()

                #print("Trying Spell named", Spell_Candidate["name"])

                for possible_classes in Spell_Candidate["classes"]:

                    Spell_classes.append(possible_classes["name"])

                #print(Spell_classes, Spell_Candidate["level"])

                if Spell_Candidate["level"] == 1 and ClassName in Spell_classes:

                    #print("Spell fits! Appending...")

                    spells["Level_1"].append(Spell_Candidate["name"])

                    conditions_met = True

        return spells



#print(find_class_spells("Wizard", 3))
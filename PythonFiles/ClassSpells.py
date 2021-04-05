import requests
import random
import numpy as np

# Algumas classes dependem de sabedoria para quantificar a quantidade de magias, por isso o input da função deve contar o nome da classe(pra procurarmos que magia ela pode usar)
# E modificador de sabedoria, para no caso de que a classe precisa do modificador podemos providenciar
def find_class_spells(ClassName, WisdomMod, IntMod):
    ClassSpells = {
                    "Bard" : {"cantrips": 2, "Known_Spells": 4, "Prepared_Spells" : 4, "Spell_Slots" : 2, "Spellcast_Mod" : "Charisma"},
                    "Warlock" : {"cantrips": 2, "Known_Spells": 2,"Prepared_Spells" : 2, "Spell_Slots" : 1, "Spellcast_Mod" : "Charisma"},
                    "Cleric" : {"cantrips": 3, "Known_Spells": WisdomMod + 1,"Prepared_Spells" : WisdomMod + 1, "Spell_Slots" : 2, "Spellcast_Mod" : "Wisdom"},
                    "Druid" : {"cantrips": 2, "Known_Spells": WisdomMod + 1,"Prepared_Spells" : WisdomMod + 1, "Spell_Slots" : 2, "Spellcast_Mod" : "Wisdom"},
                    "Sorcerer" : {"cantrips": 4, "Known_Spells": 2,"Prepared_Spells" : 2, "Spell_Slots" : 2, "Spellcast_Mod" : "Charisma"},
                    "Wizard" : {"cantrips": 3, "Known_Spells": 6, "Prepared_Spells" : IntMod + 1, "Spell_Slots" : 2, "Spellcast_Mod" : "Intelligence"}
                }
    spells = {}

    spells["cantrips"] = []

    spells["Level_1"] = []


    if ClassName not in ClassSpells:
        return [spells, 0, 'Intelligence']
    else:
        base_url = "https://www.dnd5eapi.co"
            #Esse metodo funciona, mas é estremamente lento, tipo, beeem lento, cerca de dois minutos pra achar do mago. não incorporei ainda no codigo principal pra vermos um jeito de resolver
            # Minha ideia é implementar um dicionario fixo que podemos salvar todas as magias(mais ou menos o que o loop abaixo faz mas em algo permanente)
            # assim podemos procurar na faixa de nivel certa.
        AccessClass = ClassSpells[ClassName]

        spells_raw = requests.get("https://www.dnd5eapi.co/api/spells/")

        spells_json = spells_raw.json()

        all_spells = spells_json["results"]
        list_of_cantrips = []
        list_of_level_1_spells = []
        list_of_any_other_spell = []
        chosenspells = []
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

                if Spell_Candidate["level"] == 0 and  ClassName in Spell_classes and Spell_Candidate['name'] not in chosenspells:

                    #print("Cantrip fits! Appending... " + str(AccessClass["cantrips"]-i) + " to go!")
                    chosenspells.append(Spell_Candidate["name"])
                    spells["cantrips"].append(Spell_Candidate["name"])
                    conditions_met = True
                


        for i in range(0, AccessClass["Known_Spells"]):
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

                if Spell_Candidate["level"] == 1 and  ClassName in Spell_classes and Spell_Candidate['name'] not in chosenspells:

                    #print("Spell fits! Appending... " + str(AccessClass["Known_Spells"]-i)+ " to go!")
                    if ClassSpells[ClassName]["Prepared_Spells"] > 0:
                        ClassSpells[ClassName]["Prepared_Spells"] -= 1
                        spells["Level_1"].append({"Spell_Name" : Spell_Candidate["name"], "Prepared" : True})
                    else:
                        spells["Level_1"].append({"Spell_Name" : Spell_Candidate["name"], "Prepared" : False})
                    chosenspells.append(Spell_Candidate["name"])
                    conditions_met = True

        return [spells, ClassSpells[ClassName]["Spell_Slots"], ClassSpells[ClassName]["Spellcast_Mod"]]



#print(find_class_spells("Wizard", 3, 4))
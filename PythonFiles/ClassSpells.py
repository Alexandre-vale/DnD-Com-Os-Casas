
ClassSpells = {
    "bard":{"cantrips": 2, "Known Spells": 4},
    "warlock":{"cantrips": 2, "Known Spells": 2},
    "cleric":{"cantrips": 3, "Known Spells": WisdomMod + 1},
    "druid":{"cantrips": 2, "Known Spells": WisdomMod + 1},
    "sorcerer":{"cantrips": 4, "Known Spells": 2},
    "wizard":{"cantrips": 3, "Known Spells": 6}
}
# Algumas classes dependem de sabedoria para quantificar a quantidade de magias, por isso o input da função deve contar o nome da classe(pra procurarmos que magia ela pode usar)
# E modificador de sabedoria, para no caso de que a classe precisa do modificador podemos providenciar
def find_class_spells(ClassName, WisdomMod):
    {

    }
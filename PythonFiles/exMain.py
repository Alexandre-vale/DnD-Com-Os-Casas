import names
import random
import requests
from time import sleep


def roll_dice(n_times):
    return [random.randint(2, 6) for _ in range(n_times)]


random_name = names.get_full_name()

ability_scores = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0,
                  'Intellect': 0, 'Wisdom': 0, 'Charisma': 0}

for keys in ability_scores:
    ability_scores[keys] = sum(roll_dice(4))

race = generate_base_race()


print(race)

race_stats = get_race_stats(race[1])

primary_language, secondary_language = race_language(race_stats)

print("Name:", random_name)

print("Ability Scores:", ability_scores)

print("Race:", race[0]) # TIRAR

print("Race URL:", race[1]) # TIRAR

for a in race_stats["Ability_Bonuses"]:
    print(f"Ability Score Bonus: {a['ability_score']['name'].title()} + {a['bonus']} ")

for keys in ability_scores:
    for ability_score in race_stats["Ability_Bonuses"]:
        if ability_score['ability_score']['name'].title() == keys[:3]:
            ability_scores[keys] += ability_score['bonus']

print("Ability Scores:", ability_scores)

print(f"Primary Language: {primary_language} \nSecondary Language: {secondary_language}")






'''
for a in race_stats["Ability_Bonuses"]:
    print(f"Ability Score Bonus: {a['ability_score']['name'].title()} + {a['bonus']} ")

for a in race_stats["Languages"]:
    print("Language:", a["name"])
'''



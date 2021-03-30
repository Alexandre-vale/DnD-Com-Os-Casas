import random


def roll_dice(n_times):
    return [random.randint(2, 6) for _ in range(n_times)]


def get_random_ability_score():
    ability_scores = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0,
                      'Intellect': 0, 'Wisdom': 0, 'Charisma': 0}

    for keys in ability_scores:
        ability_scores[keys] = sum(roll_dice(3))

    return ability_scores

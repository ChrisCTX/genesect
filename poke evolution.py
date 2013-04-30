from random import randint
from attack_modifiers import STAB, SuperEffectiveRange, Types

TOTAL_TYPES = 10

    # Fiteness per move = Base * Accuracy * STAB * (% of SE vs top used mons)
    # Average of fitness * # of SE types / total of types

def fitness_raw(pokemon, moveset):
    fitness = 0
    for move in moveset:
        stab = STAB(pokemon, move)
        fitness = fitness + move.base * stab
    fitness = fitness / len(moveset)
    SERange = SuperEffectiveRange(moveset)
    fitness = fitness * SERange / TOTAL_TYPES
    return fitness

def fitness_accuracy_stats(pokemon, moveset, statistics):
    """Takes into account accuracy."""
    #fitness = fitness + move.base * move.accuracy * stab
    pass

def mutate(moveset, probability, magnitude):
    pass

def reproduce_even(parent1, parent2):
    '''Creates a child with half of each parent moves.'''
    half = len(parent1) / 2
    child = parent1[:half] + parent2[half:]
    return child

def reproduce_random(parent1, parent2):
    '''Creates a child with random moves from the parents moveset.'''
    child = []
    for i in range(len(parent1)):
        if (randint(0, 200) % 2 == 0):
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

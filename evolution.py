from random import randint, random
from specimen import specimen

def mutate(moveset, probability, magnitude):
    pass

def get_random_indexes(max, probability):
    if max < 1:
        return []
    else:
        indexes = []
        for i in range(0, max):
            if(random() < probability):
                indexes.append(True)
            else:
                indexes.append(False)
        return indexes
    

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


def offspring(population):
    pass

from csv_loader import load_moves
from type_modifiers import STAB, getTypeCoverage
from stats import get_type_statistics, get_sample
from math import log

moves = load_moves()

def fitness(pokemon, moveset):
    """Evaluates how good a given moveset is for the metagame. """
    fitness = 0
    for move in moveset:
        move = moves[move]
        base = int(move.power)
        acc = int(move.accuracy)
        # Same Type Attack Bonus (STAB) grants an additional
        # 1.5 power multiplier if the attack is the same
        # type as either of the attacking pokemon types
        if STAB(pokemon, move):
            power = base * 1.5
        else:
            power = base
        # We also take into account the accuracy of the attack
        fitness = fitness + (power * acc / 100)
        
    stats = get_type_statistics()
    average_fitness = fitness / len(moveset)
    super_effective_coverage = getTypeCoverage(moveset)
    sample = get_sample(stats)
    for covered_type in super_effective_coverage:
        average_fitness *= sample / stats[covered_type] 

    return log(average_fitness)



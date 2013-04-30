from csv_loader import load_moves
from poke_types import getSECoverage
from stats import get_type_statistics, get_sample
from math import log

moves = load_moves()

def getTypeCoverage(moveset):
    """Returns a list of types the moveset is SE against. """
    coverage = []
    for move in moveset:
        move_coverage = getSECoverage(moves[move].type)
        for covered_type in move_coverage:
            if covered_type not in coverage:
                coverage.append(covered_type)
    return coverage

def STAB(pokemon, move):
    """Returns True if the pokemon is the same type as the attack. """
    if pokemon.type1 == move.type:
        return True
    elif pokemon.type2 == move.type:
        return True
    else:
        return False

def fitness(pokemon, moveset):
    """Evaluates how good a given moveset is for the metagame. """
    fitness = 0
    for move in moveset:
        move = moves[move]
        base = int(move.power)
        # Same Type Attack Bonus (STAB) grants an additional
        # 1.5 power multiplier if the attack is the same
        # type as either of the attacking pokemon types
        power = 0
        if STAB(pokemon, move):
            power = base * 1.5
        else:
            power = base
        fitness = fitness + power
        
    stats = get_type_statistics()
    average_fitness = fitness / len(moveset)
    super_effective_coverage = getTypeCoverage(moveset)
    sample = get_sample(stats)
    for covered_type in super_effective_coverage:
        average_fitness *= sample / stats[covered_type] 

    return log(average_fitness)

#### Example ########

from csv_loader import load_pokemons
pk = load_pokemons()
ty = pk["tyranitar"]
print fitness(ty, ["stoneedge"])
print fitness(ty, ["stoneedge", "crunch"])
print fitness(ty, ["stoneedge", "crunch", "pursuit"])
print fitness(ty, ["stoneedge", "crunch", "pursuit", "superpower"])
print fitness(ty, ["stoneedge", "crunch", "fireblast", "superpower"])
print fitness(ty, ["stoneedge", "stoneedge", "stoneedge", "stoneedge"])
print fitness(ty, ["crunch", "fireblast", "icebeam", "lowkick"])

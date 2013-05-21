from csv_loader import load_statistics, load_pokemons
from type_modifiers import getUsageDict

stats = load_statistics()

def get_type_statistics():
    pokemons = load_pokemons()
    type_usage = getUsageDict()

    for pokemon, number_of_uses in stats.items():
        type1 = pokemons[pokemon].type1
        type2 = pokemons[pokemon].type2

        type_usage[type1] += number_of_uses
        if type2:   # could be None
            type_usage[type2] += number_of_uses

    return type_usage

def get_sample(usage):
    return sum(usage.values())
    

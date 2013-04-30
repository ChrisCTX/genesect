def STAB(pokemon, move):
    if pokemon.type1 == move.type or pokemon.type2 == move.type:
        return 1.5
    else:
        return 1

def SuperEffectiveRange(moveset):
    pass

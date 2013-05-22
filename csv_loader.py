import csv
from move import Move
from pokemon import Pokemon

def load_moves():
    """ Loads the moves from the CSV file into a dictionary. """
    csv_file = open("data/moves.csv", 'r')
    fieldnames = ("name", "accuracy", "power", "stat", "type")
    reader = csv.DictReader(csv_file, fieldnames = fieldnames)
    moves = {}
    for m in reader:
        moves[m["name"]] = Move(m["name"], m["type"], m["stat"],
                                m["power"], m["accuracy"])
    csv_file.close()
    return moves

def load_pokemons():
    """ Loads the pokemon from the CSV file into a dictionary. """
    # We first load all the pokemon
    pokedex_csv_file = open("data/pokedex.csv", 'r')
    fieldnames = ("name", "type1", "type2", "junk1", "junk2")
    reader = csv.DictReader(pokedex_csv_file, fieldnames = fieldnames)
    pokemons = {}
    for p in reader:
        # We clean up the secondary type, make it an actual None
        # if the specific pokemon doesn't have one.
        if p["type2"] == "undefined":
            p["type2"] = None
        pokemons[p["name"]] = Pokemon(p["name"], p["type1"],
                                      p["type2"], []) 
    pokedex_csv_file.close()
    # Once all pokemons are loaded we add their movepools
    pokemons = load_movepools(pokemons)
    return pokemons

def load_movepools(pokemons):    
    """ Loads all movepools from CSV file into the pokemons. """
    movepool_csv_file = open("data/movepools.csv", 'r')
    for line in movepool_csv_file:
    # Just playing with the file, getting name of pokemon
    # and a list of the moves it has access to
        line_list = line.split(',', 1)
        name = line_list[0]
        pool = line_list[1].split(',')
        pool[len(pool)-1] = str.strip(pool[len(pool)-1])#eliminate newline char
        pokemons[name].movepool = pool
        
    movepool_csv_file.close()
    return pokemons

def load_statistics():
    """ Loads statsitics dictionary from a metagame's usage stats. """
    stats_csv_file = open("data/stats.csv", 'r')
    usage = {}
    for line in stats_csv_file:
        split = line.split(',')
        name = split[0].lower()
        usage[name] = int(split[1])
    return usage

def load_files():
    return (load_pokemons(), load_moves())

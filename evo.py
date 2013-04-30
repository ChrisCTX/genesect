from pipe import where, concat, as_list
from csv_loader import load_files
from eyecandy import print_dna, print_name

pokemon, moves = load_files()

#print_name()
#print_dna()
#print pokemon["snorlax"], pokemon["snorlax"].movepool

# Not really Pythonic, but still realy awesome
print   (
            pokemon.values()
            | where(lambda x: x.type1 == "Bug")
            #| where(lambda x: x.type2 == "Flying")
            | as_list
        )

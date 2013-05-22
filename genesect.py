from csv_loader import load_pokemons, load_moves
from fitness import fitness
from specimen import specimen as Individual
from eyecandy import print_dna, print_name
from random import choice
from pipe import *

moves = load_moves()

def getRandomMove(pokemon, spectrum):
    offensive_movepool = pokemon.movepool | where(lambda x: x in moves) | as_list

    if spectrum == "p":
        offensive_movepool = (offensive_movepool |
                              where(lambda x: moves[x].stat == "Physical") |
                              as_list)
    elif spectrum == "s":
        offensive_movepool = (offensive_movepool |
                              where(lambda x: moves[x].stat == "Special") |
                              as_list)

    move = choice(offensive_movepool)
    return move

def getRandomMoveset(pokemon, size, spectrum="m"):
    moveset = []
    for i in range(size):
        moveset.append(getRandomMove(pokemon, spectrum))
    return  moveset

VERBOSE = 0
POPULATION_SIZE = 10
MAX_GENERATIONS = 100

print_name()
print_dna()

pokedex = load_pokemons()
species = str(raw_input("What pokemon would you like to Optimize? \n"))
pokemon = pokedex[species]
#number = int(raw_input("How many moves to optimize for? (minimum 2) \n"))
number = 4
spectrum = "p"


# Generate the initial population of individuals randomly - first Generation
population = [Individual(species, getRandomMoveset(pokemon, number, spectrum), 0)
              for x in range(POPULATION_SIZE)]

# Evaluate the fitness of each individual in that population
for specimen in population:
    specimen.fitness = fitness(pokemon, specimen.moveset)

population.sort(reverse=True)
print "Initial population's first specimen:"
print population[0]
print "\nEvolution beings... (this will take a while)\n"

# Evolution loop
for generation in range(MAX_GENERATIONS):
    # Select the best-fit individuals for reproduction - parents
    best_fit = population[:POPULATION_SIZE/2]

    # Breed new individuals through crossover and mutation
    new_population = [Individual(species, getRandomMoveset(pokemon, number, spectrum), 0)
                      for x in range(POPULATION_SIZE/2)]

    # Evaluate the individual fitness of new individuals
    for specimen in new_population:
        specimen.fitness = fitness(pokemon, specimen.moveset)

    # Replace least-fit population with new individuals
    population = best_fit + new_population

    # Sort by fitness for next generation manipulation
    population.sort(reverse=True)

    if VERBOSE > 0:
        print "Generation" + str(generation) + "'s Most fit specimen:"
        print population[0]

print_dna()

print "\nThe top 3 specimens of the evolution are:"
print population[0]
print population[1]
print population[2]
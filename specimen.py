class specimen():
    def __init__(self, species, moveset, fitness):
        self.species = species
        self.moveset = moveset
        self.fitness = fitness

    def __cmp__(self, other):
        if self.fitness < other:
            return -1
        elif self.fitness == other:
            return 0
        else:
            return 1

    def __str__(self):
        return str(self.moveset) + ", " +str(self.fitness)
class Move():
    def __init__(self, name, type, stat, power, accuracy):
        self.name = name
        self.type = type
        self.stat = stat
        self.power = power
        self.accuracy = accuracy

    def __str__(self):
        return self.name

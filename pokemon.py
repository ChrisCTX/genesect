class Pokemon():
    def __init__(self, name, type1, type2, movepool):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.movepool = movepool

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

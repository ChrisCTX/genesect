all_types = ["Bug", "Dark", "Dragon", "Electric", "Fighting", "Fire",
             "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal",
             "Poison", "Psychic", "Rock", "Steel", "Water", None]

supes = {
        "Normal": [],
        "Fire": ["Grass", "Ice", "Bug", "Steel"],
        "Water": ["Fire", "Ground", "Rock"],
        "Electric": ["Water", "Flying"],
        "Grass": ["Water", "Ground", "Rock"],
        "Ice": ["Grass", "Ground", "Flying", "Dragon"],
        "Fighting": ["Normal", "Ice", "Rock", "Dark", "Steel"],
        "Poison": ["Grass"],
        "Ground": ["Fire", "Electric", "Poison", "Rock", "Steel"],
        "Flying": ["Grass, Fighting, Bug"],
        "Psychic": ["Fighting", "Poison"],
        "Bug": ["Grass", "Psychic", "Dark"],
        "Rock": ["Fire", "Ice", "Flying", "Bug"],
        "Ghost": ["Psychic", "Ghost"],
        "Dragon": ["Dragon"],
        "Dark": ["Psychic", "Ghost"],
        "Steel": ["Ice", "Rock"]
    }

def isSuperEffective(attacker_type, victim_type):
    return True if victim_type in supes[attacker_type] else False

def getSECoverage(move_type):
    return supes[move_type]

def getUsageDict():
    types = {}
    for type in all_types:
        types[type] = 0
    return types

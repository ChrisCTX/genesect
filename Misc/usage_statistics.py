
class UsageStatistics():
    def __init__(self, stats_file):
        pass

    def generate(self):
        pass

with open("data/ranked_stats.txt") as stats_file:
    content = stats_file.readlines()

    with open("clean_stats.txt", "w") as new:
        for line in content:
            clean = line.split(' ')
            new.write(clean[0] + "," + clean[2])




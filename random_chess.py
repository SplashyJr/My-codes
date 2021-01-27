import random

team1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

team2 = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]


matchups = list(zip(team1, team2))
random.shuffle(matchups)
team1[:], team2[:] = zip(*matchups)

print(matchups)

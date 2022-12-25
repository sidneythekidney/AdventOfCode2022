# Read through all of the entries

beats = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

strategy = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

strategy_points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

lines = []
with open("input.txt") as f:
    lines = f.readlines()

strategy_score = 0

for line in lines:
    [opponent, you] = line.strip().split(' ')
    if strategy[opponent] == strategy[you]:
        strategy_score += 3
    elif beats[strategy[opponent]] == strategy[you]:
        strategy_score += 0
    else:
        strategy_score += 6
    strategy_score += strategy_points[strategy[you]]

print("Final strategy score: " + str(strategy_score))
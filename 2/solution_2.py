# Read through all of the entries

loses = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

beats = {
    "Scissors": "Rock",
    "Rock": "Paper",
    "Paper": "Scissors" 
}

strategy = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
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
    if you == 'X':
        strategy_score += strategy_points[loses[strategy[opponent]]]
    elif you == 'Y':
        strategy_score += 3 + strategy_points[strategy[opponent]]
    else:
        strategy_score += 6 + strategy_points[beats[strategy[opponent]]]

print("Final strategy score: " + str(strategy_score))
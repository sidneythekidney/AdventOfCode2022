with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

trees = [[int(tree) for tree in line] for line in lines]

best_scenic_score = 0

for i in range(len(trees)):
    for j in range(len(trees[i])):
        # Look in ech direction to determine scenic score
        left_score = 0
        for k in range(j-1, -1, -1):
            left_score += 1
            if trees[i][k] >= trees[i][j]:
                break
        right_score = 0
        for k in range(j+1, len(trees[i])):
            right_score += 1
            if trees[i][k] >= trees[i][j]:
                break
        bottom_score = 0
        for k in range(i+1, len(trees)):
            bottom_score += 1
            if trees[k][j] >= trees[i][j]:
                break
        top_score = 0
        for k in range(i-1, -1, -1):
            top_score += 1
            if trees[k][j] >= trees[i][j]:
                break
        best_scenic_score = max(best_scenic_score, left_score * right_score * top_score * bottom_score)

print("Best scenic score: " + str(best_scenic_score))
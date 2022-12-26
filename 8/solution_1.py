with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

trees = [[int(tree) for tree in line] for line in lines]

# Create tree cover maps
left_cover = [[-1 for _ in tree_row] for tree_row in trees]
right_cover = [[-1 for _ in tree_row] for tree_row in trees]
bottom_cover = [[-1 for _ in tree_row] for tree_row in trees]
top_cover = [[-1 for _ in tree_row] for tree_row in trees]

for i in range(len(trees)):
    for j in range(len(trees[i])):
        # Top cover
        if i != 0:
            top_cover[i][j] = max(top_cover[i-1][j], trees[i-1][j])
        # Left cover
        if j != 0:
            left_cover[i][j] = max(left_cover[i][j-1], trees[i][j-1])

for i in range(len(trees)-1, -1, -1):
    for j in range(len(trees[i])-1, -1, -1):
        # Bottom cover
        if i != len(trees)-1:
            bottom_cover[i][j] = max(bottom_cover[i+1][j], trees[i+1][j])
        # Right cover
        if j != len(trees[i])-1:
            right_cover[i][j] = max(right_cover[i][j+1], trees[i][j+1])

visible_trees = 0

for i in range(len(trees)):
    for j in range(len(trees[i])):
        if top_cover[i][j] < trees[i][j] or bottom_cover[i][j] < trees[i][j] or left_cover[i][j] < trees[i][j] or right_cover[i][j] < trees[i][j]:
            visible_trees += 1

print("Number of visible trees: " + str(visible_trees))
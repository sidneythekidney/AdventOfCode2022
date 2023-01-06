with open("input.txt") as f:
    lines = f.readlines()

# Create 2d grid of heights
heights = [[x for x in line.strip()] for line in lines]
visited = [[0 for _ in line.strip()] for line in lines]

# Find starting location
for i in range(len(heights)):
    for j in range(len(heights[i])):
        if heights[i][j] == 'S':
            start = [i, j]
        if heights[i][j] == 'E':
            end = [i, j]
            heights[i][j] = 'z'

best_path = 0

# Perform breadth first search
visited[start[0]][start[1]] = 1
exploring = [[start[0], start[1], 0]] # [x, y, length of path there]
while len(exploring):
    # Get the first element from the queue and mark as visited
    [i, j, length] = exploring[0]

    # Check to see if we reach the end and return
    if [i, j] == end:
        best_path = length
        break

    # Check in all direction adding coordinautes to queue as necessary
    # Check left
    if j != 0 and visited[i][j-1] == 0 and (heights[i][j].isupper() or ord(heights[i][j-1]) - ord(heights[i][j]) <= 1):
        exploring.append([i, j-1, length+1])
        visited[i][j-1] = 1
    # Check right
    if j != len(heights[i])-1 and visited[i][j+1] == 0 and (heights[i][j].isupper() or ord(heights[i][j+1]) - ord(heights[i][j]) <= 1):
        exploring.append([i, j+1, length+1])
        visited[i][j+1] = 1
    # Check up
    if i != 0 and visited[i-1][j] == 0 and (heights[i][j].isupper() or ord(heights[i-1][j]) - ord(heights[i][j]) <= 1):
        exploring.append([i-1, j, length+1])
        visited[i-1][j] = 1
    # Check down
    if i != len(heights)-1 and visited[i+1][j] == 0 and (heights[i][j].isupper() or ord(heights[i+1][j]) - ord(heights[i][j]) <= 1):
        exploring.append([i+1, j, length+1])
        visited[i+1][j] = 1

    # Remove the explored element from the queue
    exploring = exploring[1:]

if best_path != 0:
    print("Best path length: " + str(best_path))
else:
    print("No valid path found")
    exit(1)
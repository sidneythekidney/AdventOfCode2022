with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

tail_visited = set()

head = [0, 0]
tail = [0, 0]

tail_visited.add('0,0')

for line in lines:
    [direction, magnitude] = line.split(' ')
    magnitude = int(magnitude)
    for i in range(magnitude):
        # Move the head in the correct direction
        if direction == 'U':
            head[0] += 1
        elif direction == 'D':
            head[0] -= 1
        elif direction == 'L':
            head[1] -= 1
        else:
            head[1] += 1
        
        # Move the tail to be closer to the head if needed
        if abs(head[0] - tail[0]) >= 2:
            if head[0] > tail[0]:
                # Move tail up
                tail[0] += 1
            else:
                # Move tail down
                tail[0] -= 1
            # Move tail diagonally if needed
            if head[1] > tail[1]:
                # Move tail right
                tail[1] += 1
            elif head[1] < tail[1]:
                # Move tail left
                tail[1] -= 1

        if abs(head[1] - tail[1]) >= 2:
            if head[1] < tail[1]:
                # Move tail left
                tail[1] -= 1
            else:
                # Move tail right
                tail[1] += 1
            # Move tail diagonally if needed
            if head[0] > tail[0]:
                # Move tail up
                tail[0] += 1
            if head[0] < tail[0]:
                # Move tail down
                tail[0] -= 1
        
        # Add tail position to set
        tail_visited.add(','.join([str(dimension) for dimension in tail]))

print("Number of locations visited by tail: " + str(len(tail_visited)))

CRT_WIDTH = 40
CRT_HEIGHT = 6

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

register = 1
cycle = 1

addx_cycle_length = 2

crt = []

for line in lines:
    parsed_line = line.split(' ')
    cmd = parsed_line[0]
    if len(parsed_line) > 1:
        val = int(parsed_line[1])

    if cmd == 'addx':
        for i in range(addx_cycle_length):
            # Draw the pixel
            if abs(len(crt) % CRT_WIDTH - register) <= 1:
                crt.append('#')
            else:
                crt.append('.')
            cycle += 1
        register += val
    else:
        # Draw the pixel
        if abs(len(crt) % CRT_WIDTH - register) <= 1:
            crt.append('#')
        else:
            crt.append('.')
        cycle += 1

print("CRT:")
# Print CRT
for i in range(CRT_HEIGHT):
    for j in range(CRT_WIDTH):
        print(crt[CRT_WIDTH * i + j] + ' ', end='')
    print()

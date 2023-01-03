with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

register = 1
signal_strengths = 0
cycle = 1

addx_cycle_length = 2

for line in lines:
    parsed_line = line.split(' ')
    cmd = parsed_line[0]
    if len(parsed_line) > 1:
        val = int(parsed_line[1])

    if cmd == 'addx':
        for i in range(addx_cycle_length):
            if cycle % 40 == 20:
                signal_strengths += cycle * register
            cycle += 1
        register += val
    else:
        if cycle % 40 == 20:
            signal_strengths += cycle * register
        cycle += 1

print("Total signal strength: " + str(signal_strengths))

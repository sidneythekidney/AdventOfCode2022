with open('input.txt') as f:
    lines = f.readlines()

stacks = []

# Find blank line
blank_line = 0
for line in lines:
    if len(line) == 1:
        break
    else:
        blank_line += 1

number_of_stacks = int(lines[blank_line-1].strip()[-1])

# Add number of stacks
for i in range(number_of_stacks):
    stacks.append([])

# Add entries to initial stack
if blank_line - 2 < 0:
    print("Error with initial input")
    exit()

bottom_line = blank_line - 2

for i in range(bottom_line, -1, -1):
    stack_number = 0
    for j in range(1, len(lines[i]), 4):
        if lines[i][j] not in [' ', '\n']:
            stacks[stack_number].append(lines[i][j])
        stack_number += 1

first_command_line = blank_line + 1

for i in range(first_command_line, len(lines)):
    # Parse command string
    command = lines[i].split(' ')[1::2]
    [crate_number, from_stack, to_stack] = [int(i.strip()) for i in command]
    
    moved_crates = stacks[from_stack-1][-1*crate_number:]
    stacks[from_stack-1] = stacks[from_stack-1][:-1*crate_number]
    stacks[to_stack-1] += moved_crates

top_crates = ''.join([i[-1] for i in stacks])
print(top_crates)
import ast
import functools  

def determine_in_order(first, second):
    # Parse input
    for i in range(min(len(first), len(second))):
        if type(first[i]) is int and type(second[i]) is int:
            if first[i] < second[i]:
                return 1
            elif first[i] > second[i]:
                return -1
        elif type(first[i]) is list and type(second[i]) is list:
            in_order = determine_in_order(first[i], second[i])
            if in_order != 0:
                return in_order
        elif type(first[i]) is list and type(second[i]) is int:
            in_order = determine_in_order(first[i], [second[i]])
            if in_order != 0:
                return in_order
        else:
            in_order = determine_in_order([first[i]], second[i])
            if in_order != 0:
                return in_order

    if len(first) < len(second):
        return 1
    elif len(first) > len(second):
        return -1
    return 0

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

all_packets = [[[2]], [[6]]] # initialize with divider packets

for i in range(0, len(lines), 3):
    all_packets.append(ast.literal_eval(lines[i]))
    all_packets.append(ast.literal_eval(lines[i+1]))

cmp = functools.cmp_to_key(determine_in_order)
all_packets.sort(key=cmp, reverse=True)

# Find the divider elements
divider_index_1 = all_packets.index([[2]]) + 1
divider_index_2 = all_packets.index([[6]]) + 1

print("Decoder key: " + str(divider_index_1 * divider_index_2))
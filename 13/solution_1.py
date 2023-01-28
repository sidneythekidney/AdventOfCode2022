import ast    

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

sum_of_inorder_indices = 0

for i in range(0, len(lines), 3):
    first = ast.literal_eval(lines[i])
    second = ast.literal_eval(lines[i+1])

    is_in_order = determine_in_order(first, second)
    if is_in_order == 1:
        sum_of_inorder_indices += (i // 3 + 1)

print("Sum of inorder indices: " + str(sum_of_inorder_indices))
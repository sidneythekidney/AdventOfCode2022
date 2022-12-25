lines = []

with open("input.txt") as f:
    lines = f.readlines()

total_priority = 0

for line in lines:
    line = line.strip()
    first_compartment = line[:len(line)//2]
    second_compartment = line[len(line)//2:]
    for letter in second_compartment:
        if letter in first_compartment:
            # Add priority
            if letter.isupper():
                total_priority += ord(letter) - ord('A') + 27
            else:
                total_priority += ord(letter) - ord('a') + 1
            break

print("Total priority: " + str(total_priority))

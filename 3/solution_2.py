lines = []

with open("input.txt") as f:
    lines = f.readlines()

total_priority = 0

for line in lines:
    line = line.strip()

for i in range(0, len(lines), 3):
    compartments = lines[i: i+3]
    item_count = {}
    found = False
    for compartment in compartments:
        found_items = ""
        for item in compartment:
            if item not in found_items:
                if item not in item_count.keys():
                    item_count[item] = 1
                else:
                    item_count[item] += 1
                    if item_count[item] == 3:
                        # This is the badge, Add priority
                        if item.isupper():
                            total_priority += ord(item) - ord('A') + 27
                        else:
                            total_priority += ord(item) - ord('a') + 1
                        found = True
                        break
                found_items += item

        if (found == True):
            break

print("Total priority: " + str(total_priority))

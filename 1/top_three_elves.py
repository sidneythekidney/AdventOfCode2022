with open('input.txt') as f:
    lines = f.readlines()

max_elf_calories = 0
current_elf_calories = 0

calories_by_elf = []

for line in lines:
    line = line.strip()
    if len(line) == 0:
        calories_by_elf.append(current_elf_calories)
        current_elf_calories = 0
    else:
        current_elf_calories += int(line)
calories_by_elf.append(current_elf_calories)

calories_by_elf.sort(reverse=True)

print("Max calories: " + str(sum(calories_by_elf[:3])))
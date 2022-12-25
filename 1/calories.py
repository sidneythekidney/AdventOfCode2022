with open('input.txt') as f:
    lines = f.readlines()

max_elf_calories = 0
current_elf_calories = 0

for line in lines:
    line = line.strip()
    if len(line) == 0:
        max_elf_calories = max(max_elf_calories, current_elf_calories)
        current_elf_calories = 0
    else:
        current_elf_calories += int(line)

print("Max calories: " + str(max_elf_calories))
with open("input.txt") as f:
    pairings = f.readlines()

complete_overlaps = 0

for pair in pairings:
    [first_elf, second_elf] = pair.split(',')
    first_elf_tasks = first_elf.split('-')
    second_elf_tasks = second_elf.split('-')

    first_elf_tasks = [int(i) for i in first_elf_tasks]
    second_elf_tasks = [int(i) for i in second_elf_tasks]

    if first_elf_tasks[0] <= second_elf_tasks[0] and first_elf_tasks[1] >= second_elf_tasks[1]:
        complete_overlaps += 1

    elif second_elf_tasks[0] <= first_elf_tasks[0] and second_elf_tasks[1] >= first_elf_tasks[1]:
        complete_overlaps += 1

print("Complete overlaps: " + str(complete_overlaps))
directory_sizes = {
    '/': 0
}

directory_files = {}

with open('input.txt') as f:
    lines = f.readlines()

current_path = ['/']

for line in lines:
    command = [i.strip() for i in line.split(' ')]
    # parse command
    if command[0] == '$' and command[1] == 'cd':
        if command[2] == '..':
            # Remove the last element from the current path
            current_path.pop()
        elif command[2] == '/':
            current_path = ['/']
        else:
            current_path.append(command[2])
            if '/'.join(current_path) not in directory_sizes.keys():
                directory_sizes['/'.join(current_path)] = 0
            
    elif command[0].isdigit():
        current_path_as_string = '/'.join(current_path)
        if current_path_as_string not in directory_files.keys():
            directory_files[current_path_as_string] = set()

        # Make sure we don't count the same file twice
        if command[1] not in directory_files[current_path_as_string]:
            directory_files[current_path_as_string].add(command[1])
            for i in range(len(current_path)):
                directory_sizes['/'.join(current_path[0:i+1])] += int(command[0])

relevant_directories_size = 0
for directory, size in directory_sizes.items():
    if size <= 100000:
        relevant_directories_size += size

print("Directories of size at most 100000 combined sizes: " + str(relevant_directories_size))
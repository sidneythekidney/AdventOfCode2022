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

required_space = 30000000
total_file_space = 70000000
total_files_size = directory_sizes["/"]

directory_to_delete_size = total_files_size

for directory, size in directory_sizes.items():
    if total_file_space - total_files_size + size >= required_space and size < directory_to_delete_size:
        directory_to_delete_size = size

print("Size of smallest directory that would free up enough space: " + str(directory_to_delete_size))
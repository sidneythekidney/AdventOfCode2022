def is_out_of_bounds(cube, min_x, max_x, min_y, max_y, min_z, max_z):
    if cube[0] < min_x or cube[0] > max_x or cube[1] < min_y or cube[1] > max_y or cube[2] < min_z or cube[2] > max_z:
        return True
    return False

def is_exterior(cubes, cube, min_x, max_x, min_y, max_y, min_z, max_z):
    # Create a stack to perform dfs to determine if a cube is covered
    if cube in cubes:
        return False
    visited = []
    stack = [cube]
    while len(stack) > 0:
        current_cube = stack.pop()
        if current_cube in visited:
            continue
        visited.append(current_cube)

        # Check to see if cube is out of bounds, retur true if it is
        if (is_out_of_bounds(current_cube, min_x, max_x, min_y, max_y, min_z, max_z)):
            return True
        # Consider all the cubes in other directions
        if ([current_cube[0]-1, current_cube[1], current_cube[2]] not in cubes and [current_cube[0]-1, current_cube[1], current_cube[2]] not in visited):
            stack.append([current_cube[0]-1, current_cube[1], current_cube[2]])

        if ([current_cube[0]+1, current_cube[1], current_cube[2]] not in cubes and [current_cube[0]+1, current_cube[1], current_cube[2]] not in visited):
            stack.append([current_cube[0]+1, current_cube[1], current_cube[2]])

        if ([current_cube[0], current_cube[1]-1, current_cube[2]] not in cubes and [current_cube[0], current_cube[1]-1, current_cube[2]] not in visited):
            stack.append([current_cube[0], current_cube[1]-1, current_cube[2]])

        if ([current_cube[0], current_cube[1]+1, current_cube[2]] not in cubes and [current_cube[0], current_cube[1]+1, current_cube[2]] not in visited):
            stack.append([current_cube[0], current_cube[1]+1, current_cube[2]])

        if ([current_cube[0], current_cube[1], current_cube[2]-1] not in cubes and [current_cube[0], current_cube[1], current_cube[2]-1] not in visited):
            stack.append([current_cube[0], current_cube[1], current_cube[2]-1])
        
        if ([current_cube[0], current_cube[1], current_cube[2]+1] not in cubes and [current_cube[0], current_cube[1], current_cube[2]+1] not in visited):
            stack.append([current_cube[0], current_cube[1], current_cube[2]+1])

    return False

cubes = []

with open('input.txt') as f:
    lines = f.readlines()
    for a in lines:
        cubes.append([eval(i) for i in a.strip().split(',')])

# Find max x,y,z
max_x = 0
max_y = 0
max_z = 0

# Find min x, y, z
min_x = 100000000
min_y = 100000000
min_z = 100000000

surface_area = 0
num_cube = 1

for cube in cubes:
    max_x = max(max_x, cube[0])
    max_y = max(max_y, cube[1])
    max_z = max(max_z, cube[2])

    min_x = min(min_x, cube[0])
    min_y = min(min_y, cube[1])
    min_z = min(min_z, cube[2])

for cube in cubes:
    print("cube #" + str(num_cube))
    # Check for exterior cube sides
    if is_exterior(cubes, [cube[0]-1, cube[1], cube[2]], min_x, max_x, min_y, max_y, min_z, max_z):
        surface_area += 1
    if is_exterior(cubes, [cube[0]+1, cube[1], cube[2]], min_x, max_x, min_y, max_y, min_z, max_z):
        surface_area += 1
    if is_exterior(cubes, [cube[0], cube[1]-1, cube[2]], min_x, max_x, min_y, max_y, min_z, max_z):
        surface_area += 1
    if is_exterior(cubes, [cube[0], cube[1]+1, cube[2]], min_x, max_x, min_y, max_y, min_z, max_z):
        surface_area += 1
    if is_exterior(cubes, [cube[0], cube[1], cube[2]-1], min_x, max_x, min_y, max_y, min_z, max_z):
        surface_area += 1
    if is_exterior(cubes, [cube[0], cube[1], cube[2]+1], min_x, max_x, min_y, max_y, min_z, max_z):
        surface_area += 1

    num_cube += 1

print("final exterior surface area: " + str(surface_area))

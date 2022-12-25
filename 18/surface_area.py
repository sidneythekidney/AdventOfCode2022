def is_exterior(cubes, cube):
    pass

cubes = []

with open('sample_input.txt') as f:
    lines = f.readlines()
    for a in lines:
        cubes.append(a.strip().split(','))

surface_area = 0

num_cube = 1

for cube in cubes:
    # Check each face of the cube to determine if it is exterior
    if is_exterior(cubes, [cube[0]-1, cube[1], cube[2]]):
        surface_area += 1
    if is_exterior(cubes, [cube[0]+1, cube[1], cube[2]]):
        surface_area += 1
    if is_exterior(cubes, [cube[0], cube[1]-1, cube[2]]):
        surface_area += 1
    if is_exterior(cubes, [cube[0]-1, cube[1]+1, cube[2]]):
        surface_area += 1
    if is_exterior(cubes, [cube[0], cube[1], cube[2]-1]):
        surface_area += 1
    if is_exterior(cubes, [cube[0]-1, cube[1], cube[2+1]]):
        surface_area += 1

    num_cube += 1

print("final surface area: " + str(surface_area))

from collections import defaultdict


cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

with open("input.txt") as inp:
    for i, line in enumerate(inp.readlines()):
        line = line.strip()
        for j, elem in enumerate(line):
            if elem == "#":
                cubes[i][j][0] = 1
                
    

min_i, min_j, min_z = -1, -1, -1
max_i, max_j, max_z = len(cubes)-1, len(cubes)-1, len(cubes)-1

                
def count_active_nei(i, j, z):
    active = 0
    for diff_i in range(-1, 2):
        for diff_j in range(-1, 2):
            for diff_z in range(-1, 2):
                if (diff_i, diff_j, diff_z) != (0, 0, 0):
                    if cubes[i+diff_i][j+diff_j][z+diff_z] == 1:
                        active += 1
    return active


for i in range(6):
    new_cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for i in range(min_i-1, max_i+2):
        for j in range(min_j-1, max_j+2):
            for z in range(min_z-1, max_z+2):
                new_cubes[i][j][z] = cubes[i][j][z]
                active = count_active_nei(i, j, z)
                if cubes[i][j][z] == 1:
                    if active not in [2, 3]:
                        new_cubes[i][j][z] = 0
                elif cubes[i][j][z] == 0:
                    if active == 3:
                        new_cubes[i][j][z] = 1
                        min_i = min(min_i, i)
                        min_j = min(min_j, j)
                        min_z = min(min_z, z)
                        max_i = max(max_i, i)
                        max_j = max(max_j, j)
                        max_z = max(max_z, z)

    cubes = new_cubes




active = 0
for i in range(min_i-1, max_i+2):
        for j in range(min_j-1, max_j+2):
            for z in range(min_z-1, max_z+2):
                if cubes[i][j][z] == 1:
                    active += 1

print(active)


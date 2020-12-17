from collections import defaultdict


cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))

with open("input.txt") as inp:
    for i, line in enumerate(inp.readlines()):
        line = line.strip()
        for j, elem in enumerate(line):
            if elem == "#":
                cubes[i][j][0][0] = 1
                
    

min_i, min_j, min_z, min_w = -1, -1, -1, -1
max_i, max_j, max_z, max_w = len(cubes)-1, len(cubes)-1, len(cubes)-1, len(cubes)-1



                
def count_active_nei(i, j, z, w):
    active = 0
    for diff_i in range(-1, 2):
        for diff_j in range(-1, 2):
            for diff_z in range(-1, 2):
                for diff_w in range(-1, 2):
                    if (diff_i, diff_j, diff_z, diff_w) != (0, 0, 0, 0):
                        if cubes[i+diff_i][j+diff_j][z+diff_z][w+diff_w] == 1:
                            active += 1
    return active


for i in range(6):
    new_cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    for i in range(min_i-1, max_i+2):
        for j in range(min_j-1, max_j+2):
            for z in range(min_z-1, max_z+2):
                for w in range(min_w-1, max_w+2):
                    new_cubes[i][j][z][w] = cubes[i][j][z][w]
                    active = count_active_nei(i, j, z, w)
                    if cubes[i][j][z][w] == 1:
                        if active not in [2, 3]:
                            new_cubes[i][j][z][w] = 0
                    elif cubes[i][j][z][w] == 0:
                        if active == 3:
                            new_cubes[i][j][z][w] = 1
                            min_i = min(min_i, i)
                            min_j = min(min_j, j)
                            min_z = min(min_z, z)
                            min_w = min(min_w, w)
                            max_i = max(max_i, i)
                            max_j = max(max_j, j)
                            max_z = max(max_z, z)
                            max_w = max(max_w, w)

    cubes = new_cubes




active = 0
for i in range(min_i-1, max_i+2):
        for j in range(min_j-1, max_j+2):
            for z in range(min_z-1, max_z+2):
                for w in range(min_w-1, max_w+2):
                    if cubes[i][j][z][w] == 1:
                        active += 1

print(active)


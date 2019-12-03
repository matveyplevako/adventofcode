from collections import defaultdict

with open("input.txt") as inp:
    wire1 = inp.readline().split(",")
    wire2 = inp.readline().split(",")

grid = defaultdict(lambda: defaultdict(int))

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

i, j = 0, 0
for d in wire1:
    direction = d[0]
    num = int(d[1:])
    p = directions[direction]
    for _ in range(num):
        x, y = p
        i += x
        j += y
        grid[i][j] = 1

intersect = None

i, j = 0, 0
for d in wire2:
    direction = d[0]
    num = int(d[1:])
    p = directions[direction]
    for _ in range(num):
        x, y = p
        i += x
        j += y
        if (i + j != 0) and grid[i][j] == 1 and ((intersect is None) or (abs(i) + abs(j) < intersect)):
            intersect = abs(i) + abs(j)

print(intersect)

with open("out1.txt", "w") as out:
    out.write(str(intersect) + '\n')

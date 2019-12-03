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

w1_steps = defaultdict(lambda: defaultdict(int))
cur_step = 1

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
        w1_steps[i][j] = min(cur_step, w1_steps[i][j]) if w1_steps[i][j] != 0 else cur_step
        cur_step += 1

intersect = None

i, j = 0, 0
cur_step = 0
for d in wire2:
    direction = d[0]
    num = int(d[1:])
    p = directions[direction]
    for _ in range(num):
        x, y = p
        i += x
        j += y
        cur_step += 1
        if (i + j != 0) and grid[i][j] == 1 and ((intersect is None) or (intersect > cur_step + w1_steps[i][j])):
            intersect = cur_step + w1_steps[i][j]

print(intersect)

with open("out2.txt", "w") as out:
    out.write(str(intersect) + '\n')

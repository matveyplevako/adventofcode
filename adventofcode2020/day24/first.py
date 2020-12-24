from collections import defaultdict

grid = defaultdict(lambda: defaultdict(bool))

black = 0

directions = {
    'w': (-1, 0),
    'sw': (0, -1,),
    'se': (1, -1),
    'e': (1, 0),
    'ne': (0, 1),
    'nw': (-1, 1)
}


def color_tile(instructions):
    global black
    i = 0
    x, y = 0, 0
    while i < len(instructions):
        inst = instructions[i]
        if inst in ['s', 'n']:
            i += 1
            inst = instructions[i-1:i+1]

        dx, dy = directions[inst]
        x += dx
        y += dy
        i += 1

    if grid[x][y]:
        black -= 1
    else:
        black += 1
    grid[x][y] = not grid[x][y]


with open('input.txt') as inp:
    for line in inp.readlines():
        line = line.strip()
        color_tile(line)

print(black)



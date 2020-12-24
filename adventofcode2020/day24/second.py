from collections import defaultdict

grid = defaultdict(lambda: defaultdict(bool))

black = 0

min_x, min_y, max_x, max_y = [None] * 4

directions = {
    'w': (-1, 0),
    'sw': (0, -1,),
    'se': (1, -1),
    'e': (1, 0),
    'ne': (0, 1),
    'nw': (-1, 1)
}


def color_tile(instructions):
    global black, grid
    global min_x, min_y, max_x, max_y
    i = 0
    x, y = 0, 0
    while i < len(instructions):
        inst = instructions[i]
        if inst in ['s', 'n']:
            i += 1
            inst = instructions[i - 1:i + 1]

        dx, dy = directions[inst]
        x += dx
        y += dy
        i += 1

    if grid[x][y]:
        black -= 1
    else:
        black += 1

    grid[x][y] = not grid[x][y]

    if min_x is None:
        min_x = x
    if min_y is None:
        min_y = y
    if max_x is None:
        max_x = x
    if max_y is None:
        max_y = y

    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)


def count_adjust(x, y):
    local_black = 0
    for direct in directions:
        dx, dy = directions[direct]
        if grid[x + dx][y + dy]:
            local_black += 1
    return local_black


def day():
    global min_x, min_y, max_x, max_y
    global black
    to_flip = []
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            adj = count_adjust(x, y)
            if grid[x][y] and (adj == 0 or adj > 2):
                black -= 1
                to_flip.append((x, y))
            elif not grid[x][y] and adj == 2:
                black += 1
                to_flip.append((x, y))

                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    for flip in to_flip:
        grid[flip[0]][flip[1]] = not grid[flip[0]][flip[1]]


with open('input.txt') as inp:
    for line in inp.readlines():
        line = line.strip()
        color_tile(line)

for i in range(100):
    day()
print(black)


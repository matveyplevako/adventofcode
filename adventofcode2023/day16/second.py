cave_map = []

directions = {
    1: (0, 1),
    3: (0, -1),
    2: (1, 0),
    4: (-1, 0),
}

mirror_1 = {
    1: 4,
    2: 3,
    3: 2,
    4: 1
}

mirror_2 = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

visited = set()


def dfs(ni, nj, direction):
    """
    1 >
    2 v
    3 <
    4 ^
    """
    while True:
        di, dj = directions[direction]
        ni, nj = ni + di, nj + dj
        if not len(cave_map) > ni >= 0 or not len(cave_map[0]) > nj >= 0:
            return
        if (ni, nj, direction) in visited:
            return
        visited.add((ni, nj, direction))
        if cave_map[ni][nj] == '.':
            continue
        elif cave_map[ni][nj] == '/':
            direction = mirror_1[direction]
        elif cave_map[ni][nj] == '\\':
            direction = mirror_2[direction]
        elif direction in [1, 3] and cave_map[ni][nj] == '-':
            continue
        elif direction in [2, 4] and cave_map[ni][nj] == '|':
            continue
        elif direction in [1, 3] and cave_map[ni][nj] == "|":
            dfs(ni, nj, 2)
            dfs(ni, nj, 4)
            return
        elif direction in [2, 4] and cave_map[ni][nj] == "-":
            dfs(ni, nj, 1)
            dfs(ni, nj, 3)
            return


def main():
    global visited
    with open("input.txt") as inp:
        for line in inp.readlines():
            cave_map.append(list(line.strip()))

    mm = 0
    for j in range(len(cave_map[0])):
        dfs(-1, j, 2)
        mm = max(mm, len(set([(x[0], x[1]) for x in visited])))
        visited = set()

    for j in range(len(cave_map[0])):
        dfs(len(cave_map), j, 4)
        mm = max(mm, len(set([(x[0], x[1]) for x in visited])))
        visited = set()

    for i in range(len(cave_map)):
        dfs(i, -1, 1)
        mm = max(mm, len(set([(x[0], x[1]) for x in visited])))
        visited = set()

    for i in range(len(cave_map)):
        dfs(i, len(cave_map[0]), 3)
        mm = max(mm, len(set([(x[0], x[1]) for x in visited])))
        visited = set()

    print(mm)


if __name__ == '__main__':
    main()

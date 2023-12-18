from collections import defaultdict

cave_map = defaultdict(lambda: defaultdict(bool))

directions = {
    "R": (0, 1),
    "L": (0, -1),
    "D": (1, 0),
    "U": (-1, 0),
}


def flood_fill(i, j):
    s = {(i, j)}
    used = set()
    c = 0
    while s:
        i, j = s.pop()
        if (i, j) in used:
            continue
        c += 1
        used.add((i, j))
        for di, dj in directions.values():
            ni, nj = i + di, j + dj
            if not cave_map[ni][nj]:
                s.add((ni, nj))
    return c


def main():
    i, j = 0, 0
    min_i, max_i = 0, 0
    min_j, max_j = 0, 0
    total = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            direction, length, color = line.split()
            di, dj = directions[direction]
            for _ in range(int(length)):
                i += di
                j += dj
                cave_map[i][j] = True
                total += 1

            max_i = max(max_i, i)
            max_j = max(max_j, j)
            min_i = min(min_i, i)
            min_j = min(min_j, i)

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if cave_map[i][j]:
                total += flood_fill(i + 1, j + 1)
                print(total)
                return

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if cave_map[i][j]:
                print(1, end='')
            else:
                print(' ', end='')
        print()


if __name__ == '__main__':
    main()

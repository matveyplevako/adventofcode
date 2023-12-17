from collections import defaultdict
from heapq import heappop, heappush

cave_map = []
minimal_cost = defaultdict(lambda: defaultdict(lambda: 10 ** 6))

dx = {(-1, 0), (1, 0), (0, -1), (0, 1)}


# dx = [(1, 0), (0, -1), (0, 1), (-1, 0)]


def draw_path(path):
    for i in range(len(cave_map)):
        for j in range(len(cave_map)):
            if (i, j) in path:
                print('.', end='')
            else:
                print(cave_map[i][j], end='')
        print()


def main():
    with open("input.txt") as inp:
        for line in inp.readlines():
            cave_map.append(list(map(int, line.strip())))

    s = [(0, 0, 0, 0, 0)]
    used = set()
    while s:
        cost, i, j, prev_di, prev_dj = heappop(s)
        if i == len(cave_map) - 1 and j == len(cave_map[0]) - 1:
            print(cost)
            break
        if (i, j, prev_di, prev_dj) in used:
            continue
        used.add((i, j, prev_di, prev_dj))
        for (di, dj) in dx - {(prev_di, prev_dj), (-prev_di, -prev_dj)}:
            ni, nj = i + di, j + dj
            c = cost
            for iter_num in range(1, 11):
                if not len(cave_map) > ni >= 0 or not len(cave_map[0]) > nj >= 0:
                    break
                c += cave_map[ni][nj]
                if iter_num >= 4:
                    heappush(s, (c, ni, nj, di, dj))
                ni += di
                nj += dj


if __name__ == '__main__':
    main()

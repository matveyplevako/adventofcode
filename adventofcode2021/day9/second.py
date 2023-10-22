from collections import defaultdict
from functools import reduce
from operator import mul

cave_map = defaultdict(lambda: defaultdict(lambda: 9))
adjust = ((0, -1), (0, 1), (1, 0), (-1, 0))


def check_if_smallest(i, j):
    for adj in adjust:
        if cave_map[i][j] >= cave_map[i + adj[0]][j + adj[1]]:
            return False
    return True


def get_basin_size(i, j, ):
    visited = set()
    q = [(i, j)]
    while q:
        point = q.pop(0)
        visited.add(point)
        for adj in adjust:
            next_point = (point[0] + adj[0], point[1] + adj[1])
            if cave_map[next_point[0]][next_point[1]] < 9 and next_point not in visited:
                q.append(next_point)
    return len(visited)


def main():
    basins = []
    with open("input.txt") as inp:
        cave_map_raw = inp.readlines()

    for i, line in enumerate(cave_map_raw):
        line = line.strip()
        for j, digit in enumerate(line):
            cave_map[i][j] = int(digit)

    for i in range(len(cave_map)):
        for j in range(len(cave_map[0])):
            if check_if_smallest(i, j):
                basins.append(get_basin_size(i, j))
    print(reduce(mul, sorted(basins, reverse=True)[:3]))


if __name__ == '__main__':
    main()

from collections import defaultdict
from itertools import combinations

space_map = defaultdict(lambda: defaultdict(lambda: '.'))


def main():
    galaxies = []
    with open("input.txt") as inp:
        for i, row in enumerate(inp.readlines()):
            for j, x in enumerate(row.strip()):
                space_map[i][j] = x
                if x == "#":
                    galaxies.append((i, j))

    expand_i = [i for i in range(len(space_map)) if i not in [x[0] for x in galaxies]]
    expand_j = [j for j in range(len(space_map[0])) if j not in [x[1] for x in galaxies]]

    dist = 0
    for g1, g2 in combinations(galaxies, 2):
        d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        for exp_i in expand_i:
            if min(g1[0], g2[0]) < exp_i < max(g1[0], g2[0]):
                d += 1
        for exp_j in expand_j:
            if min(g1[1], g2[1]) < exp_j < max(g1[1], g2[1]):
                d += 1
        dist += d
    print(dist)

if __name__ == '__main__':
    main()

from collections import defaultdict

cave_map = defaultdict(lambda: defaultdict(lambda: 9))


def check_if_smallest(i, j):
    adjust = ((0, -1), (0, 1), (1, 0), (-1, 0))
    for adj in adjust:
        if cave_map[i][j] >= cave_map[i + adj[0]][j + adj[1]]:
            return False
    return True


def main():
    ans = 0
    with open("input.txt") as inp:
        cave_map_raw = inp.readlines()

    for i, line in enumerate(cave_map_raw):
        line = line.strip()
        for j, digit in enumerate(line):
            cave_map[i][j] = int(digit)

    for i in range(len(cave_map)):
        for j in range(len(cave_map[0])):
            if check_if_smallest(i, j):
                ans += cave_map[i][j] + 1

    print(ans)

if __name__ == '__main__':
    main()

from collections import defaultdict

cave_map = []
minimal_cost = defaultdict(lambda: defaultdict(int))


def main():
    with open("input.txt") as inp:
        for line in inp.readlines():
            cave_map.append(list(map(int, line.strip())))

    minimal_cost[0][0] = cave_map[0][0]


    print(*cave_map, sep='\n')


if __name__ == '__main__':
    main()

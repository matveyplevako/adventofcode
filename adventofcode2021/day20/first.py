from collections import defaultdict

cave_map = defaultdict(lambda: defaultdict(lambda: '.'))

M = 200


def get_pixel(i, j, encoder):
    order = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 0),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ][::-1]
    num = 0
    for ind, (di, dj) in enumerate(order):
        num += 2 ** ind * (0 if cave_map[i + di][j + dj] == '.' else 1)
    return encoder[num]


def step(encoder):
    new_cave_map = defaultdict(lambda: defaultdict(lambda: '.'))
    for i in range(-M, M):
        for j in range(-M, M):
            new_cave_map[i][j] = get_pixel(i, j, encoder)
    return new_cave_map


def print_cave():
    for i in range(-M + 1, M - 1):
        for j in range(-M + 1, M - 1):
            print(cave_map[i][j], end='')
        print()


def count_lights():
    c = 0
    for i in range(-M + 1, M - 1):
        for j in range(-M + 1, M - 1):
            c += cave_map[i][j] == '#'
    return c


def main():
    global cave_map
    with open("input.txt") as inp:
        encoder = inp.readline().strip()
        inp.readline()
        for i, row in enumerate(inp.readlines()):
            for j, value in enumerate(row.strip()):
                cave_map[i][j] = value

    cave_map = step(encoder)
    cave_map = step(encoder)
    # print_cave()
    print(count_lights())


if __name__ == '__main__':
    main()

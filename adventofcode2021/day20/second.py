from collections import defaultdict

cave_map = defaultdict(lambda: defaultdict(lambda: '.'))

L = -100
R = 200


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
    for i in range(L, R):
        for j in range(L, R):
            if i == L or i == R - 1 or j == L or j == R:
                new_cave_map[i][j] = '.' if cave_map[i][j] == '#' else '#'
            else:
                new_cave_map[i][j] = get_pixel(i, j, encoder)
    return new_cave_map


def print_cave():
    for i in range(L, R):
        for j in range(L, R):
            print(cave_map[i][j], end='')
        print()


def count_lights():
    c = 0
    for i in range(L, R):
        for j in range(L, R):
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

    for i in range(50):
        cave_map = step(encoder)
        print(i)
    # print_cave()
    print(count_lights())


if __name__ == '__main__':
    main()

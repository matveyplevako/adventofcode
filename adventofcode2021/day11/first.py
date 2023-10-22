from collections import defaultdict

cave_map = defaultdict(lambda: defaultdict(int))


def increase_energy():
    for i in range(10):
        for j in range(10):
            cave_map[i][j] += 1


def process_flash():
    visited = set()
    for i in range(10):
        for j in range(10):
            if cave_map[i][j] > 9:
                flash_octopus(i, j, visited)


def flash_octopus(octopus_i, octopus_j, visited):
    if (octopus_i, octopus_j) in visited:
        return
    visited.add((octopus_i, octopus_j))
    for i in range(-1, 2):
        for j in range(-1, 2):
            di, dj = octopus_i + i, octopus_j + j
            if (i, j) != (0, 0):
                cave_map[di][dj] += 1
                if (
                        0 <= di < 10 and
                        0 <= dj < 10 and
                        cave_map[di][dj] > 9
                ):
                    flash_octopus(di, dj, visited)


def zero_flashed():
    flashes = 0
    for i in range(10):
        for j in range(10):
            if cave_map[i][j] > 9:
                flashes += 1
                cave_map[i][j] = 0
    return flashes


def perform_step():
    increase_energy()
    process_flash()
    return zero_flashed()


def print_map():
    for i in range(10):
        for j in range(10):
            if cave_map[i][j] == 0:
                print("!", end='')
            else:
                print(cave_map[i][j], end='')
        print()
    print('-------')


def main():
    ans = 0
    with open("input.txt") as inp:
        cave_map_raw = inp.readlines()

    for i, line in enumerate(cave_map_raw):
        line = line.strip()
        for j, digit in enumerate(line):
            cave_map[i][j] = int(digit)

    for i in range(100):
        ans += perform_step()

    print(ans)


if __name__ == '__main__':
    main()

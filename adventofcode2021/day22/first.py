from collections import defaultdict

reactor_map = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))


def process(x, y, z, inst):
    for i in range(max(-50, x[0]), min(50, x[1]) + 1):
        for j in range(max(-50, y[0]), min(50, y[1]) + 1):
            for k in range(max(-50, z[0]), min(50, z[1]) + 1):
                reactor_map[i][j][k] = inst


def count_on():
    c = 0
    for i in range(-50, 51):
        for j in range(-50, 51):
            for k in range(-50, 51):
                if reactor_map[i][j][k]:
                    c += 1
    return c


def main():
    with open("input.txt") as inp:
        for line in inp.readlines():
            inst, region = line.strip().split()
            inst = 1 if inst == 'on' else 0
            x, y, z = list(map(lambda s: list(map(int, s.split('=')[1].split('..'))), region.split(',')))
            process(x, y, z, inst)

    print(count_on())


if __name__ == '__main__':
    main()

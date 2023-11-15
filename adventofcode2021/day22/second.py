def check_if_intersects(c1, c2):
    for i in range(1, 4):
        if max(c1[i][0], c2[i][0]) <= min(c1[i][1], c2[i][1]):
            return True
    return False


def volume_intersection(c1, c2):
    x_inter = max(c1[1][0], c2[1][0]), min(c1[1][1], c2[1][1])
    y_inter = max(c1[2][0], c2[2][0]), min(c1[2][1], c2[2][1])
    z_inter = max(c1[3][0], c2[3][0]), min(c1[3][1], c2[3][1])
    x = [c2[0] * -1, x_inter, y_inter, z_inter]
    if all(x[i][1] >= x[i][0] for i in range(1, 4)):
        return x


def get_volume(c):
    v = 1
    for i in range(1, 4):
        v *= c[i][1] - c[i][0] + 1
    return v


def main():
    cubes = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            inst, region = line.strip().split()
            x, y, z = list(map(lambda s: list(map(int, s.split('=')[1].split('..'))), region.split(',')))
            inst = 1 if inst == 'on' else -1
            cubes.append((inst, x, y, z))

    history = []
    for ind, cube in enumerate(cubes):
        for cube1 in history.copy():
            v = volume_intersection(cube, cube1)
            if v:
                history.append(v)
        if cube[0] > 0:
            history.append(cube)

    v = 0
    for h in history:
        v += h[0] * get_volume(h)
    print(v)


if __name__ == '__main__':
    main()

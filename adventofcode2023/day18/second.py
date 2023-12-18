directions = {
    "0": (0, 1),
    "2": (0, -1),
    "1": (1, 0),
    "3": (-1, 0),
}


def main():
    i, j = 0, 0
    v = []
    perimeter = 0
    total = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            _, _, color = line.split()
            direction = color[-2]
            di, dj = directions[direction]
            length = int(color[2:-2], 16)
            i += di * int(length)
            j += dj * int(length)
            perimeter += int(length)
            v.append((i, j))

    total = 0
    for i in range(len(v) - 1):
        j = (i + 1) % len(v)
        total += v[i][0] * v[j][1] - v[i][1] * v[j][0]
    print(int((abs(total) + perimeter) / 2 + 1))


if __name__ == '__main__':
    main()

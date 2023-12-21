from collections import defaultdict

garden_map = []
step_map = defaultdict(lambda: defaultdict(lambda: 10 ** 6))


def is_valid_step(i, j):
    i = i % len(garden_map)
    j = j % len(garden_map)
    return garden_map[i][j] != "#"


def main():
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            garden_map.append(list(line))

    s = None
    for i in range(len(garden_map)):
        for j in range(len(garden_map[0])):
            if garden_map[i][j] == "S":
                s = (i, j)

    q = [(0, s)]
    steps = 65
    # steps = 65 + 131
    # steps = 65 + 131 * 2
    # use it to build quadratic equation
    used = set()
    while q:
        step, (i, j) = q.pop(0)
        if (i, j) in used:
            continue
        step_map[i][j] = step % 2
        used.add((i, j))
        for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if is_valid_step(ni, nj) and step + 1 <= steps:
                q.append((step + 1, (ni, nj)))

    c = 0
    min_i = min([min(x) for x in step_map.values()])
    max_i = max([max(x) for x in step_map.values()])
    for i in range(min_i, max_i + 1):
        for j in range(min_i, max_i + 1):
            if steps % 2 == step_map[i][j]:
                c += 1
    print(c)

    x = 26501365
    x -= 65
    x //= 131
    print(3882 + 15338 * x + 15221 * x ** 2)


if __name__ == '__main__':
    main()

from math import sqrt, ceil, floor


def sum_of_progression(a, n):
    return (n / 2) * (2 * a + (n - 1) * -1)


def find_sol(a1, a):
    return a + sqrt(4 * a ** 2 + 4 * a - 8 * a1 + 1) / 2 + 1 / 2


def find_max(a):
    return a + 1 / 2


def find_all_possible(x1, x2, y1, y2):
    m = 0
    pairs = []
    for y in range(-1000, 1000):
        left = find_sol(y1, y)
        right = find_sol(y2, y)
        if ceil(left) == floor(right) or right - left > 1:
            for sub_y in range(int(ceil(left)), int(right) + 1):
                for x in range(1, 1000):
                    if x2 <= sum_of_progression(x, min(int(sub_y), x)) <= x1:
                        m += 1
                        pairs.append(f"{x},{y}")
    return pairs


def main():
    with open("input.txt") as inp:
        for i, line in enumerate(inp.readlines()):
            line = line.strip()
            x, y = line.split(', ')
            x2, x1 = map(int, x.lstrip('target area: x=').split('..'))
            y2, y1 = map(int, y.lstrip('y=').split('..'))

    m = find_all_possible(x1, x2, y1, y2)
    print(len(set(m)))


if __name__ == '__main__':
    main()

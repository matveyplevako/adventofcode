from math import sqrt, ceil, floor


def sum_of_progression(a, n):
    return (n / 2) * (2 * a + (n - 1) * -1)


def find_sol(a1, a):
    return a + sqrt(4 * a ** 2 + 4 * a - 8 * a1 + 1) / 2 + 1 / 2


def find_max(a):
    return a + 1 / 2


def find_y(y1, y2):
    m = 1
    for y in range(1, 10000):
        left = find_sol(y1, y)
        right = find_sol(y2, y)
        if ceil(left) == floor(right):
            m = y
    return m


def main():
    with open("input.txt") as inp:
        for i, line in enumerate(inp.readlines()):
            line = line.strip()
            _, y = line.split(', ')
            y2, y1 = map(int, y.lstrip('y=').split('..'))

    y = find_y(y1, y2)
    print(floor(sum_of_progression(y, find_max(y))))


if __name__ == '__main__':
    main()

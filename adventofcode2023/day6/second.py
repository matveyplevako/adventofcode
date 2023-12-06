def calc_dist(t, d):
    c = 0
    for h in range(1, t):
        if h * (t - h) > d:
            c += 1
    return c


def main():
    with open("input.txt") as inp:
        t = int(''.join(inp.readline().split(": ")[1].split()))
        d = int(''.join(inp.readline().split(": ")[1].split()))
        print(t, d)
        D = t ** 2 - 4 * d
        h1 = (-t + D ** (1/2)) / -2
        h2 = (-t - D ** (1/2)) / -2
        print(int(h2 - h1))


if __name__ == '__main__':
    main()

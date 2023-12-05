from functools import reduce, partial


def read_ranges(inp):
    ranges = []
    while True:
        s = inp.readline()
        if not s.strip():
            break
        ranges.append(list(map(int, s.split())))
    return ranges


def pass_through_filters(seed, filters):
    for f in filters:
        seed = pass_through_filter(seed, f)
    return seed


def pass_through_filter(seed, filters):
    for f in filters:
        if f[1] <= seed <= f[1] + f[2]:
            return f[0] + (seed - f[1])
    return seed


def rec_search(f, ind, start=None, end=None):
    if ind == 0:
        for p in f[0]:
            m1 = max(start, p[0])
            m2 = min(end, p[0] + p[1])
            if m1 <= m2:
                return m1, pass_through_filters(m1, f[1:])
        return
    seed_f = f[ind]
    m = None
    p = None
    for x in seed_f:
        m1 = max(start, x[0])
        m2 = min(end, x[0] + x[2])
        if m1 <= m2:
            dx = x[1] - x[0]
            res = rec_search(f, ind - 1, m1 + dx, m2 + dx)
            if res:
                if not m or res[1] < m:
                    m = res[1]
                    p = res
    return p


def main():
    with open("input.txt") as inp:
        seeds = list(map(int, inp.readline().split(": ")[1].split()))
        pairs = []
        for i in range(0, len(seeds), 2):
            pairs.append((seeds[i], seeds[i + 1]))
        seed_filters = []
        inp.readline()
        for i in range(7):
            inp.readline()
            filters = read_ranges(inp)
            m = min([x[1] for x in filters])
            if m != 0:
                filters.append([0, 0, m - 1])
            m = max([x[1] for x in filters])
            filters.append([m + 1, m + 1, 10 ** 9])
            seed_filters.append(filters)

    seed_filters.insert(0, pairs)
    s = rec_search(seed_filters, len(seed_filters) - 1, 0, 10 ** 9)
    print(s[1])


if __name__ == '__main__':
    main()

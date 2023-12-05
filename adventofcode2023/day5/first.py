
def read_ranges(inp):
    ranges = []
    while True:
        s = inp.readline()
        if not s.strip():
            break
        ranges.append(list(map(int, s.split())))
    return ranges


def pass_through_filter(seed, filters):
    for f in filters:
        if f[1] <= seed <= f[1] + f[2]:
            return f[0] + (seed - f[1])
    return seed


def main():
    m = None
    with open("input.txt") as inp:
        seeds = list(map(int, inp.readline().split(": ")[1].split()))
        seed_filters = []
        inp.readline()
        for i in range(7):
            inp.readline()
            filters = read_ranges(inp)
            seed_filters.append(filters)

        for seed in seeds:
            for f in seed_filters:
                seed = pass_through_filter(seed, f)
            if not m or seed < m:
                m = seed
    print(m)


if __name__ == '__main__':
    main()

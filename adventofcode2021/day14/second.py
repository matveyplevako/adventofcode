from collections import Counter

instructions = dict()


def main():
    with open("input.txt") as inp:
        poly = inp.readline().strip()
        inp.readline()
        for line in inp.readlines():
            state, new_elem = line.strip().split(' -> ')
            instructions[state] = new_elem

    c1 = Counter()
    for i in range(len(poly)-1):
        c1[poly[i:i+2]] += 1

    cf = Counter()
    for i in range(41):
        cf.clear()
        for k in c1:
            cf[k[0]] += c1[k]
        cf[poly[-1]] += 1

        c2 = Counter()
        # AB -> C AC BC
        for k in c1:
            c2[k[0] + instructions[k]] += c1[k]
            c2[instructions[k] + k[1]] += c1[k]
        c1 = c2

    print(max(cf.values()) - min(cf.values()))


if __name__ == '__main__':
    main()

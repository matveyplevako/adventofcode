from collections import Counter

instructions = dict()


def process_step(poly: str):
    new_ploy = poly[0]
    for i in range(len(poly) - 1):
        cut = poly[i:i + 2]
        if cut in instructions:
            cut = instructions[cut] + cut[1]
        new_ploy += cut

    return new_ploy


def main():
    with open("input.txt") as inp:
        poly = inp.readline().strip()
        inp.readline()
        for line in inp.readlines():
            state, new_elem = line.strip().split(' -> ')
            instructions[state] = new_elem

    for i in range(10):
        poly = process_step(poly)

    quantities = Counter(poly).values()
    print(max(quantities) - min(quantities))


if __name__ == '__main__':
    main()


def str_hash(x):
    return ''.join(sorted(x))


def get_base_number(numbers, size):
    return set(list([x for x in numbers if len(x) == size])[0])


def find_top_segment(seven, one):
    return (seven - one).pop()


def find_bottom_segment(numbers, seven, four):
    t = seven | four
    return ([set(x) for x in numbers if set(x).issuperset(t) and len(x) == 6][0] - t).pop()


def find_middle_segment(numbers, eight, four, one):
    def segment_filter(x):
        return len(x) == 6 and x.issuperset(one) and not x.issuperset(four)
    return (eight - [set(x) for x in numbers if segment_filter(set(x))][0]).pop()


def find_b_segment(numbers, seven, d, g):
    def segment_filter(x):
        return len(x) == 6 and x.issuperset(seven) and d in x and g in x
    nine = [set(x) for x in numbers if segment_filter(set(x))][0]
    return (nine - seven - {d} - {g}).pop()


def find_f_segment(numbers, a, g, d, b):
    def segment_filter(x):
        return len(x) == 5 and x.issuperset(segments)
    segments = {a, g, d, b}
    five = [set(x) for x in numbers if segment_filter(set(x))][0]
    return (five - segments).pop()


def find_c_segment(one, f):
    return (one - {f}).pop()


def find_e_segment(eight, a, b, c, d, f, g):
    return (eight - {a, b, c, d, f, g}).pop()


def solve_single_line(numbers):
    one = get_base_number(numbers, 2)
    seven = get_base_number(numbers, 3)
    four = get_base_number(numbers, 4)
    eight = get_base_number(numbers, 7)

    a = find_top_segment(seven, one)
    g = find_bottom_segment(numbers, seven, four)
    d = find_middle_segment(numbers, eight, four, one)
    b = find_b_segment(numbers, seven, d, g)
    f = find_f_segment(numbers, a, g, d, b)
    c = find_c_segment(one, f)
    e = find_e_segment(eight, a, b, c, d, f, g)

    loc = locals()
    letter_mapping = dict((k, loc[k]) for k in "abcdefg")

    def map_comb_to_letters(comb):
        return str_hash(''.join([letter_mapping[x] for x in comb]))

    mapping = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bdcf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    return dict((map_comb_to_letters(k), v) for (k, v) in mapping.items())


def main():
    ans = 0

    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip().split(" | ")
            numbers = line[0].split()
            output = line[1].split()
            mapping = solve_single_line(numbers)
            nums = [mapping[str_hash(x)] for x in output]
            ans += int(''.join(map(str, nums)))
    print(ans)


if __name__ == '__main__':
    main()

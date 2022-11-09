from functools import cache

nums = []


@cache
def move_cost(n):
    return int(n * (n + 1) / 2)


@cache
def calc_cost(align_pos):
    return sum(abs(align_pos - x) for x in nums)


def ternary_search(f, l, r):
    while r - l > 0.1:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        if f(m1) > f(m2):
            l = m1
        else:
            r = m2
    return int(r)


def main():
    global nums
    with open("input.txt") as inp:
        nums = list(map(int, inp.readline().strip().split(",")))

    pos = ternary_search(calc_cost, min(nums), max(nums))
    print(calc_cost(pos))


if __name__ == '__main__':
    main()

from functools import cache


@cache
def count_recursive(num, days_left):
    if num >= days_left:
        return 1

    if num == 0:
        return count_recursive(6, days_left-1) + count_recursive(8, days_left-1)
    else:
        return count_recursive(0, days_left - num)


def main():
    days = 256
    total = 0
    with open("input.txt") as inp:
        nums = list(map(int, inp.readline().strip().split(",")))
        for num in nums:
            total += count_recursive(num, days)
    print(total)


if __name__ == '__main__':
    main()

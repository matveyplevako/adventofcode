def get_lists(nums):
    seq = []
    for i in range(len(nums) - 1):
        seq.append(nums[i + 1] - nums[i])
    lists = [seq]
    if not all([x == 0 for x in seq]):
        lists.extend(get_lists(seq))
    return lists


def calc_next_num(nums):
    lists = get_lists(nums)
    lists.insert(0, nums)
    return sum(x[-1] for x in lists)


def main():
    ans = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            nums = list(map(int, line.split()))
            ans += calc_next_num(nums)
    print(ans)


if __name__ == '__main__':
    main()

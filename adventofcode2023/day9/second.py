from functools import reduce
from operator import sub


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
    lists = lists[::-1]
    ans = 0
    for i in range(1, len(lists)):
        ans = lists[i][0] - ans
    return ans


def main():
    ans = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            nums = list(map(int, line.split()))
            ans += calc_next_num(nums)
    print(ans)


if __name__ == '__main__':
    main()

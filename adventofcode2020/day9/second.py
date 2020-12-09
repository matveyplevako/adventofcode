from collections import defaultdict

acc = 0
invalid = 1504371145

def check_if_sum(last_n, num):
    need_to_add = set()
    for x in last_n:
        if x in need_to_add:
            return True
        need_to_add.add(num - x)
    print(num)


with open("input.txt") as inp:
    nums = list(map(lambda x: int(x.strip()), inp.readlines()))
    for i in range(len(nums)):
        for j in range(i + 2, len(nums) + 1):
            if sum(nums[i:j]) == invalid:
                print(i, j, min(nums[i:j]) + max(nums[i:j]))



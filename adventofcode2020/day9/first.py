from collections import defaultdict

acc = 0
last_of = 25

def check_if_sum(last_n, num):
    need_to_add = set()
    for x in last_n:
        if x in need_to_add:
            return True
        need_to_add.add(num - x)
    print(num)


with open("input.txt") as inp:
    nums = list(map(lambda x: int(x.strip()), inp.readlines()))
    for i in range(last_of, len(nums)):
        last_n = nums[i-last_of:i]
        check_if_sum(last_n, nums[i])


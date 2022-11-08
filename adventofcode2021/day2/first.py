depth = 0
horizontal = 0

mapping = {
    "forward": lambda d, h, n: (d, h + n),
    "down": lambda d, h, n: (d + n, h),
    "up": lambda d, h, n: (d - n, h),
}

with open("input.txt") as inp:
    for instruction in inp.readlines():
        action, num = instruction.split()
        depth, horizontal = mapping[action](depth, horizontal, int(num))
    print(depth * horizontal)

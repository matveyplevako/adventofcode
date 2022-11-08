depth = 0
horizontal = 0
aim = 0

mapping = {
    "forward": lambda d, h, a, n: (d + a * n, h + n, a),
    "down": lambda d, h, a, n: (d, h, a + n),
    "up": lambda d, h, a, n: (d, h, a - n),
}

with open("input.txt") as inp:
    for instruction in inp.readlines():
        action, num = instruction.split()
        depth, horizontal, aim = mapping[action](depth, horizontal, aim, int(num))
    print(depth * horizontal)

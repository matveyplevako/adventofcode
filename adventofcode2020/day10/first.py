from collections import defaultdict


with open("input.txt") as inp:
    adapters = sorted(list(map(lambda x: int(x.strip()), inp.readlines())))
    phone_joltage = max(adapters) + 3
    adapters += [phone_joltage]
    last_adapt = 0
    diffs = defaultdict(int)
    for adapter in adapters:
        diff = adapter - last_adapt
        last_adapt = adapter
        diffs[diff] += 1

print(diffs[1] * diffs[3])


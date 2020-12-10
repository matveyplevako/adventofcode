from collections import defaultdict


with open("input.txt") as inp:
    adapters = sorted(list(map(lambda x: int(x.strip()), inp.readlines())))
    phone_joltage = max(adapters) + 3
    adapters = adapters
    arangemets = defaultdict(int)
    arangemets[0] = 1

    for adapter in adapters:
        for i in range(3):
            if adapter-i-1 in arangemets:
                arangemets[adapter] += arangemets[adapter-i-1]


print(arangemets[max(adapters)])


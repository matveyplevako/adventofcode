ans = 0

with open("input.txt") as inp:
    signals = inp.readlines()
    previous = sum(map(int, signals[:3]))
    for i in range(len(signals)):
        current = sum(map(int, signals[i:i+3]))
        if current > previous:
            ans += 1
        previous = current
    print(ans)

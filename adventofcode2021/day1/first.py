ans = 0

with open("input.txt") as inp:
    signals = inp.readlines()
    previous = int(signals[0])
    for signal in signals:
        current = int(signal)
        if current > previous:
            ans += 1
        previous = current
    print(ans)

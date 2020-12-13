with open("input.txt") as inp:
    _ = inp.readline()
    pairs = []
    buses = [int(x) if x != "x" else x for x in inp.readline().split(",")]
    for ind, bus in enumerate(buses):
        if bus != "x":
            pairs.append([bus - ind, bus])
    
    # Chinese Remainder Theorem.
    val = 1
    for x, y in pairs:
        val *= y
    total = 0
    for x, y in pairs:
        total = (total + x * val // y * pow(val // y, y - 2, y)) % val

    print(total)


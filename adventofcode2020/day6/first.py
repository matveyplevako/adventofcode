count = 0

with open("input.txt") as inp:
    buffer = set()
    lines = inp.readlines() + [""]
    for ind, line in enumerate(lines):
        line = line.strip()
        if line:
            [buffer.add(x) for x in line]
        else:
            count += len(buffer)
            buffer = set()

print(count)

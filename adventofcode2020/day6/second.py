count = 0

with open("input.txt") as inp:
    buffer = set()
    lines = inp.readlines() + [""]
    for ind, line in enumerate(lines):
        line = line.strip()
        if line:
            if ind == 0 or lines[ind - 1] == "\n":
                [buffer.add(x) for x in line]
            else:
                [buffer.remove(x) for x in buffer.copy() if x not in line]
        else:
            count += len(buffer)
            buffer = set()

print(count)

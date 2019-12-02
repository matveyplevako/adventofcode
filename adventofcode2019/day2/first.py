with open("input.txt") as inp:
    text = inp.read().split(",")
    opcodes = list(map(int, text))

opcodes[1] = 12
opcodes[2] = 2

for i in range(0, len(opcodes), 4):
    op = opcodes[i]
    if op == 99:
        break
    first = opcodes[i+1]
    second = opcodes[i+2]
    result = opcodes[i+3]

    if op == 1:
        opcodes[result] = opcodes[first] + opcodes[second]

    if op == 2:
        opcodes[result] = opcodes[first] * opcodes[second]


with open("out1.txt", "w") as out:
    out.write(str(opcodes[0]) + '\n')

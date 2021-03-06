with open("input.txt") as inp:
    text = inp.read().split(",")
    opcodes = text

position = 0

while position < len(opcodes):
    op = opcodes[position]

    if len(op) > 2:
        C = int(op[-3])
    else:
        C = 0

    if len(op) > 3:
        B = int(op[-4])
    else:
        B = 0

    op = int(op[-2:])

    if op == 99:
        break

    first = int(opcodes[position + 1])

    if op == 3:
        n = input('waiting for input:\n')
        opcodes[first] = n
        position += 2
    elif op == 4:
        if C == 0:
            print(opcodes[first])
        else:
            print(first)
        position += 2
    else:
        if C == 0:
            first = int(opcodes[first])

        second = int(opcodes[position + 2])
        if B == 0:
            second = int(opcodes[second])

        result = int(opcodes[position + 3])

        if op == 1:
            opcodes[result] = str(first + second)

        if op == 2:
            opcodes[result] = str(first * second)

        if op == 7:
            opcodes[result] = '1' if first < second else '0'
        if op == 8:
            opcodes[result] = '1' if first == second else '0'

        position += 4

        if op == 5:
            if first:
                position = second
            else:
                position -= 1
        if op == 6:
            if not first:
                position = second
            else:
                position -= 1


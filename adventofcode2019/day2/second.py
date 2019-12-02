with open("input.txt") as inp:
    text = inp.read().split(",")
    nums = list(map(int, text))

for noun in range(100):
    for verb in range(100):
        opcodes = nums.copy()
        for i in range(0, len(opcodes), 4):

            opcodes[1] = noun
            opcodes[2] = verb

            op = opcodes[i]
            if op == 99:
                break
            first = opcodes[i + 1]
            second = opcodes[i + 2]
            result = opcodes[i + 3]

            if op == 1:
                opcodes[result] = opcodes[first] + opcodes[second]

            if op == 2:
                opcodes[result] = opcodes[first] * opcodes[second]
        if opcodes[0] == 19690720:
            with open("out2.txt", "w") as out:
                out.write(str(100 * noun + verb) + '\n')

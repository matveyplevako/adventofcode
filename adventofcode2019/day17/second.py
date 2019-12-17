from collections import defaultdict

with open("input.txt") as inp:
    text = dict((ind, elem) for ind, elem in enumerate(inp.read().split(",")))
    opcodes = defaultdict(lambda: '0', text)
    opcodes[0] = '2'

grid = defaultdict(lambda: defaultdict(int))


def explore_map(gen):
    i, j = 0, 0
    while True:
        char = int(next(gen))
        print(chr(char), end='')
        if char != 10:
            # if char in
            grid[i][j] = char
            j += 1
        else:
            i += 1
            j = 0
        if i == 32:
            break


def next_move(inp_tape):
    position = 0
    base = 0
    inp_position = 0

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

        if len(op) > 4:
            A = int(op[-5])
        else:
            A = 0

        op = int(op[-2:])

        if op == 99:
            break

        first = int(opcodes[position + 1])

        if op == 3:
            # n = input('waiting for input:\n')
            n = inp_tape[inp_position]
            inp_position += 1
            if C == 0:
                opcodes[first] = n
            elif C == 2:
                opcodes[first + base] = n
            else:
                raise Exception('cannot assign value to int')
            position += 2
        elif op == 4:
            if C == 0:
                yield opcodes[first]
            elif C == 2:
                yield opcodes[base + first]
            else:
                yield str(first)
            position += 2
        elif op == 9:
            if C == 0:
                base += int(opcodes[first])
            elif C == 2:
                base += int(opcodes[first + base])
            else:
                base += first
            position += 2
        else:
            if C == 0:
                first = int(opcodes[first])

            if C == 2:
                first = int(opcodes[first + base])

            second = int(opcodes[position + 2])
            if B == 0:
                second = int(opcodes[second])

            if B == 2:
                second = int(opcodes[second + base])

            result = int(opcodes[position + 3])
            if A == 2:
                result += base

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


def part2(gen, inp_tape):
    seq = "L,4 L,4 L,10 R,4 R,4 L,4 L,4 R,8 R,10 L,4 L,4 L,10 " \
          "R,4 R,4 L,10 R,10 L,4 L,4 L,10 R,4 R,4 L,10 R,10 R,4 " \
          "L,4 L,4 R,8 R,10 R,4 L,10 R,10 R,4 L,10 R,10 R,4 L,4 L,4 R,8 R,10"
    seq = seq.split()
    names = set(seq)
    names = dict((elem, chr(75 + ind)) for ind, elem in enumerate(names))
    inv_names = {v: k for k, v in names.items()}
    encoded = []
    for item in seq:
        encoded.append(names[item])

    # group together
    A = ''.join(encoded[:4])
    B = ''.join(encoded[4:9])
    C = ''.join(encoded[13:16])

    groups = {A: 'A', B: 'B', C: 'C'}
    inv_groups = {'A': A, 'B': B, 'C': C}

    item = ''
    res = []
    while encoded:
        item += encoded.pop(0)
        if item in groups:
            res.append(groups[item])
            item = ''

    res = ','.join(res)
    part_a = ','.join(map(inv_names.get, inv_groups['A']))
    part_b = ','.join(map(inv_names.get, inv_groups['B']))
    part_c = ','.join(map(inv_names.get, inv_groups['C']))

    input_for_machine = '\n'.join([res, part_a, part_b, part_c, 'n\n'])

    for char in input_for_machine:
        inp_tape.append(ord(char))
    while True:
        try:
            ascii_char = int(next(gen))
            if ascii_char <= 256:
                print(chr(ascii_char), end='')
            else:
                print(ascii_char)
        except StopIteration:
            break
    # print(chr(next(gen)))


def main():
    inp_tape = []
    gen = next_move(inp_tape)
    next(gen)
    explore_map(gen)
    part2(gen, inp_tape)
    # explore_map()


if __name__ == '__main__':
    main()

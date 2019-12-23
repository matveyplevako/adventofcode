from collections import defaultdict

with open("input.txt") as inp:
    text = dict((ind, elem) for ind, elem in enumerate(inp.read().split(",")))
    opcodes_initial = defaultdict(lambda: '0', text)


def next_move(inp_tape):
    position = 0
    inp_position = 0
    base = 0
    opcodes = opcodes_initial.copy()

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
            if inp_position >= len(inp_tape):
                n = '-1'
                yield '-1'
            else:
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


class Computer:

    def __init__(self, num):
        self.inp_tape = [num]
        self.gen = next_move(self.inp_tape)

    def inp(self, elem):
        self.inp_tape.append(elem)

    def next(self):
        return next(self.gen)


def explore():
    computers = [Computer(i) for i in range(50)]
    last_nat_x, last_nat_y, nat_x, nat_y = [None] * 4
    for i in range(400):
        all_empty = True
        for c_i in range(50):
            c = computers[c_i]
            n = c.next()
            if n != '-1':
                all_empty = False
                x, y = c.next(), c.next()
                if int(n) >= 50:
                    nat_x, nat_y = x, y
                else:
                    computers[int(n)].inp(x)
                    computers[int(n)].inp(y)

        if all_empty and i > 0:
            if last_nat_y == nat_y:
                print(nat_y)
                break
            computers[0].inp(nat_x)
            computers[0].inp(nat_y)
            last_nat_x, last_nat_y = nat_x, nat_y


if __name__ == '__main__':
    inp_tape = []
    gen = next_move(inp_tape)
    explore()

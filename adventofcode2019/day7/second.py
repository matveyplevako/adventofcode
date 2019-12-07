from itertools import permutations, cycle
from collections import defaultdict

with open("input.txt") as inp:
    text = inp.read().split(",")


def run(inp, states, ind, next):
    prog_inp = inp[ind]

    while states['pc'] < len(states['opcodes']):
        op = states['opcodes'][states['pc']]
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

        first = int(states['opcodes'][states['pc'] + 1])

        if op == 3:
            n = prog_inp[states['inp_position']]
            states['inp_position'] += 1
            # n = input('waiting for input:\n')
            states['opcodes'][first] = n
            states['pc'] += 2
        elif op == 4:
            if C == 0:
                # print(opcodes[first])
                output = states['opcodes'][first]
                inp[next].append(output)
            else:
                # print(first)
                output = first
                inp[next].append(output)
            states['pc'] += 2
            break
        else:
            if C == 0:
                first = int(states['opcodes'][first])

            second = int(states['opcodes'][states['pc'] + 2])
            if B == 0:
                second = int(states['opcodes'][second])

            result = int(states['opcodes'][states['pc'] + 3])

            if op == 1:
                states['opcodes'][result] = str(first + second)

            if op == 2:
                states['opcodes'][result] = str(first * second)

            if op == 7:
                states['opcodes'][result] = '1' if first < second else '0'
            if op == 8:
                states['opcodes'][result] = '1' if first == second else '0'

            states['pc'] += 4

            if op == 5:
                if first:
                    states['pc'] = second
                else:
                    states['pc'] -= 1
            if op == 6:
                if not first:
                    states['pc'] = second
                else:
                    states['pc'] -= 1


def main():
    possible = [5, 6, 7, 8, 9]
    max_thruster = -1

    for comb in permutations(possible):
        inp = defaultdict(list)
        inp[0].append(0)
        finished = set()
        ind = 0
        states = defaultdict(lambda: {"opcodes": text.copy(), "pc": 0, "inp_position": 0})
        for phase in cycle(comb):
            if ind < 5:
                inp[ind].insert(0, phase)

            if states[ind % 5]['opcodes'][states[ind % 5]['pc']] == '99':
                finished.add(ind % 5)
            else:
                run(inp, states[ind % 5], ind % 5, (ind + 1) % 5)

            if len(finished) == 5:
                max_thruster = max(max_thruster, max(inp[0], key=int), key=int)
                break

            ind += 1

    print(max_thruster)

    with open("out2.txt", "w") as out:
        out.write(str(max_thruster) + '\n')


if __name__ == '__main__':
    main()

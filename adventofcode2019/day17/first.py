from collections import defaultdict

with open("input.txt") as inp:
    text = dict((ind, elem) for ind, elem in enumerate(inp.read().split(",")))
    opcodes = defaultdict(lambda: '0', text)

grid = defaultdict(lambda: defaultdict(int))


def explore_map(gen):
    alignment = 0
    try:
        i, j = 0, 0
        while True:
            char = int(next(gen))
            if char != 10:
                if char == 35 and i > 1 and j > 0:
                    intersect = {grid[i - 2][j], grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1]}
                    if intersect == {35}:
                        alignment += (i - 1) * j
                grid[i][j] = char
                j += 1
            else:
                i += 1
                j = 0

            print(chr(char), end='')
    except StopIteration:
        return alignment


def next_move():
    position = 0
    base = 0
    move = yield
    move = str(move)

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
            n = move
            if C == 0:
                opcodes[first] = n
            elif C == 2:
                opcodes[first + base] = n
            else:
                raise Exception('cannot assign value to int')
            position += 2
        elif op == 4:
            if C == 0:
                move = yield opcodes[first]
            elif C == 2:
                move = yield opcodes[base + first]
            else:
                move = yield str(first)
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


def main():
    gen = next_move()
    next(gen)
    print(explore_map(gen))


if __name__ == '__main__':
    main()

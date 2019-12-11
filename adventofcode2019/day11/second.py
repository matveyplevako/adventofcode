from collections import defaultdict
import sys

with open("input.txt") as inp:
    text = dict((ind, elem) for ind, elem in enumerate(inp.read().split(",")))
    opcodes = defaultdict(int, text)


def next_move(color):
    position = 0
    base = 0

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
            n = color
            if C == 0:
                opcodes[first] = n
            elif C == 2:
                opcodes[first + base] = n
            else:
                raise Exception('cannot assign value to int')
            position += 2
        elif op == 4:
            if C == 0:
                color = yield opcodes[first]
            elif C == 2:
                color = yield opcodes[base + first]
            else:
                color = yield str(first)
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
    grid = defaultdict(lambda: defaultdict(lambda: '0'))
    gen = next_move('1')
    color = next(gen)
    turn = next(gen)
    x, y, direction = [0] * 3
    min_h, min_w, max_h, max_w = [0] * 4
    while True:
        try:
            grid[x][y] = str(color)
            if turn not in ['0', '1']:
                print(type(turn))
                exit()
            direction = (direction + (1 if turn == '0' else -1)) % 4
            x += 1 if direction == 0 else -1 if direction == 2 else 0
            y += 1 if direction == 3 else -1 if direction == 1 else 0
            min_w = min(min_w, y)
            min_h = min(min_h, x)
            max_w = max(max_w, y)
            max_h = max(max_h, x)
            color = gen.send(grid[x][y])
            turn = next(gen)
        except StopIteration:
            break

    for x in range(max_h, min_h - 1, -1):
        for y in range(min_w - 1, max_w + 2):
            assert type(grid[x][y]) == str
            print('#' if grid[x][y] == '1' else ' ', end=' ')
        print()


if __name__ == '__main__':
    main()

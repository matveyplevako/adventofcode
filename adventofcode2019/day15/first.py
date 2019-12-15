from collections import defaultdict, deque

with open("input.txt") as inp:
    text = dict((ind, elem) for ind, elem in enumerate(inp.read().split(",")))
    opcodes = defaultdict(int, text)

'''
   1N
 3W + 4E
   2S
'''

directions = {1: (1, 0), 2: (-1, 0), 3: (0, -1), 4: (0, 1)}
grid = defaultdict(lambda: defaultdict(lambda: ' '))

max_i, min_i = -1, 100000
max_j, min_j = -1, 100000
oxy_position = None
level = defaultdict(lambda: defaultdict(lambda: 100000))


def explore_map(gen, i=0, j=0, used=None):
    global max_i, min_i, max_j, min_j
    if used is None:
        used = set()

    for d in directions.items():
        direction, (di, dj) = d
        max_i = max(max_i, i + di)
        min_i = min(min_i, i + di)
        max_j = max(max_j, j + dj)
        min_j = min(min_j, j + dj)
        if (i + di, j + dj) in used:
            continue
        result = gen.send(direction)
        if result == '2':
            global oxy_position
            oxy_position = (i + di, j + dj)
            grid[di + i][dj + j] = '+'
            # return i + di, j + dj
        if result != '0':
            used.add((i + di, j + dj))
            level[di + i][dj + j] = min(level[i][j] + 1, level[di + i][dj + j])
            explore_map(gen, di + i, dj + j, used)
            used.remove((i + di, j + dj))
            # step back
            if direction in [1, 3]:
                gen.send(direction + 1)
            else:
                gen.send(direction - 1)
        else:
            grid[di + i][dj + j] = '#'


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


def show_grid():
    grid[0][0] = '@'
    for i in range(min_i - 2, max_i + 2):
        for j in range(min_j - 2, max_j + 2):
            print(grid[i][j], end='')
        print()


def main():
    gen = next_move()
    next(gen)
    level[0][0] = 0
    explore_map(gen)
    print(level[oxy_position[0]][oxy_position[1]])


if __name__ == '__main__':
    main()

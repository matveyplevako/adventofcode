from collections import defaultdict
from time import sleep

SHOW_GAME = False
PLAY = False

with open("input.txt") as inp:
    text = dict((ind, elem) for ind, elem in enumerate(inp.read().split(",")))
    opcodes = defaultdict(int, text)
    opcodes[0] = '2'


def calculate_position(platform_and_ball):
    platform, ball = platform_and_ball
    if SHOW_GAME and not PLAY:
        sleep(0.2)
    if platform < ball:
        return '1'
    elif platform > ball:
        return '-1'
    else:
        return '0'


def next_move(platform_and_ball):
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
            if PLAY:
                assert SHOW_GAME, "You have to turn screen on"
                n = input('waiting for input:\n')
            else:
                n = calculate_position(platform_and_ball)
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


def main():
    grid = defaultdict(lambda: defaultdict(int))
    platform_and_ball = [0, 0]
    gen = next_move(platform_and_ball)
    x_max, y_max = 0, 0
    score = -1
    while True:
        try:
            # x - from left, y - from top
            x = int(next(gen))
            y = int(next(gen))

            x_max = max(x, x_max)
            y_max = max(y, y_max)
            tile = int(next(gen))
            if tile == 3:
                platform_and_ball[0] = x
            if tile == 4:
                platform_and_ball[1] = x
            if x == -1 and y == 0:
                score = tile
                if SHOW_GAME:
                    print('\n\n')
                    print("SCORE:", score)
                    print('\n\n')
                continue
            grid[y][x] = tile

            if SHOW_GAME:
                for i in range(int(y_max) + 2):
                    for j in range(int(x_max) + 2):
                        elem = grid[i][j]
                        if elem == 0:
                            print(' ', end='')
                        elif elem == 1:
                            print('#', end='')
                        elif elem == 2:
                            print('.', end='')
                        elif elem == 3:
                            print('—', end='')
                        else:
                            print('*', end='')
                    print()

        except StopIteration:
            break

    print(score)

if __name__ == '__main__':
    main()

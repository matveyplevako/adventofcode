from copy import deepcopy


def move_east(cave):
    new_cave = deepcopy(cave)
    for i in range(len(cave)):
        for j in range(len(cave[0])):
            if cave[i][j] == '>':
                if j == len(cave[0]) - 1 and cave[i][0] == '.':
                    new_cave[i][j] = '.'
                    new_cave[i][0] = '>'
                elif j < len(cave[0]) - 1 and cave[i][j + 1] == '.':
                    new_cave[i][j] = '.'
                    new_cave[i][j + 1] = '>'
    return new_cave


def move_south(cave):
    new_cave = deepcopy(cave)
    for i in range(len(cave)):
        for j in range(len(cave[0])):
            if cave[i][j] == 'v':
                if i == len(cave) - 1 and cave[0][j] == '.':
                    new_cave[i][j] = '.'
                    new_cave[0][j] = 'v'
                elif i < len(cave) - 1 and cave[i + 1][j] == '.':
                    new_cave[i][j] = '.'
                    new_cave[i + 1][j] = 'v'
    return new_cave


def step(cave):
    cave = move_east(cave)
    cave = move_south(cave)
    return cave


def main():
    with open("input.txt") as inp:
        inp = inp.readlines()
        cave = [['.' for _ in range(len(inp[0].strip()))] for _ in range(len(inp))]
    with open("input.txt") as inp:
        for i, line in enumerate(inp.readlines()):
            for j, s in enumerate(line.strip()):
                cave[i][j] = s
    for i in range(10_000):
        new_cave = step(cave)
        if ''.join([''.join(row) for row in cave]) == ''.join([''.join(row) for row in new_cave]):
            print(i+1)
            break
        cave = new_cave


if __name__ == '__main__':
    main()

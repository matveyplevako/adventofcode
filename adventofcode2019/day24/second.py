from collections import Counter, defaultdict

grid = defaultdict(lambda: defaultdict(lambda: [0] * 5))

with open("input.txt") as inp:
    for ind, inp_line in enumerate(inp.readlines()):
        inp_line = inp_line.strip()
        rep = {'.': 0, '#': 1}
        grid[0][ind] = list(map(rep.get, inp_line))


def neighbors(level, i, j):
    row_range, line_range = None, None
    if (i, j) == (1, 2):
        row_range = range(5)
        line_range = [0]
    elif (i, j) == (3, 2):
        row_range = range(5)
        line_range = [len(grid[0]) - 1]
    elif (i, j) == (2, 1):
        row_range = [0]
        line_range = range(5)
    elif (i, j) == (2, 3):
        row_range = [len(grid[0]) - 1]
        line_range = range(5)
    if row_range and line_range:
        elements = []
        [[elements.append(grid[level + 1][line][row]) for row in row_range] for line in line_range]

        adj = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        elements.extend([grid[level][i + p][j + k] for (p, k) in adj if (i + p != 2 or j + k != 2)])
        return Counter(elements)

    elements = [grid[level][i + adj_i][j + adj_j] for (adj_i, adj_j) in [(1, 0), (-1, 0), (0, 1), (0, -1)] if
                0 <= i + adj_i < len(grid[0]) and 0 <= j + adj_j < len(grid[0][0])]

    if i == 0:
        elements.append(grid[level - 1][1][2])
    if i == len(grid[0]) - 1:
        elements.append(grid[level - 1][3][2])
    if j == 0:
        elements.append(grid[level - 1][2][1])
    if j == len(grid[0][0]) - 1:
        elements.append(grid[level - 1][2][3])

    return Counter(elements)


def grid_print():
    inv_rep = {0: '.', 1: '#'}
    for level in range(-5, 6):
        print(f"level -- {level} --")
        for i in range(len(grid[0])):
            for j in range(len(grid[0][0])):
                if i == 2 == j:
                    print('?', end='')
                else:
                    print(inv_rep[grid[level][i][j]], end='')
            print()


def next_gen(level_range):
    global grid
    bugs = 0
    new_grid = defaultdict(lambda: defaultdict(lambda: [0] * 5))
    for level in range(-level_range, level_range + 1):
        for i in range(len(grid[0])):
            for j in range(len(grid[0][0])):
                if i == 2 == j:
                    continue
                if grid[level][i][j] == 1:
                    if neighbors(level, i, j)[1] == 1:
                        bugs += 1
                        new_grid[level][i][j] = 1
                    else:
                        new_grid[level][i][j] = 0
                else:
                    if 1 <= neighbors(level, i, j)[1] <= 2:
                        bugs += 1
                        new_grid[level][i][j] = 1
                    else:
                        new_grid[level][i][j] = 0
    grid = new_grid
    return bugs


if __name__ == '__main__':
    levels = 200
    bugs = -1
    for i in range(levels):
        bugs = next_gen(i + 1)
    print(bugs)

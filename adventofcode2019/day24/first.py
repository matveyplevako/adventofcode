from collections import Counter
from copy import deepcopy

grid = {}

with open("input.txt") as inp:
    for ind, line in enumerate(inp.readlines()):
        line = line.strip()
        rep = {'.': 0, '#': 1}
        grid[ind] = list(map(rep.get, line))


def grid_hash():
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                res += 2 ** (i * len(grid[0]) + j)
    return res


def neighbors(i, j):
    return Counter([grid[i + adj_i][j + adj_j] for (adj_i, adj_j) in [(1, 0), (-1, 0), (0, 1), (0, -1)] if
                    0 <= i + adj_i < len(grid) and 0 <= j + adj_j < len(grid)])


def grid_print():
    inv_rep = {0: '.', 1: '#'}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(inv_rep[grid[i][j]], end='')
        print()


def next_gen():
    global grid
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] and neighbors(i, j)[1] != 1:
                new_grid[i][j] = 0
            if not grid[i][j] and 1 <= neighbors(i, j)[1] <= 2:
                new_grid[i][j] = 1
    grid = new_grid


if __name__ == '__main__':
    states = set()
    while True:
        h = grid_hash()
        if h in states:
            print(h)
            break
        states.add(h)
        next_gen()

from collections import defaultdict
from heapq import heappop, heappush

pipe_map = defaultdict(lambda: defaultdict(lambda: '.'))
adj_map = defaultdict(lambda: defaultdict(list))
dist_map = defaultdict(lambda: defaultdict(int))


def is_inside_the_loop(i, j):
    c = 0
    for y in range(j, -1, -1):
        # look at map of pipes, if S is |LJS shape, then consider it in count
        if (dist_map[i][y] or pipe_map[i][y] == "S") and pipe_map[i][y] in "|LJS":
            c += 1
    return c % 2 == 1


def main():
    s_i, s_j = 0, 0
    with open("input.txt") as inp:
        for i, row in enumerate(inp.readlines()):
            for j, x in enumerate(row.strip()):
                pipe_map[i][j] = x
                if x == "S":
                    s_i, s_j = i, j

    i_len, j_len = len(pipe_map), len(pipe_map[0])
    for i in range(i_len):
        for j in range(j_len):
            if pipe_map[i][j] in "-J7S" and pipe_map[i][j - 1] in "-LFS":
                adj_map[i][j].append((i, j - 1))
            if pipe_map[i][j] in "-LFS" and pipe_map[i][j + 1] in "-J7S":
                adj_map[i][j].append((i, j + 1))
            if pipe_map[i][j] in "|LJS" and pipe_map[i - 1][j] in "|7FS":
                adj_map[i][j].append((i - 1, j))
            if pipe_map[i][j] in "|7FS" and pipe_map[i + 1][j] in "|LJS":
                adj_map[i][j].append((i + 1, j))

    s = [(0, (s_i, s_j))]
    dist_map[s_i][s_j] = 0
    used = {s[0]}
    m = 0
    while s:
        d, node = heappop(s)
        m = max(m, d)
        used.add(node)
        adj = adj_map[node[0]][node[1]]
        for x in adj:
            if x not in used:
                dist_map[x[0]][x[1]] = dist_map[node[0]][node[1]] + 1
                heappush(s, (dist_map[x[0]][x[1]], x))
    print(m)

    c = 0
    for i in range(i_len):
        for j in range(j_len):
            if pipe_map[i][j] == "S":
                print("S", end='')
            if dist_map[i][j]:
                print(".", end='')
            elif not dist_map[i][j] and is_inside_the_loop(i, j):
                c += 1
                print('#', end='')
            else:
                print(" ", end='')
        print()
    print(c)


if __name__ == '__main__':
    main()

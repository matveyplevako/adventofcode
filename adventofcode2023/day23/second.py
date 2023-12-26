import sys

island_map = []
max_length = {}

sys.setrecursionlimit(10_000)


def dfs(i, j, path):
    if (i, j) == (0, 1):
        # print(len(path))
        return 1
    if (i, j) in max_length and len(path) <= max_length[i, j]:
        print(max_length[i, j])
        return max_length[i, j]
    if (i, j) in path:
        return None
    path.append((i, j))
    m = None
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if len(island_map) > ni >= 0 and len(island_map[0]) > nj >= 0 and island_map[ni][nj] != "#":
            res = dfs(ni, nj, path.copy())
            if res:
                m = max(res, m) if m is not None else res
    if m:
        max_length[i, j] = m + 1
    else:
        return None
    return max_length[i, j]


def main():
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            island_map.append(list(line))
        res = dfs(len(island_map) - 1, len(island_map[0]) - 2, []) - 1

    print(res)

    # for i in range(len(island_map)):
    #     for j in range(len(island_map[0])):
    #         if (i, j) in max_length:
    #             print(max_length[i, j], end='\t')
    #         else:
    #             print(island_map[i][j], end='\t')
    #     print()


if __name__ == '__main__':
    main()

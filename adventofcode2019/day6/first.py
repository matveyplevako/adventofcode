from collections import defaultdict, deque

grid = defaultdict(set)
with open("input.txt") as inp:
    for line in inp.readlines():
        A, B = line.split(")")
        grid[A].add(B.strip())


def bfs(graph, start):
    total = 0
    v = start
    d = deque()
    d.append(v)
    levels = {v: 0}
    while len(d) != 0:
        v = d.popleft()
        for s_v in graph[v]:
            levels[s_v] = levels[v] + 1
            d.append(s_v)
            total += levels[s_v]

    return total


result = bfs(grid, "COM")
print(result)

with open("out1.txt", "w") as out:
    out.write(str(result) + '\n')

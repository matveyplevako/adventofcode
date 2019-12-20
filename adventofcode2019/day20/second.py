from collections import defaultdict, deque

grid = defaultdict(lambda: defaultdict(str))

with open('input.txt') as inp:
    line_length = -1
    for i, line in enumerate(inp.readlines()):
        for j, char in enumerate(line):
            grid[i][j] = char
        line_length = max(j, line_length)

portals = defaultdict(list)
teleport_to = {}
for i in range(len(grid)):
    for j in range(line_length):
        if grid[i][j] != '.':
            continue
        if grid[i - 1][j].isupper():
            name = grid[i - 2][j] + grid[i - 1][j]
            portals[name].append((i, j))
        elif grid[i + 1][j].isupper():
            name = grid[i + 1][j] + grid[i + 2][j]
            portals[name].append((i, j))
        elif grid[i][j - 1].isupper():
            name = grid[i][j - 2] + grid[i][j - 1]
            portals[name].append((i, j))
        elif grid[i][j + 1].isupper():
            name = grid[i][j + 1] + grid[i][j + 2]
            portals[name].append((i, j))


def is_inner(i, j):
    if i == 2:
        return False
    if i == len(grid) - 3:
        return False
    if j == line_length - 3:
        return False
    if j == 2:
        return False
    return True


for key, value in portals.items():
    if key not in ["AA", "ZZ"]:
        a, b = value
        teleport_to[a] = b
        teleport_to[b] = a

start = portals["AA"][0]
end = portals["ZZ"][0]


def dijkstra():
    queue = deque()
    v = start[0], start[1], 0
    queue.append(v)
    used = set()
    dist = {v: 0}
    while len(queue) != 0:
        v = queue.popleft()
        p_level = v[-1]
        if (v[0], v[1]) == end and p_level == 0:
            return dist
        for adj in [(1, 0), (-1, 0), (0, 1), (0, -1), None]:
            if adj is None:
                v_is_inner = is_inner(v[0], v[1])
                if v[:-1] in teleport_to and (v_is_inner or p_level != 0):
                    adj_i, adj_j = teleport_to[v[:-1]]
                    p_level += 1 if v_is_inner else -1
                else:
                    continue
            else:
                adj_i = v[0] + adj[0]
                adj_j = v[1] + adj[1]
            if grid[adj_i][adj_j] != '.':
                continue
            p = (adj_i, adj_j, p_level)
            adj_dist = dist[v] + 1
            if p in teleport_to and teleport_to[p] in dist:
                adj_dist = min(dist[teleport_to[p]] + 1, adj_dist)
            if p not in used:
                queue.append(p)
            dist[p] = adj_dist
            used.add(p)

    return dist


distances = dijkstra()
print(distances[(end[0], end[1], 0)])

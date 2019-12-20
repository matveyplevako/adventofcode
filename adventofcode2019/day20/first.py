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

for key, value in portals.items():
    if key not in ["AA", "ZZ"]:
        a, b = value
        teleport_to[a] = b
        teleport_to[b] = a

start = portals["AA"][0]
end = portals["ZZ"][0]


def dijkstra():
    queue = deque()
    queue.append(start)
    used = set()
    dist = {start: 0}
    while len(queue) != 0:
        v = queue.popleft()
        for adj in [(1, 0), (-1, 0), (0, 1), (0, -1), None]:
            if adj is None and v in teleport_to:
                if v in teleport_to:
                    adj_i, adj_j = teleport_to[v]
                else:
                    continue
            else:
                adj_i = v[0] + adj[0]
                adj_j = v[1] + adj[1]
            if grid[adj_i][adj_j] != '.':
                continue
            p = (adj_i, adj_j)
            adj_dist = dist[v] + 1
            if p in teleport_to and teleport_to[p] in dist:
                adj_dist = min(dist[teleport_to[p]] + 1, adj_dist)
            if p not in used:
                queue.append(p)
            dist[p] = adj_dist
            used.add(p)

    return dist


distances = dijkstra()
print(distances[end])

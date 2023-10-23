from collections import defaultdict
import heapq

cave_map = defaultdict(lambda: defaultdict(lambda: 9999999))
adjust = ((0, -1), (0, 1), (1, 0), (-1, 0))


def bfs(cave_length):
    q = []
    heapq.heappush(q, (0, (0, 0)))
    visited = set()
    while q:
        cost, v = heapq.heappop(q)
        if v in visited:
            continue
        visited.add(v)
        if v[0] == cave_length - 1 and v[1] == cave_length - 1:
            return cost
        for adj in adjust:
            new_pos = (v[0] + adj[0], v[1] + adj[1])
            new_cost = cost + cave_map[new_pos[0]][new_pos[1]]
            heapq.heappush(q, (new_cost, new_pos))


def main():
    with open("input.txt") as inp:
        for i, line in enumerate(inp.readlines()):
            line = line.strip()
            cave_length = len(line)
            for j in range(len(line)):
                cave_map[i][j] = int(line[j])

    cost = bfs(cave_length)
    print(cost)


if __name__ == '__main__':
    main()

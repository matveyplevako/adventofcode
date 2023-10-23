from collections import defaultdict
import heapq

cave_map = defaultdict(lambda: defaultdict(lambda: 9999999))
adjust = ((0, -1), (0, 1), (1, 0), (-1, 0))


def get_risk(pos, cave_length):
    i, j = pos
    initial_i = i % cave_length
    initial_j = j % cave_length
    risk = cave_map[initial_i][initial_j] + (i // cave_length + j // cave_length)
    return (risk - 1) % 9 + 1


def bfs(cave_length):
    q = []
    heapq.heappush(q, (0, (0, 0)))
    visited = set()
    while q:
        cost, v = heapq.heappop(q)
        if v in visited:
            continue
        visited.add(v)
        if v[0] == cave_length * 5 - 1 and v[1] == cave_length * 5 - 1:
            return cost
        for adj in adjust:
            new_i = v[0] + adj[0]
            new_j = v[1] + adj[1]
            new_pos = (new_i, new_j)
            if new_i < 0 or new_j < 0 or new_i >= cave_length * 5 or new_j >= cave_length * 5:
                continue
            new_cost = cost + get_risk(new_pos, cave_length)
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

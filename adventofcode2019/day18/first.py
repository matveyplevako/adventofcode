import collections

with open("input.txt") as f:
    grid = [l.rstrip('\n') for l in f]


def reachable_keys(start, have_keys):
    bfs = collections.deque([start])
    distance = {start: 0}
    keys = {}
    while bfs:
        h = bfs.popleft()
        for pt in [
            (h[0] + 1, h[1]),
            (h[0] - 1, h[1]),
            (h[0], h[1] + 1),
            (h[0], h[1] - 1),
        ]:
            if not (0 <= pt[0] < len(grid) and 0 <= pt[1] < len(grid[0])):
                continue
            ch = grid[pt[0]][pt[1]]
            if ch == '#':
                continue
            if pt in distance:
                continue
            distance[pt] = distance[h] + 1
            if 'A' <= ch <= 'Z' and ch.lower() not in have_keys:
                continue
            if 'a' <= ch <= 'z' and ch not in have_keys:
                keys[ch] = distance[pt], pt
            else:
                bfs.append(pt)
    return keys


def reachable4(starts, havekeys):
    keys = {}
    for i, start in enumerate(starts):
        for ch, (dist, pt) in reachable_keys(start, havekeys).items():
            keys[ch] = dist, pt, i
    return keys


seen = {}


def min_path(starts, have_keys):
    hks = ''.join(sorted(have_keys))
    if (starts, hks) in seen:
        return seen[starts, hks]
    if len(seen) % 10 == 0:
        print(hks)
    keys = reachable4(starts, have_keys)
    if len(keys) == 0:
        # done!
        ans = 0
    else:
        poss = []
        for ch, (dist, pt, roi) in keys.items():
            nstarts = tuple(pt if i == roi else p for i, p in enumerate(starts))
            poss.append(dist + min_path(nstarts, have_keys + ch))
        ans = min(poss)
    seen[starts, hks] = ans
    return ans


starts = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            starts = ((i, j),)
            break

print(min_path(starts, ''))

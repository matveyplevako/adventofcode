from dataclasses import dataclass, field
from heapq import heappop, heappush


@dataclass(order=True)
class CaveState:
    cost: int
    dist: int = field(compare=False)
    pos: dict = field(compare=False)


move_cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

letter_column = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9,
}


def solved(cave):
    correct = {
        (2, 3): 'A',
        (3, 3): 'A',
        (2, 5): 'B',
        (3, 5): 'B',
        (2, 7): 'C',
        (3, 7): 'C',
        (2, 9): 'D',
        (3, 9): 'D',
    }
    return cave == correct


def get_hash(cave):
    cave_hash = ''
    for pos, s in sorted(cave.items()):
        cave_hash += s + str(pos)
    return cave_hash


def brute_force(cave: dict):
    stack = []
    used = set()
    heappush(stack, CaveState(0, 0, cave.copy()))
    mm = 0
    while True:
        cave_state = heappop(stack)
        cost, d, cave = cave_state.cost, cave_state.dist, cave_state.pos
        if cost - mm > 1000:
            print(cost)
            draw_cave(cave)
            mm = cost
        if solved(cave):
            return cost, cave
        cave_hash = get_hash(cave)
        if cave_hash in used:
            continue
        used.add(cave_hash)
        for pos in cave:
            for (ni, nj) in [
                (1, 1),
                (1, 2),
                (1, 4),
                (1, 6),
                (1, 8),
                (1, 10),
                (1, 11),
                (2, 3),
                (2, 5),
                (2, 7),
                (2, 9),
                (3, 3),
                (3, 5),
                (3, 7),
                (3, 9),
                (4, 3),
                (4, 5),
                (4, 7),
                (4, 9),
                (5, 3),
                (5, 5),
                (5, 7),
                (5, 9),
            ]:
                if (ni, nj) not in cave:
                    if pos[0] == 1:
                        if nj != letter_column[cave[pos]]:
                            continue
                    if (ni == 1 and pos[0] not in [2, 3, 4, 5]) or (ni in [2, 3, 4, 5] and pos[0] != 1):
                        continue
                    if pos[0] != 1:
                        if any([(si, pos[1]) in cave for si in range(1, pos[0])]):
                            continue
                    if ni != 1:
                        for i in range(2, 6):
                            if (i, nj) not in cave:
                                ni = i
                                break
                    if any([(1, sj) in cave and (1, sj) != pos for sj in range(min(nj, pos[1]), max(nj, pos[1]) + 1)]):
                        continue
                    dist = abs(ni - pos[0]) + abs(nj - pos[1])
                    c = move_cost[cave[pos]] * dist
                    new_cave = cave.copy()
                    del new_cave[pos]
                    new_cave[(ni, nj)] = cave[pos]
                    heappush(stack, CaveState(cost + c, d + dist, new_cave))


def draw_cave(cave):
    print('#############')
    for i in range(1, 7):
        print('#', end='')
        for j in range(1, 12):
            if (i, j) in cave:
                print(cave[(i, j)], end='')
            else:
                if i == 1 or (j in [3, 5, 7, 9] and i < 4):
                    print('.', end='')
                else:
                    print('#', end='')
        print('#')


def main():
    cave = {}
    with open("input.txt") as inp:
        for i, line in enumerate(inp.readlines()):
            for j, s in enumerate(line):
                if s.isalpha():
                    cave[(i, j)] = s

    # draw_cave(cave)
    print(brute_force(cave))
    # test()


if __name__ == '__main__':
    main()

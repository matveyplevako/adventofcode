def move_north(cave_map, i, j):
    if i > 0 and cave_map[i - 1][j] == ".":
        cave_map[i][j] = "."
        cave_map[i - 1][j] = "O"
        if i > 1 and cave_map[i - 2][j] == ".":
            return move_north(cave_map, i - 1, j)
    return cave_map


def move_west(cave_map, i, j):
    if j > 0 and cave_map[i][j - 1] == ".":
        cave_map[i][j] = "."
        cave_map[i][j - 1] = "O"
        if j > 1 and cave_map[i][j - 2] == ".":
            return move_west(cave_map, i, j - 1)
    return cave_map


def move_south(cave_map, i, j):
    if i < len(cave_map) - 1 and cave_map[i + 1][j] == ".":
        cave_map[i][j] = "."
        cave_map[i + 1][j] = "O"
        if i < len(cave_map) - 2 and cave_map[i + 2][j] == ".":
            return move_south(cave_map, i + 1, j)
    return cave_map


def move_east(cave_map, i, j):
    if j < len(cave_map[0]) - 1 and cave_map[i][j + 1] == ".":
        cave_map[i][j] = "."
        cave_map[i][j + 1] = "O"
        if j < len(cave_map[0]) - 2 and cave_map[i][j + 2] == ".":
            return move_east(cave_map, i, j + 1)
    return cave_map


def move_1(direction, cave_map):
    for i in range(len(cave_map)):
        for j in range(len(cave_map[0])):
            if cave_map[i][j] == "O":
                cave_map = direction(cave_map, i, j)
    return cave_map


def move_2(direction, cave_map):
    for i in range(len(cave_map) - 1, -1, -1):
        for j in range(len(cave_map[0]) - 1, -1, -1):
            if cave_map[i][j] == "O":
                cave_map = direction(cave_map, i, j)
    return cave_map


def get_cache(cave_map):
    return ''.join(''.join(x) for x in cave_map)


def get_ans(cave_map):
    ans = 0
    for i in range(len(cave_map)):
        ans += cave_map[::-1][i].count("O") * (i + 1)
    return ans


def find_repeat(seq):
    for i in range(len(seq)):
        for j in range(i + 3, len(seq)):
            diff = (j - i + 1)
            if seq[i:j + 1] == seq[i + diff:j + diff + 1]:
                return i, seq[i:j + 1]


def main():
    cave_map = []
    seq = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            cave_map.append(list(line.strip()))

    while True:
        cave_map = move_1(move_north, cave_map)
        cave_map = move_1(move_west, cave_map)
        cave_map = move_2(move_south, cave_map)
        cave_map = move_2(move_east, cave_map)
        seq.append(get_ans(cave_map))
        if find_repeat(seq):
            break
    i, seq = find_repeat(seq)
    s = 1000000000
    print(seq[(s - i - 1) % len(seq)])


if __name__ == '__main__':
    main()

def move_north(cave_map, i, j):
    if i > 0 and cave_map[i - 1][j] == ".":
        cave_map[i][j] = "."
        cave_map[i - 1][j] = "O"
        if i > 1 and cave_map[i - 2][j] == ".":
            return move_north(cave_map, i - 1, j)
    return cave_map


def main():
    cave_map = []
    ans = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            cave_map.append(list(line.strip()))
    for i in range(len(cave_map)):
        for j in range(len(cave_map[0])):
            if cave_map[i][j] == "O":
                cave_map = move_north(cave_map, i, j)

    for i in range(len(cave_map)):
        ans += cave_map[::-1][i].count("O") * (i + 1)
    print(ans)


if __name__ == '__main__':
    main()

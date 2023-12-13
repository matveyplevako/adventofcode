def search(cave_map):
    for pos_j in range(1, len(cave_map[0])):
        dj = min(len(cave_map[0]) - pos_j, pos_j)
        if all(cave_map[i][pos_j - dj:pos_j] == cave_map[i][pos_j:pos_j + dj][::-1] for i in range(len(cave_map))):
            return pos_j
    for pos_i in range(1, len(cave_map)):
        di = min(len(cave_map) - pos_i, pos_i)
        if cave_map[pos_i - di:pos_i] == cave_map[pos_i: pos_i + di][::-1]:
            return 100 * pos_i


def main():
    ans = 0
    with open("input.txt") as inp:
        cave_map = []
        for line in inp.readlines() + [""]:
            if line.strip():
                cave_map.append(line.strip())
            else:
                ans += search(cave_map)
                cave_map = []

    print(ans)


if __name__ == '__main__':
    main()

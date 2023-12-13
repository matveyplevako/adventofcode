def search(cave_map):
    for pos_j in range(1, len(cave_map[0])):
        dj = min(len(cave_map[0]) - pos_j, pos_j)
        diff = 0
        for i in range(len(cave_map)):
            left = cave_map[i][pos_j - dj:pos_j]
            right = cave_map[i][pos_j:pos_j + dj][::-1]
            for (a, b) in zip(left, right):
                if a != b:
                    diff += 1
        if diff == 1:
            return pos_j
    for pos_i in range(1, len(cave_map)):
        di = min(len(cave_map) - pos_i, pos_i)
        diff = 0
        top = cave_map[pos_i - di:pos_i]
        bottom = cave_map[pos_i: pos_i + di][::-1]
        for j in range(len(cave_map[0])):
            for (a, b) in zip([x[j] for x in top], [x[j] for x in bottom]):
                if a != b:
                    diff += 1
        if diff == 1:
            return 100 * pos_i


def main():
    ans = 0
    with open("input.txt") as inp:
        cave_map = []
        for line in inp.readlines() + [""]:
            if line.strip():
                cave_map.append(list(line.strip()))
            else:
                ans += search(cave_map)
                cave_map = []
    print(ans)


if __name__ == '__main__':
    main()

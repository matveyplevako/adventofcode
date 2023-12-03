from collections import defaultdict

engine = defaultdict(lambda: defaultdict(str))


def get_number(i, j):
    num = engine[i][j]
    if engine[i][j + 1].isdigit():
        num += engine[i][j + 1]
        if engine[i][j + 2].isdigit():
            num += engine[i][j + 2]
    return num


def is_adjust(i, j, num):
    for di in range(-1, 2):
        for dj in range(-1, len(num) + 1):
            if engine[i + di][j + dj] and not engine[i + di][j + dj].isdigit() and engine[i + di][j + dj] != '.':
                return True


def main():
    with open("input.txt") as inp:
        for i, row in enumerate(inp.readlines()):
            for j, x in enumerate(row.strip()):
                engine[i][j] = x

    nums = list()
    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if engine[i][j].isdigit() and not engine[i][j - 1].isdigit():
                num = get_number(i, j)
                if is_adjust(i, j, num):
                    nums.append(num)

    print(sum(map(int, nums)))


if __name__ == '__main__':
    main()

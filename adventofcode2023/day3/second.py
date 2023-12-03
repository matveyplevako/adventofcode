from collections import defaultdict

engine = defaultdict(lambda: defaultdict(str))


def get_number(i, j):
    num = ""
    if engine[i][j - 1].isdigit():
        if engine[i][j - 2].isdigit():
            num += engine[i][j - 2]
        num += engine[i][j - 1]
    num += engine[i][j]
    if engine[i][j + 1].isdigit():
        num += engine[i][j + 1]
        if engine[i][j + 2].isdigit():
            num += engine[i][j + 2]
    return int(num)


def main():
    with open("input.txt") as inp:
        for i, row in enumerate(inp.readlines()):
            for j, x in enumerate(row.strip()):
                engine[i][j] = x

    nums = list()
    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if engine[i][j] == '*':
                adj = set()
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if engine[di + i][dj + j].isdigit():
                            adj.add(get_number(di + i, dj + j))
                if len(adj) == 2:
                    adj = list(adj)
                    nums.append(adj[0] * adj[1])

    print(sum(nums))


if __name__ == '__main__':
    main()

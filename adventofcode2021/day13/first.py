from collections import defaultdict

paper = defaultdict(lambda: defaultdict(int))
instructions = []
dots = set()


def fold(instruction):
    axis = instruction[0]
    mid = instruction[1]
    if axis == "y":
        fold_y(mid)
    else:
        fold_x(mid)


def fold_x(mid):
    max_i = max(paper)
    max_j = max(max(x) for x in paper.values())
    for i in range(max_i + 1):
        for j in range(mid, max_j + 1):
            if paper[i][j] > 0:
                new_j_pos = mid * 2 - j
                paper[i][new_j_pos] += 1
                paper[i][j] = 0


def fold_y(mid):
    max_i = max(paper)
    max_j = max(max(x) for x in paper.values())
    for i in range(mid, max_i + 1):
        for j in range(max_j + 1):
            if paper[i][j] > 0:
                new_i_pos = mid * 2 - i
                paper[new_i_pos][j] = 1
                paper[i][j] = 0


def print_map():
    mnj = min(min(x) for x in paper.values())
    mxj = max(max(x) for x in paper.values())
    for i in range(min(paper), max(paper) + 1):
        for j in range(mnj, mxj + 1):
            if paper[i][j] > 0:
                print("#", end='')
            else:
                print(".", end='')
        print()
    print()


def main():
    with open("input.txt") as inp:
        lines = inp.readlines()
        while lines:
            line = lines.pop(0).strip()
            if not line:
                break
            j, i = map(int, line.split(","))
            paper[i][j] = 1

        for line in lines:
            line = line.strip()
            cord, num = line.lstrip("fold along ").split("=")
            num = int(num)
            instructions.append((cord, num))

        fold(instructions[0])
        print(sum([len([x for x in row.values() if x > 0]) for row in paper.values()]))


if __name__ == '__main__':
    main()

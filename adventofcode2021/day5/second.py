from collections import defaultdict
from operator import add, sub


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x_min = min(x1, x2)
        self.x_max = max(x1, x2)
        self.y_min = min(y1, y2)
        self.y_max = max(y1, y2)

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


def fill_horizontal_vertical_line_in_field(line: Line, field):
    for i in range(line.x_min, line.x_max + 1):
        for j in range(line.y_min, line.y_max + 1):
            field[j][i] += 1


def fill_diagonal_line_in_field(line: Line, field):
    i, j = line.x1, line.y1
    assert line.x_max - line.x_min == line.y_max - line.y_min

    x_op = sub if line.x1 > line.x2 else add
    y_op = sub if line.y1 > line.y2 else add

    for c in range(line.x_max - line.x_min + 1):
        field[y_op(j, c)][x_op(i, c)] += 1


def main():
    field = defaultdict(lambda: defaultdict(int))
    with open("input.txt") as inp:
        for line in inp.readlines():
            a, b = line.strip().split(' -> ')
            x1, y1 = map(int, a.split(','))
            x2, y2 = map(int, b.split(','))
            line = Line(x1, y1, x2, y2)
            if x1 == x2 or y1 == y2:
                fill_horizontal_vertical_line_in_field(line, field)
            else:
                fill_diagonal_line_in_field(line, field)
    ans = 0
    for row in field:
        for col in field[row]:
            if field[row][col] > 1:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()

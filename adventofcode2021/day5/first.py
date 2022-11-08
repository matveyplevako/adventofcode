from collections import defaultdict


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x_min = min(x1, x2)
        self.x_max = max(x1, x2)
        self.y_min = min(y1, y2)
        self.y_max = max(y1, y2)


def fill_horizontal_vertical_line_in_field(line: Line, field):
    for i in range(line.x_min, line.x_max + 1):
        for j in range(line.y_min, line.y_max + 1):
            field[j][i] += 1


def main():
    field = defaultdict(lambda: defaultdict(int))
    with open("input.txt") as inp:
        for line in inp.readlines():
            a, b = line.strip().split(' -> ')
            x1, y1 = map(int, a.split(','))
            x2, y2 = map(int, b.split(','))
            if x1 == x2 or y1 == y2:
                line = Line(x1, y1, x2, y2)
                fill_horizontal_vertical_line_in_field(line, field)

    ans = 0
    for row in field:
        for col in field[row]:
            if field[row][col] > 1:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()

from collections import defaultdict

supported_by = defaultdict(list)
supports = defaultdict(list)


def count_fall(initial_b):
    q = [initial_b]
    fall = set()
    while q:
        b = q.pop(0)
        fall.add(b)
        will_fall = [x for x in supports[b] if len([z for z in supported_by[x] if z not in fall]) < 1]
        for brick in will_fall:
            fall.add(brick)
            q.append(brick)

    return len(fall - {initial_b})


def check_bricks_collide_on_xy(b1, b2):
    x = min(b1[1][0], b2[1][0]) >= max(b1[0][0], b2[0][0])
    y = min(b1[1][1], b2[1][1]) >= max(b1[0][1], b2[0][1])
    return x and y


def main():
    bricks = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            l, r = line.split("~")
            bricks.append((tuple(map(int, l.split(","))), tuple(map(int, r.split(",")))))

    while True:
        q = []
        for x in bricks:
            z = x[0][2]
            bricks_level_1_down = [b for b in bricks if b[1][2] == z - 1]
            if z > 1 and not any([check_bricks_collide_on_xy(x, b) for b in bricks_level_1_down]):
                q.append(((x[0][0], x[0][1], x[0][2] - 1), (x[1][0], x[1][1], x[1][2] - 1)))
            else:
                q.append(x)

        # print(q)
        if q == bricks:
            break
        bricks = q

    for x in bricks:
        for sup in bricks:
            if x[1][2] == sup[0][2] - 1 and check_bricks_collide_on_xy(x, sup):
                supported_by[sup].append(x)
                supports[x].append(sup)

    c = 0
    for b in bricks:
        c += count_fall(b)

    print(c)


if __name__ == '__main__':
    main()

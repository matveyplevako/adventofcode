from collections import defaultdict

supported_by = defaultdict(list)
supports = defaultdict(list)


def check_if_can_be_removed(b):
    if not supports[b]:
        return True
    if all(len(supported_by[x]) > 1 for x in supports[b]):
        return True


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

    # for (key, value) in supports.items():
    #     print(key, value)

    can_be_removed = set()
    for b in bricks:
        if check_if_can_be_removed(b):
            can_be_removed.add(b)

    print(len(can_be_removed))


if __name__ == '__main__':
    main()

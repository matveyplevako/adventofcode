from itertools import combinations


def find_ray_intersection(ray1, ray2):
    x1, y1, _ = ray1[0]
    dx1, dy1, _ = ray1[1]
    x2, y2, _ = ray2[0]
    dx2, dy2, _ = ray2[1]

    # Check if the rays are parallel
    if dx1 * dy2 == dy1 * dx2:
        return None  # No intersection

    # Calculate the t-values for the intersection point
    t1 = (dx2 * (y1 - y2) + dy2 * (x2 - x1)) / (dx1 * dy2 - dy1 * dx2)
    t2 = (dx1 * (y1 - y2) + dy1 * (x2 - x1)) / (dx1 * dy2 - dy1 * dx2)

    # Check if the intersection occurs in front of the starting points
    if t1 < 0 or t2 < 0:
        return None  # No intersection

    # Calculate the coordinates of the intersection point
    x_int = x1 + t1 * dx1
    y_int = y1 + t1 * dy1

    return (x_int, y_int)


def main():
    lines = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            pos, direction = line.split(" @ ")
            pos = list(map(int, pos.split(",")))
            direction = list(map(int, direction.split(",")))
            lines.append((pos, direction))

    left, right = 200000000000000, 400000000000000

    c = 0
    for l1, l2 in combinations(lines, 2):
        res = find_ray_intersection(l1, l2)
        if res:
            x, y = res
            if left <= x <= right and left <= y <= right:
                c += 1
    print(c)


if __name__ == '__main__':
    main()

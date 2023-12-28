from sympy import symbols, solve


def part2(lines):
    x = symbols('x')
    y = symbols('y')
    z = symbols('z')
    vx = symbols('vx')
    vy = symbols('vy')
    vz = symbols('vz')

    x1, v1 = lines[0]
    x2, v2 = lines[1]
    x3, v3 = lines[2]

    x1, y1, z1 = x1
    x2, y2, z2 = x2
    x3, y3, z3 = x3

    vx1, vy1, vz1 = v1
    vx2, vy2, vz2 = v2
    vx3, vy3, vz3 = v3

    sols = solve(
        [(x - x1) * (vy - vy1) - (y - y1) * (vx - vx1), (y - y1) * (vz - vz1) - (z - z1) * (vy - vy1),
         (x - x2) * (vy - vy2) - (y - y2) * (vx - vx2), (y - y2) * (vz - vz2) - (z - z2) * (vy - vy2),
         (x - x3) * (vy - vy3) - (y - y3) * (vx - vx3), (y - y3) * (vz - vz3) - (z - z3) * (vy - vy3)],
        [x, y, z, vx, vy, vz], dict=True)

    for s in sols:
        if s[vx] == int(s[vx]) and s[vy] == int(s[vy]) and s[vz] == int(s[vz]):
            break
    return s[x] + s[y] + s[z]


def main():
    lines = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            pos, direction = line.split(" @ ")
            pos = list(map(int, pos.split(",")))
            direction = list(map(int, direction.split(",")))
            lines.append((pos, direction))

    ans = part2(lines)
    print(ans)


if __name__ == '__main__':
    main()

def get_groups(s):
    counts = []
    c = 0
    for x in s + ".":
        if x == ".":
            if c:
                counts.append(c)
            c = 0
        else:
            c += 1
    return counts


def search(spring: str, rec):
    unknown = spring.count("?")
    c = 0
    for num in range(2 ** unknown):
        s = spring
        for i in range(unknown):
            symbol = [".", "#"][(num >> i) % 2]
            s = s.replace("?", symbol, 1)
        if get_groups(s) == rec:
            c += 1
    return c


def main():
    ans = 0
    with open("input.txt") as inp:
        for row in inp.readlines():
            spring, rec = row.split()
            rec = list(map(int, rec.split(",")))
            ans += search(spring, rec)
    print(ans)


if __name__ == '__main__':
    main()

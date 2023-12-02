def main():
    s = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            game, colors = line.split(":")
            r_max, g_max, b_max = 0, 0, 0
            for b_set in colors.split(', '):
                for b in b_set.split('; '):
                    color = b.split()[-1]
                    value = int(b.split()[0])
                    if color == "red":
                        r_max = max(r_max, value)
                    elif color == "green":
                        g_max = max(g_max, value)
                    else:
                        b_max = max(b_max, value)
            s += r_max * g_max * b_max
    print(s)


if __name__ == '__main__':
    main()

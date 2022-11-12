def main():
    ans = 0

    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip().split(" | ")[1].split()
            for size in [2, 3, 4, 7]:
                ans += len([x for x in line if len(x) == size])
    print(ans)


if __name__ == '__main__':
    main()

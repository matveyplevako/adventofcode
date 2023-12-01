def main():
    s = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            digits = [x for x in line if x.isnumeric()]
            s += int(digits[0] + digits[-1])
    print(s)


if __name__ == '__main__':
    main()

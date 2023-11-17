def main():
    score = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            l, r = line[:len(line) // 2], line[len(line) // 2:]
            common = (set(l) & set(r)).pop()
            if common.islower():
                score += ord(common) - 96
            else:
                score += ord(common) - 38
        print(score)


if __name__ == '__main__':
    main()

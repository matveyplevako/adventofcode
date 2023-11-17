def main():
    score = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            a, b = line.strip().split(',')
            a, b = [list(map(int, x.split('-'))) for x in [a, b]]
            if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
                score += 1
        print(score)


if __name__ == '__main__':
    main()

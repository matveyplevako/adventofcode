def main():
    s = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            card, nums = line.split(": ")
            w, h = nums.split(' | ')
            w = list(map(int, w.split()))
            h = list(map(int, h.split()))
            intersect = set(w) & set(h)
            if intersect:
                s += 2 ** (len(intersect) - 1)
    print(s)


if __name__ == '__main__':
    main()

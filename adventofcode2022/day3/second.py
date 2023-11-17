def main():
    score = 0
    with open("input.txt") as inp:
        inp = inp.read().split('\n')
        for i in range(0, len(inp), 3):
            common = (set(inp[i]) & set(inp[i + 1]) & set(inp[i + 2])).pop()
            if common.islower():
                score += ord(common) - 96
            else:
                score += ord(common) - 38
        print(score)


if __name__ == '__main__':
    main()

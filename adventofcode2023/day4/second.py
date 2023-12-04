from collections import defaultdict

cards = defaultdict(lambda: 0)


def main():
    with open("input.txt") as inp:
        for ind, line in enumerate(inp.readlines()):
            cards[ind + 1] += 1
            card, nums = line.split(": ")
            w, h = nums.split(' | ')
            w = list(map(int, w.split()))
            h = list(map(int, h.split()))
            intersect = set(w) & set(h)
            if intersect:
                for i in range(len(intersect)):
                    cards[ind + i + 2] += (cards[ind + 1])

    print(sum(cards.values()))


if __name__ == '__main__':
    main()

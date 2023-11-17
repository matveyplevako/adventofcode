points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

won_comb = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}


def main():
    score = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            a, b = line.split()
            score += points[b]
            if ord(a) == ord(b) - 23:
                score += 3
            if won_comb[a] == b:
                score += 6
        print(score)


if __name__ == '__main__':
    main()

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

loose_comb = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}


def main():
    score = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            a, b = line.split()
            if b == "X":
                score += points[loose_comb[a]]
            elif b == "Y":
                score += points[chr(ord(a) + 23)]
                score += 3
            else:
                score += points[won_comb[a]]
                score += 6
        print(score)


if __name__ == '__main__':
    main()

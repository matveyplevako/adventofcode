closing_brackets = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_open_brackets(line):
    stack = []
    for char in line:
        if char in "[({<":
            stack.append(char)
        else:
            elem = stack.pop()
            if char != closing_brackets[elem]:
                return []
    return stack


def get_score_filling_brackets(open_brackets):
    score = 0
    for elem in open_brackets[::-1]:
        score = score * 5 + points[closing_brackets[elem]]
    return score


def main():
    scores = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            open_brackets = get_open_brackets(line)
            score = get_score_filling_brackets(open_brackets)
            if score:
                scores.append(score)

    print(sorted(scores)[len(scores) // 2])


if __name__ == '__main__':
    main()

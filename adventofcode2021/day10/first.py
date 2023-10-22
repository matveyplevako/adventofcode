closing_brackets = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def check_if_corrupted(line):
    stack = []
    for char in line:
        if char in "[({<":
            stack.append(char)
        else:
            elem = stack.pop()
            if char != closing_brackets[elem]:
                return points[char]
    return 0


def main():
    ans = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            ans += check_if_corrupted(line)
    print(ans)


if __name__ == '__main__':
    main()

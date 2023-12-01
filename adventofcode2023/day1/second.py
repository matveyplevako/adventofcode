
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    s = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            str_digits = []
            for ind, x in enumerate(line):
                if x.isnumeric():
                    str_digits.append(x)
                else:
                    for dig in digits:
                        if dig in line[ind:ind+len(dig)]:
                            str_digits.append(digits[dig])
            s += int(str_digits[0] + str_digits[-1])

    print(s)


if __name__ == '__main__':
    main()

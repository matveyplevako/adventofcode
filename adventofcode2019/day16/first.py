with open("input.txt") as inp:
    inp_number = list(map(int, inp.readline().strip()))


def pattern(digit_index, pat_index):
    pat_index = (pat_index + 1) % (4 * digit_index)
    if pat_index < digit_index:
        return 0
    elif pat_index < 2 * digit_index:
        return 1
    elif pat_index < 3 * digit_index:
        return 0
    elif pat_index < 4 * digit_index:
        return -1


def main(number):
    for i in range(100):
        print(i)
        new_number = []
        for ind in range(len(number)):
            new_digit = 0
            for index in range(len(number)):
                new_digit += number[index] * pattern(ind + 1, index)
            new_number.append(abs(new_digit) % 10)
        number = new_number
    number = ''.join(map(str, number))
    print(number[:8])


if __name__ == '__main__':
    main(inp_number)

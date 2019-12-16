with open("input.txt") as inp:
    inp_number = 10_000 * list(map(int, inp.readline().strip()))


def main(number):
    number = number[int(''.join(map(str, number))[:7]):]
    for i in range(100):
        rev_partial_sum = [number[-1]]
        for digit in reversed(number[:-1]):
            rev_partial_sum.append(rev_partial_sum[-1] + digit)
        number = [abs(x) % 10 for x in reversed(rev_partial_sum)]
    number = ''.join(map(str, number))
    print(number[:8])


if __name__ == '__main__':
    main(inp_number)

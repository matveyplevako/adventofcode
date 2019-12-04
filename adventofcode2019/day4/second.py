with open("input.txt") as inp:
    start, end = map(int, inp.readline().split("-"))

fit = 0

for i in range(start, end + 1):
    digits = str(i)
    has_same = False
    for digit in digits:
        # all in non decreasing so the same digits will be together
        if digits.count(digit) == 2:
            has_same = True
            break

    if has_same and sorted(digits) == list(digits):
        fit += 1

print(fit)


with open("out2.txt", "w") as out:
    out.write(str(fit) + '\n')

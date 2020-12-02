correct = 0

with open("inp.txt") as inp:
    for line in inp.readlines():
        line = line.strip()
        lines, data = line.split(" ", 1)
        left_b, right_b = map(int, lines.split("-"))
        letter_rule, word = data.split(": ")
        count = word.count(letter_rule)
        if left_b <= count <= right_b:
            correct += 1

print(correct)

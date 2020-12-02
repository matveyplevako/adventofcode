correct = 0

with open("inp.txt") as inp:
    for line in inp.readlines():
        line = line.strip()
        lines, data = line.split(" ", 1)
        left_b, right_b = map(int, lines.split("-"))
        letter_rule, word = data.split(": ")
        text_position = word[right_b - 1] + word[left_b - 1]
        if text_position.count(letter_rule) == 1:
            correct += 1

print(correct)

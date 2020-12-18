def evaluate(expression):
    i = 0
    left_part = expression[i]
    if "(" in left_part:
        expression_in_parentheses = [left_part]
        open_count = left_part.count("(")
        while open_count != 0:
            i += 1
            open_count += expression[i].count("(")
            open_count -= expression[i].count(")")
            expression_in_parentheses.append(expression[i])
        expression_in_parentheses[0] = expression_in_parentheses[0][1:]
        expression_in_parentheses[-1] = expression_in_parentheses[-1][:-1]
        left_part = evaluate(expression_in_parentheses)
    else:
        left_part = int(left_part)
    i += 1
    rez = left_part
    while i < len(expression):
        op = expression[i]
        i += 1
        right_part = expression[i]
        if "(" in right_part:
            open_count = right_part.count("(")
            expression_in_parentheses = [right_part]
            while open_count != 0:
                i += 1
                open_count += expression[i].count("(")
                open_count -= expression[i].count(")")
                expression_in_parentheses.append(expression[i])
            right_part = evaluate(expression_in_parentheses)
        else:
            right_part = int(right_part)
        i += 1
        if op == "+":
            rez += right_part
        else:
            rez *= right_part
    return rez



with open("input.txt") as inp:
    s = 0
    for line in inp.readlines():
        expression = line.strip().split()
        s += evaluate(expression)

print(s)


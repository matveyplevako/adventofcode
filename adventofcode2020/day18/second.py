from collections import defaultdict
from operator import add, mul

cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))


def eval_in_parentheses(expression, i, to_right=True):
    closed_count = expression[i].count(")") if to_right else expression[i].count("(")
    closed_count -= expression[i].count("(") if to_right else expression[i].count(")")
    expression_in_parentheses = [expression[i]]
    while closed_count > 0:
        i = i - 1 if to_right else i + 1
        closed_count -= expression[i].count("(") if to_right else expression[i].count(")")
        closed_count += expression[i].count(")") if to_right else expression[i].count("(")
        expression_in_parentheses.append(expression[i])

    if to_right:
        expression_in_parentheses = expression_in_parentheses[::-1]
    expression_in_parentheses[0] = expression_in_parentheses[0][1:]
    expression_in_parentheses[-1] = expression_in_parentheses[-1][:-1]
    return evaluate(expression_in_parentheses), i, closed_count


def evaluate(expression):
    mult_index = expression.index("*") if "*" in expression else None
    plus_index = expression.index("+") if "+" in expression else None
    while mult_index is not None or plus_index is not None:
        ind = plus_index if plus_index else mult_index
        op = add if plus_index else mul

        left_index = ind - 1
        right_index = ind + 2
        need_left_par = 0
        left_part = expression[ind - 1]
        if ")" in left_part:
            left_part, left_index, need_left_par = eval_in_parentheses(expression, ind - 1)
        if "(" in left_part:
            need_left_par = left_part.count("(")
            left_part = int(left_part[need_left_par:])
        else:
            left_part = int(left_part)

        need_right_par = 0
        right_part = expression[ind + 1]
        if "(" in right_part:
            right_part, right_index, need_right_par = eval_in_parentheses(expression, ind + 1, False)
            right_index += 1
        if ")" in right_part:
            need_right_par = right_part.count(")")
            right_part = int(right_part[:-need_right_par])
        else:
            right_part = int(right_part)

        rez = op(left_part, right_part)

        to_sub = min(need_left_par, need_right_par)
        need_left_par -= to_sub
        need_right_par -= to_sub
        expression[left_index:right_index] = [f"{'(' * need_left_par}{rez}{')' * need_right_par}"]

        mult_index = expression.index("*") if "*" in expression else None
        plus_index = expression.index("+") if "+" in expression else None

    return expression[0]


with open("input.txt") as inp:
    s = 0
    for line in inp.readlines():
        expression = line.strip().split()
        s += int(evaluate(expression))
    print(s)


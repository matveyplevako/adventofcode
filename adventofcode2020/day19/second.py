from collections import defaultdict
import re

rules = defaultdict(list)


def get_regexp(for_rule):
    if for_rule == "8":
        reg_42 = get_regexp('42')
        return f"(({reg_42})+)"
    if for_rule == "11":
        reg_42 = get_regexp('42')
        reg_31 = get_regexp('31')
        repeat = 5
        string = ""
        for i in range(1, repeat+1):
            string += "(" + f"({reg_42})" * i + f"({reg_31})" * i + ")|"
        return string[:-1]

    if for_rule in ["a", "b"]:
        return for_rule
    string = ""
    for sub_rules in rules[for_rule]:
        string += "("
        for sub_rule in sub_rules:
            string += "(" + get_regexp(sub_rule) + ")"
        string += ")|"
    return string[:-1]


with open("input.txt") as inp:
    while True:
        line = inp.readline().strip()
        if line:
            name, valid = line.split(": ")
            for pos in valid.split(" | "):
                pos = pos.strip()
                if pos[0] == '"':
                    rules[name].append(pos.strip('"'))
                else:
                    rules[name].append(pos.split())
        else:
            break

    rules['8'] = list()
    rules['8'].append(['42'])
    rules['8'].append(['42', '8'])

    rules['11'] = list()
    rules['11'].append(['42', '31'])
    rules['11'].append(['42', '11', '31'])

    regexp_string = get_regexp('0')
    regexp = re.compile(regexp_string)

    valid = 0
    for line in inp.readlines():
        line = line.strip()
        if regexp.fullmatch(line):
            valid += 1

    print(valid)


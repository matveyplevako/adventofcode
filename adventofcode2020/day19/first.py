from collections import defaultdict
from itertools import product
import re

rules = defaultdict(list)


def get_regexp(for_rule):
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

    regexp_string = get_regexp('0')
    regexp = re.compile(regexp_string)

    valid = 0
    for line in inp.readlines():
        line = line.strip()
        if regexp.fullmatch(line):
            valid += 1

    print(valid)


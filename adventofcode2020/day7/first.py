from collections import defaultdict

count = 0


rules = defaultdict(list)
reverse_rules = defaultdict(list)


with open("input.txt") as inp:
    lines = inp.readlines()
    for line in lines:
        name, other = line.strip().split(" contain ", 1)
        rule_name = name.replace(" bags", "")
        for bag in other.split(", "):
            amount, name = bag.strip().split(" ", 1)
            name = name.replace(" bag", "").replace(" bags", "").replace(".", "")
            name = name.strip()
            if name[-1] == "s":
                name = name[:-1]
            rules[rule_name].append((name, amount))
            reverse_rules[name].append(rule_name)


def dfs(start, rules):
    visited = set()
    stack = [start]
    while stack:
        rule_name = stack.pop()
        visited.add(rule_name)
        for item in rules[rule_name]:
            if item not in visited:
                stack.append(item)
    return visited

# print(reverse_rules)
visited = dfs("shiny gold", reverse_rules)
print(len(visited) - 1)


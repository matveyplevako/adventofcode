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
    result = 0
    for rule in rules[start]:
        name, amount = rule
        if amount != "no":
            amount = int(amount)
            dfs_res = dfs(name, rules)
            result += amount * dfs_res + amount
        else:
            return 0
    return result


visited = dfs("shiny gold", rules)
print(visited)

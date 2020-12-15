from collections import defaultdict


last_seen = defaultdict(lambda: list())



with open("input.txt") as inp:
    vals = list(map(int, inp.readline().split(",")))
    for ind, val in enumerate(vals):
        last_seen[val].append(ind)
    
    last_seen[0].append(len(vals))
    last_num = 0

    turns = 30000000

    for ind in range(len(vals) + 1, turns):
        if len(last_seen[last_num]) < 2:
            last_seen[0].append(ind)
            last_num = 0
        else:
            diff = last_seen[last_num][-1] - last_seen[last_num][-2]
            last_seen[diff].append(ind)
            last_num = diff


    print(last_num)


from collections import defaultdict

acc = 0

ops = []
visited = set()

with open("input.txt") as inp:
    ops = list(map(lambda x: x.strip(), inp.readlines()))
    ind = 0
    while ind < len(ops):
        if ind in visited:
            break
        visited.add(ind)
        op, num = ops[ind].split()
        num = int(num)
        if op == "jmp":
            ind += num
        else:
            if op == "acc":
                acc += num
            ind += 1
        
print(acc)



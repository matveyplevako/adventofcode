from collections import defaultdict


ops = []


def run_prog(ops):
    ind = 0
    acc = 0
    visited = set()
    while ind < len(ops):
        if ind in visited:
            return False, acc
        visited.add(ind)
        op, num = ops[ind].split()
        num = int(num)
        if op == "jmp":
            ind += num
        else:
            if op == "acc":
                acc += num
            ind += 1

    return True, acc

with open("input.txt") as inp:
    ops = list(map(lambda x: x.strip(), inp.readlines()))
    for ind, op in enumerate(ops.copy()):
        op, val = op.split()
        if op == "jmp":
            ops[ind] = ' '.join(["nop", val])
            terminated, acc = run_prog(ops)
            if terminated:
                print(acc)
            ops[ind] = ' '.join(["jmp", val])
        elif op == "nop":
            ops[ind] = ' '.join(["jmp", val])
            terminated, acc = run_prog(ops)
            if terminated:
                print(acc)
            ops[ind] = ' '.join(["nop", val])



stack1 = list()
stack2 = list()

with open('input.txt') as inp:
    _ = inp.readline()
    line = inp.readline()
    while line:
        stack1.append(int(line))
        line = inp.readline().strip()

    _ = inp.readline()
    for line in inp.readlines():
        stack2.append(int(line))

while stack1 and stack2:
    p1, p2 = stack1.pop(0), stack2.pop(0)
    if p1 > p2:
        stack1.append(p1)
        stack1.append(p2)
    else:
        stack2.append(p2)
        stack2.append(p1)

print(sum([(stack1 + stack2)[::-1][ind] * (ind + 1) for ind in range(len(stack1 + stack2))]))


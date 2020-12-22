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


def play_game(p1_stack, p2_stack):
    prev = set()
    while p1_stack and p2_stack:
        p1_p2_hash = (tuple(p1_stack), tuple(p2_stack))
        # p1_p2_hash = (tuple(p1_stack), tuple(p2_stack))
        if p1_p2_hash in prev:
            return True, False
        prev.add(p1_p2_hash)
        p1, p2 = p1_stack.pop(0), p2_stack.pop(0)
        if len(p1_stack) < p1 or len(p2_stack) < p2:
            s1 = p1 > p2
        else:
            s1, s2 = play_game(p1_stack.copy()[:p1], p2_stack.copy()[:p2])

        if s1:
            p1_stack.append(p1)
            p1_stack.append(p2)
        else:
            p2_stack.append(p2)
            p2_stack.append(p1)

    return p1_stack, p2_stack


stack1, stack2 = play_game(stack1.copy(), stack2.copy())
# print(stack1, stack2)
print(sum([(stack1 + stack2)[::-1][ind] * (ind + 1) for ind in range(len(stack1 + stack2))]))


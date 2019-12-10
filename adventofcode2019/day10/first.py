from collections import defaultdict


def on_the_same_line(A, B, C):
    if not min(A[0], B[0]) <= C[0] <= max(A[0], B[0]) or not min(A[1], B[1]) <= C[1] <= max(A[1], B[1]):
        return False

    return A[1] * (B[0] - C[0]) + B[1] * (C[0] - A[0]) + C[1] * (A[0] - B[0]) == 0


grid = []
asteroids_location = []

with open("input.txt") as inp:
    for ind, line in enumerate(inp.readlines()):
        line = line.strip()
        for sub_ind, char in enumerate(line):
            if char == '#':
                asteroids_location.append((ind, sub_ind))

see = defaultdict(int)

for asteroid in asteroids_location:
    for can_see in asteroids_location:
        if asteroid != can_see:
            if not any(map(lambda sub_ast: on_the_same_line(asteroid, can_see, sub_ast),
                           [sub_ast for sub_ast in asteroids_location if sub_ast not in [asteroid, can_see]])):
                see[asteroid] += 1

max_elem = max(see, key=see.get)
print(max_elem, see[max_elem])
# with open("out1.txt", "w") as out:
#     out.write(str(answer) + '\n')

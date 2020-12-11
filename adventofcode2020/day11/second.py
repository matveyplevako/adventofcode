from collections import defaultdict
from copy import deepcopy

field = []

def tick():
    diffs = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    diffs.remove((0, 0))
    change = 0
    new_field = deepcopy(field)
    for i in range(len(field)):
        for j in range(len(field[0])):
            count = 0
            for diff in diffs:
                direction_di, direction_dj = diff
                mult = 1
                while 0 <= i + direction_di * mult < len(field) and 0 <= j + direction_dj * mult < len(field[0]):
                    if field[i + direction_di * mult][j + direction_dj * mult] == 2:
                        count += 1
                        break
                    if field[i + direction_di * mult][j + direction_dj * mult] == 1:
                        break
                    mult += 1


            if field[i][j] == 1 and count == 0:
                new_field[i][j] = 2
                change += 1
            elif field[i][j] == 2 and count >= 5:
                new_field[i][j] = 1
                change += 1

    
    return new_field, change
                

with open("input.txt") as inp:
    field = []
    for line in inp.readlines():
        field.append(list(map(lambda x: 2 if x == "#" else 1 if x == "L" else 0, line.strip())))



field, change = tick()
while change:
    field, change = tick()


count = 0
for line in field:
    count += line.count(2)

print(count)


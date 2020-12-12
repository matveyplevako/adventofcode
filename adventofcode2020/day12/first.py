E = ( 0,  1) # ->
S = ( 1,  0) # v
W = ( 0, -1) # <-
N = (-1,  0) # ^

directions = [E, S, W, N]
direction_to_index = {"E": 0, "S": 1, "W": 2, "N": 3}


current_direction = 0
i, j = 0, 0


def turn(degrees):
    if degrees == 360:
        return 0
    elif degrees == 270:
        return 3
    elif degrees == 180:
        return 2
    elif degrees == 90:
        return 1
    else:
        print("not supported")

def move(direction, units):
    new_i = i + directions[direction][0] * units
    new_j = j + directions[direction][1] * units
    return new_i, new_j


with open("input.txt") as inp:
    field = []
    for line in inp.readlines():
        line = line.strip()
        action, num = line[0], int(line[1:])
        if action == "R":
            current_direction = (current_direction + turn(num)) % 4
        elif action == "L":
            current_direction = (current_direction - turn(num)) % 4
        elif action == "F":
            i, j = move(current_direction, num)
        else:
            i, j = move(direction_to_index[action], num)

    print(i, j)
    print(abs(i) + abs(j))

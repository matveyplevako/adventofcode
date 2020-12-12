E = ( 0,  1) # ->
S = ( 1,  0) # v
W = ( 0, -1) # <-
N = (-1,  0) # ^

directions = [E, S, W, N]
direction_to_index = {"E": 0, "S": 1, "W": 2, "N": 3}


i, j = 0, 0
waypoint_i, waypoint_j = -1, 10


def turn_right(i, j):
    return (j, -i)

def turn_left(i, j):
    return (-j, i)


def turn(degrees, to_right):
    new_i, new_j = waypoint_i, waypoint_j
    for i in range(degrees // 90):
        if to_right:
            new_i, new_j = turn_right(new_i, new_j)
        else:
            new_i, new_j = turn_left(new_i, new_j)

    return new_i, new_j


def move_waypoint(direction, units):
    new_i = waypoint_i + directions[direction][0] * units
    new_j = waypoint_j + directions[direction][1] * units
    return new_i, new_j


def move(units):
    new_i = i + waypoint_i * units
    new_j = j + waypoint_j * units
    return new_i, new_j


with open("input.txt") as inp:
    field = []
    for line in inp.readlines():
        line = line.strip()
        action, num = line[0], int(line[1:])
        if action == "R":
            waypoint_i, waypoint_j = turn(num, True)
        elif action == "L":
            waypoint_i, waypoint_j = turn(num, False)
        elif action == "F":
            i, j = move(num)
        else:
            waypoint_i, waypoint_j = move_waypoint(
                direction_to_index[action], num)

    print(i, j)
    print(abs(i) + abs(j))

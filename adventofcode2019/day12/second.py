from collections import defaultdict
from itertools import combinations
import math
from copy import deepcopy

moons = {}

with open("input.txt") as inp:
    for ind, line in enumerate(inp.readlines()):
        x, y, z = map(lambda v: int(v[v.index('=') + 1:]), line[1:line.index('>')].split(', '))
        moons[ind] = [x, y, z]


def lcm(x, y):
    return x // math.gcd(x, y) * y


def main():
    initial_moons = deepcopy(moons)
    repeating = dict(((i, -1) for i in range(3)))
    velocity = defaultdict(lambda: defaultdict(int))
    for i in range(1, 1000000):
        for first, second in combinations(moons, 2):
            f = moons[first]
            s = moons[second]
            dvx, dvy, dvz = [1 if f[axis_ind] < s[axis_ind] else -1 if f[axis_ind] > s[axis_ind] else 0 for axis_ind in
                             range(3)]
            velocity[first][0] += dvx
            velocity[first][1] += dvy
            velocity[first][2] += dvz

            velocity[second][0] -= dvx
            velocity[second][1] -= dvy
            velocity[second][2] -= dvz

        for moon in velocity:
            for axis in range(3):
                moons[moon][axis] += velocity[moon][axis]

        for initial_axis in range(3):
            if repeating[initial_axis] != -1 or any([v[initial_axis] != 0 for v in velocity.values()]):
                continue
            for moon_ind in moons:
                if moons[moon_ind][initial_axis] != initial_moons[moon_ind][initial_axis]:
                    break
            else:
                repeating[initial_axis] = i

        if all([v != -1 for v in repeating.values()]):
            break

    axis = list(repeating.values())
    print(lcm(lcm(axis[0], axis[1]), axis[2]))


if __name__ == '__main__':
    main()

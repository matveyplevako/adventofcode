from collections import defaultdict
from itertools import combinations

moons = {}

with open("input.txt") as inp:
    for ind, line in enumerate(inp.readlines()):
        x, y, z = map(lambda v: int(v[v.index('=') + 1:]), line[1:line.index('>')].split(', '))
        moons[ind] = [x, y, z]


def main():
    total_energy = 0
    velocity = defaultdict(lambda: defaultdict(int))
    for i in range(1000):
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

    for ind, moon in moons.items():
        U = sum(map(abs, moon))
        K = sum(map(abs, velocity[ind].values()))
        total_energy += K * U
    print(total_energy)


if __name__ == '__main__':
    main()

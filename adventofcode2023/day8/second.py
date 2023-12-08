from functools import reduce

maps = {}


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def find_z_pos(inst, node):
    ind = 0
    node_path = []
    while True:
        c = inst[ind % (len(inst))]
        ind += 1
        node_path.append((c, node))
        if c == "L":
            node = maps[node][0]
        else:
            node = maps[node][1]
        if node[-1] == "Z":
            break
    return ind


def main():
    nodes = []
    with open("input.txt") as inp:
        inst = inp.readline().strip()
        inp.readline()
        for line in inp.readlines():
            node, path = line.split(' = ')
            maps[node] = path.strip()[1:-1].split(', ')
            if node.endswith("A"):
                nodes.append(node)

    pos = []
    for node in nodes:
        pos.append(find_z_pos(inst, node))

    print(int(reduce(lambda a, b: lcm(a, b), pos)))


if __name__ == '__main__':
    main()

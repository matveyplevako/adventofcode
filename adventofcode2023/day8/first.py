
maps = {}


def main():
    with open("input.txt") as inp:
        inst = inp.readline().strip()
        inp.readline()
        for line in inp.readlines():
            node, path = line.split(' = ')
            maps[node] = path.strip()[1:-1].split(', ')

    node = "AAA"
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
        if node == "ZZZ":
            break
    print(ind)


if __name__ == '__main__':
    main()

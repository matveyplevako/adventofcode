from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt


def find_cardinalities(v, components, to_remove):
    q = [v]
    used = set()
    while q:
        v = q.pop()
        if v in to_remove:
            continue
        if v in used:
            continue
        used.add(v)
        for x in components[v]:
            q.append(x)
    return len(used)


def main():
    components = defaultdict(list)
    G = nx.Graph()
    G.add_nodes_from(components.keys())
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            left, right = line.split(": ")
            [components[left].append(x) for x in right.split()]
            [components[x].append(left) for x in right.split()]
    cord1 = find_cardinalities(list(components.keys())[0], components, ["kbr", "vtt", "tdk"])
    cord2 = len(components.keys()) - cord1
    print(cord1 * cord2)
    return
    # search for 3 vertices that connects 2 graph
    edges = []
    for a in components:
        for b in components[a]:
            edges.append((a, b))
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == '__main__':
    main()

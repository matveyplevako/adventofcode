inverse_grid = {}
with open("input.txt") as inp:
    for line in inp.readlines():
        A, B = line.split(")")
        B = B.strip()
        inverse_grid[B] = A


def bfs(inverse_graph):
    you = "YOU"
    san = "SAN"

    s = inverse_graph[you]
    your_path = []
    while s != "COM":
        s = inverse_graph[s]
        your_path.append(s)

    s = san
    san_path = 0
    while s not in your_path:
        san_path += 1
        s = inverse_graph[s]

    index = your_path.index(s)

    return len(your_path[:index]) + san_path


result = bfs(inverse_grid)
print(result)

with open("out2.txt", "w") as out:
    out.write(str(result) + '\n')

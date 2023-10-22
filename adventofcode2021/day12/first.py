from collections import defaultdict

cave_map = defaultdict(list)


def count_paths(v, visited):
    reached_end = 0
    if v == "end":
        return 1
    if v.islower() and v in visited:
        return 0
    visited.append(v)
    for vs in cave_map[v]:
        reached_end += count_paths(vs, visited.copy())
    return reached_end


def main():
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            a, b = line.split("-")
            cave_map[a].append(b)
            cave_map[b].append(a)

    print(count_paths("start", list()))


if __name__ == '__main__':
    main()

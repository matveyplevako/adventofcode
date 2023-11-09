from itertools import combinations, permutations
from collections import Counter


def get_diff(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return dx, dy, dz


def get_distance(p1, p2):
    dx, dy, dz = get_diff(p1, p2)
    return (dx ** 2 + dy ** 2 + dz ** 2) ** (1 / 2)


def read_chunk(raw_scanner):
    coords = []
    for line in raw_scanner.split('\n')[1:]:
        x, y, z = eval(line)
        coords.append((x, y, z))
    return coords


def get_distances(coords):
    dist = {}
    for index_1, index_2 in combinations(range(len(coords)), 2):
        distance = get_distance(coords[index_1], coords[index_2])
        dist[distance] = (index_1, index_2)
    return dist


def rotation_transforms():
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                yield i, j, k


def transform(p, v, k, d=None):
    p = p[k[0]] * v[0], p[k[1]] * v[1], p[k[2]] * v[2]
    if d:
        return p[0] + d[0], p[1] + d[1], p[2] + d[2]
    return p


def get_offset(d1, c1, d2, c2):
    same_keys = d1.keys() & d2.keys()
    if len(same_keys) < 66:
        return
    diffs = list()
    for key in list(same_keys)[3:]:
        p1, p2 = d1[key]
        p3, p4 = d2[key]
        c11 = c1[p1]
        c12 = c1[p2]
        c21 = c2[p3]
        c22 = c2[p4]
        # print(c21, c22)
        for k in permutations([0, 1, 2]):
            for v in rotation_transforms():
                a = get_diff(c11, transform(c21, v, k)) == get_diff(c12, transform(c22, v, k))
                b = get_diff(c11, transform(c22, v, k)) == get_diff(c12, transform(c21, v, k))
                if a:
                    diffs.append((get_diff(c11, transform(c21, v, k)), v, k))
                if b:
                    diffs.append((get_diff(c11, transform(c22, v, k)), v, k))
    c = Counter(diffs)
    return max(c, key=c.get)


def rec_transform(dists, current, used):
    vectors = set()
    for i in range(len(dists)):
        if i in used or i == current:
            continue
        res = get_offset(dists[current][0], dists[current][1], dists[i][0], dists[i][1])
        if res:
            used.add(i)
            d, v, k = res
            for vect in dists[i][1]:
                vectors.add(transform(vect, v, k, d))
            for vect in rec_transform(dists, i, used):
                vectors.add(transform(vect, v, k, d))
    return vectors


def main():
    coords = []
    with open("input.txt") as inp:
        scanners = inp.read().split('\n\n')
        for raw_scanner in scanners:
            coords.append(read_chunk(raw_scanner))

    dists = []
    for c in coords:
        d = get_distances(c)
        dists.append((d, c))

    vectors = {v for v in dists[0][1]}
    v = rec_transform(dists, 0, {0})
    print(len(v | vectors))


if __name__ == '__main__':
    main()

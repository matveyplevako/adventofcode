from collections import defaultdict
import numpy as np
from operator import mul
from functools import reduce

tiles = {}


def rotate(to_rotate, k):
    return np.rot90(to_rotate, k=k)


def match(array_1, array_2):
    left_right = np.count_nonzero(array_1[:, -1] - array_2[:, 0]) == 0
    right_left = np.count_nonzero(array_1[:, 0] - array_2[:, -1]) == 0
    top_bottom = np.count_nonzero(array_1[0] - array_2[-1]) == 0
    bottom_top = np.count_nonzero(array_1[-1] - array_2[0]) == 0
    # print(*array_1, sep='\n')
    # print('---')
    # print(*array_2, sep='\n')
    # print(left_right, right_left, top_bottom, bottom_top)
    return left_right or right_left or top_bottom or bottom_top


def check_if_match(array_1, array_2):
    # 0 - top
    # 1 - right
    # 2 - bottom
    # 3 - left
    for i in range(4):
        if match(array_1, rotate(array_2, i)):
            return True

    array_2 = np.flipud(array_2)
    for i in range(4):
        if match(array_1, rotate(array_2, i)):
            return True

    return False


with open("input.txt") as inp:
    array = list()
    tile_id = None
    for line in inp.readlines() + ['']:
        if not tile_id:
            tile_id = int(line.split()[1][:-1])
        else:
            line = line.strip()
            if line:
                array.append([1 if x == "#" else 0 for x in line])
            else:
                tiles[tile_id] = np.array(array)
                tile_id = None
                array = list()

matches = defaultdict(list)

tile_keys = list(tiles.keys())

for tile_id in tile_keys:
    for sub_tile_id in tile_keys:
        if tile_id != sub_tile_id:
            if check_if_match(tiles[tile_id], tiles[sub_tile_id]):
                matches[tile_id].append(sub_tile_id)

ids = []
for tile in matches:
    if len(matches[tile]) == 2:
        ids.append(tile)

print(reduce(mul, ids))


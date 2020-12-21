from collections import defaultdict
import numpy as np

tiles = {}


def rotate(to_rotate, k):
    return np.rot90(to_rotate, k=k)


def match_left(array_1, array_2):
    return np.count_nonzero(array_1[:, -1] - array_2[:, 0]) == 0


def match_bottom(array_1, array_2):
    return np.count_nonzero(array_1[-1] - array_2[0]) == 0


def check_if_match_2(array_1, array_2):
    # 0 - top
    # 1 - right
    # 2 - bottom
    # 3 - left
    for i in range(4):
        if match_left(array_1, rotate(array_2, i)):
            return rotate(array_2, i)

    array_2 = np.flipud(array_2)
    for i in range(4):
        if match_left(array_1, rotate(array_2, i)):
            return rotate(array_2, i)


def check_if_match_3(array_1, array_2):
    # 0 - top
    # 1 - right
    # 2 - bottom
    # 3 - left
    for i in range(4):
        if match_bottom(array_1, rotate(array_2, i)):
            return rotate(array_2, i)

    array_2 = np.flipud(array_2)
    for i in range(4):
        if match_bottom(array_1, rotate(array_2, i)):
            return rotate(array_2, i)


def match(array_1, array_2):
    left_right = np.count_nonzero(array_1[:, -1] - array_2[:, 0]) == 0
    right_left = np.count_nonzero(array_1[:, 0] - array_2[:, -1]) == 0
    top_bottom = np.count_nonzero(array_1[0] - array_2[-1]) == 0
    bottom_top = np.count_nonzero(array_1[-1] - array_2[0]) == 0
    return left_right or right_left or top_bottom or bottom_top


def check_if_match(array_1, array_2):
    for i in range(4):
        if match(array_1, rotate(array_2, i)):
            return True

    array_2 = np.flipud(array_2)
    for i in range(4):
        if match(array_1, rotate(array_2, i)):
            return True

    return False


def count_monsters(mask, picture):
    count = 0
    mask_length, mask_width = len(mask), len(mask[0])
    for picture_i in range(len(picture) - mask_length + 1):
        for picture_j in range(len(picture[0]) - mask_width + 1):
            if np.count_nonzero(
                    picture[picture_i:picture_i + mask_length, picture_j:picture_j + mask_width] * mask - mask) == 0:
                count += 1
    return count


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

to_flip = 1
leftmost = ids[to_flip]
used_lefts = {leftmost}
picture = defaultdict(list)

n = 12
# n = 3


flip_first = False

for row in range(n):
    pixs = leftmost
    # for picture_i in range(10):
    for picture_i in range(1, 9):
        # for picture_j in range(10):
        for picture_j in range(1, 9):
            picture[picture_i + 10 * row].append(tiles[pixs][picture_i][picture_j])

    for i in range(n - 1):
        near = matches[pixs]
        for j in range(4):
            array_2 = check_if_match_2(tiles[pixs], tiles[near[j]])
            if array_2 is not None:
                tiles[near[j]] = array_2
                pixs = near[j]
                break
        else:
            raise Exception('did not converge')

        for picture_i in range(1, 9):
        # for picture_i in range(10):
            for picture_j in range(1, 9):
            # for picture_j in range(10):
                picture[picture_i + 10 * row].append(tiles[pixs][picture_i][picture_j])

    for tile in matches[leftmost]:
        array_2 = check_if_match_3(tiles[leftmost], tiles[tile])
        if array_2 is not None and tile not in used_lefts:
            tiles[tile] = array_2
            leftmost = tile
            break
    else:
        if row == 0:
            flip_first = True
        tiles[leftmost] = np.flipud(tiles[leftmost])
        for tile in matches[leftmost]:
            array_2 = check_if_match_3(tiles[leftmost], tiles[tile])
            if array_2 is not None and tile not in used_lefts:
                tiles[tile] = array_2
                leftmost = tile
                break
    used_lefts.add(leftmost)

if flip_first:
    for i in range(1, 5):
        picture[i], picture[9 - i] = picture[9 - i], picture[i]
picture = np.array([picture[row] for row in picture])

sea_monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

# for i in range(len(picture)):
#     for j in range(len(picture[0])):
#         print(picture[i][j], end="")
#         if j and j % 10 == 0:
#             print(' ', end="")
#     print()
#     if i and i % 10 == 0:
#         print()

p = 0
sea_monster_mask = []
for row in sea_monster:
    p += row.count("#")
    sea_monster_mask.append([1 if x == "#" else 0 for x in row])

pp = 0
for row in picture:
    pp += list(row).count(1)

# for row in picture:
#     print(''.join(list(map(lambda x: "#" if x else ".", row))))

sea_monster_mask = np.array(sea_monster_mask)

c = 0
for i in range(1, 4):
    c = max(c, count_monsters(sea_monster_mask, rotate(picture, i)))

picture = np.flipud(picture)
for i in range(1, 4):
    c = max(c, count_monsters(sea_monster_mask, rotate(picture, i)))

print(pp - p * c)


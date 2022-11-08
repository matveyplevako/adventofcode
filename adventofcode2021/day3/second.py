from collections import defaultdict


def get_ind(lines, with_more_ones=True):
    indexes = set(range(len(lines)))
    for ind in range(len(lines[0].strip())):
        ones = 0
        for row_ind, row in enumerate(lines):
            if row_ind in indexes:
                if row[ind] == '1':
                    ones += 1

        if with_more_ones:
            leave_ones = ones >= len(indexes) / 2
        else:
            leave_ones = ones < len(indexes) / 2
        new_indexes = set()
        for row_ind, row in enumerate(lines):
            if ((row[ind] == '1' and leave_ones) or (row[ind] == '0' and not leave_ones)) and row_ind in indexes:
                new_indexes.add(row_ind)
        indexes = new_indexes
        if len(indexes) == 1:
            break
    assert len(indexes) == 1
    return indexes.pop()


if __name__ == '__main__':

    with open("input.txt") as inp:
        lines = inp.readlines()
        oxy = int(lines[get_ind(lines)], 2)
        co2 = int(lines[get_ind(lines, with_more_ones=False)], 2)
        print(oxy * co2)

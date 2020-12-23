def get_next_3(arr, ind):
    res = list()
    for _ in range(3):
        if ind + 1 >= len(arr):
            res.append(arr.pop(0))
        else:
            res.append(arr.pop((ind + 1)))
    return res


def select_destination(arr, num):
    for diff in range(1, 10):
        n = (num-diff) % 10
        if n in arr:
            return n


cups = list(map(int, list('496138527')))

current_ind = 0

for move in range(100):
    # print("move: ", move+1)
    current_num = cups[current_ind % len(cups)]
    next_3 = get_next_3(cups, current_ind % len(cups))
    destination_num = select_destination(cups, current_num)
    # print(current_num, destination_num)
    # print(cups, next_3)
    destination_ind = cups.index(destination_num)
    cups = cups[:destination_ind+1] + next_3 + cups[destination_ind+1:]
    # print(cups)
    current_ind = (cups.index(current_num) + 1) % len(cups)

ind_1 = cups.index(1)
print(''.join(map(str, cups[ind_1+1:] + cups[:ind_1])))


boxes = {i: [] for i in range(256)}
label_to_val = {}


def get_hash(s):
    hash_val = 0
    for x in s:
        hash_val += ord(x)
        hash_val *= 17
        hash_val %= 256
    return hash_val


def insert_into_box(s):
    label, focal = s.split("=")
    pos = get_hash(label)
    label_to_val[label] = int(focal)
    if label not in boxes[pos]:
        boxes[pos].append(label)


def remove_from_the_boxes(s):
    label = s[:-1]
    pos = get_hash(label)
    if label in boxes[pos]:
        boxes[pos].remove(label)


def main():
    ans = 0
    with open("input.txt") as inp:
        line = inp.readline().strip().split(",")
    for s in line:
        if "=" in s:
            insert_into_box(s)
        elif "-" in s:
            remove_from_the_boxes(s)

    for box_num in range(256):
        for ind, val in enumerate([label_to_val[x] for x in boxes[box_num]]):
            ans += (ind + 1) * val * (box_num + 1)
    print(ans)


if __name__ == '__main__':
    main()

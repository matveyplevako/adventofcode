from collections import defaultdict


with open("input.txt") as inp:
    ranges = {}
    while True:
        line = inp.readline().strip()
        if line:
            name, valid_ranges = line.split(": ")
            ranges[name] = list()
            for rng in valid_ranges.split(" or "):
                l, r = map(int, rng.split("-"))
                ranges[name].append((l, r))
        else:
            break
    _ = inp.readline()
    my_ticket_nums = list(map(int, inp.readline().strip().split(",")))


    _ = inp.readline()
    _ = inp.readline()
    valid_rows = []
    for line in inp.readlines():
        line = line.strip()
        row = []
        for num in line.split(","):
            num = int(num)
            valid = False
            for name in ranges:
                for rng in ranges[name]:
                    l, r = rng
                    if l <= num <= r:
                        valid = True
                        break
                if valid:
                    break
            if valid:
                row.append(num)
        if len(row) == len(my_ticket_nums):
            valid_rows.append(row)

    valid_columns = defaultdict(list)
    for i in range(len(my_ticket_nums)):
        for name in ranges:
            valid_column = True
            for j in range(len(valid_rows)):
                valid_num = False
                for rng in ranges[name]:
                    l, r = rng
                    if l <= valid_rows[j][i] <= r:
                        valid_num = True
                        break
                if not valid_num:
                    valid_column = False
            if valid_column:
                valid_columns[i].append(name)

# print(*valid_columns.values(), sep="\n")
s = sorted(valid_columns, key=lambda x: len(valid_columns[x]))
col_to_position = {}
seen = set()
for pos in s:
    left = (set(valid_columns[pos]) - seen).pop()
    col_to_position[left] = pos
    seen.add(left)
    

mult = 1
for name in "departure location, departure station, departure platform, departure track, departure date, departure time".split(", "):
    mult *= my_ticket_nums[col_to_position[name]]

print(mult)

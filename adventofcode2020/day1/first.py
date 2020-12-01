# part1 O(N)

sums = set()

with open("inp.txt") as inp:
    for line in inp.readlines():
        num = int(line)
        diff = 2020 - num
        if diff in sums:
            print(diff * num)
        else:
            sums.add(num)

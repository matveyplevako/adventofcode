with open("input.txt") as inp:
    ranges = set()
    while True:
        line = inp.readline().strip()
        if line:
            name, valid_ranges = line.split(": ")
            for rng in valid_ranges.split(" or "):
                l, r = map(int, rng.split("-"))
                ranges.add((l, r))
        else:
            break
    _ = inp.readline()
    nums = list(map(int, inp.readline().strip().split(",")))


    _ = inp.readline()
    _ = inp.readline()
    invalid_sum = 0
    for line in inp.readlines():
        line = line.strip()
        for num in line.split(","):
            num = int(num)
            valid = False
            for rng in ranges:
                l, r = rng
                if l <= num <= r:
                    valid = True
                    break
            if not valid:
                invalid_sum += num

    print(invalid_sum)

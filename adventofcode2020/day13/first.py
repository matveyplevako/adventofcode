min_diff = None
min_id = None

with open("input.txt") as inp:
    current_time = int(inp.readline())
    buses = [int(x) for x in inp.readline().split(",") if x != "x"]
    for bus in buses:
        diff = bus - current_time % bus
        if min_diff is None or min_diff > diff:
            min_diff = diff
            min_id = bus * diff

print(min_id)


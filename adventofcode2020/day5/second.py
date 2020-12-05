def find_binary(lc, uc, upper_bound, ticket):
    lower, upper = 0, upper_bound
    for x in ticket:
        dx = (upper - lower) // 2
        if x == lc:
            upper -= dx
        elif x == uc:
            lower += dx
    return lower
    
highest = 0

seats = set()

with open("input.txt") as inp:
    for line in inp.readlines():
        line = line.strip()
        row = find_binary("F", "B", 128, line[:-3])
        column = find_binary("L", "R", 8, line[-3:])
        seat_id = row * 8 + column
        seats.add(seat_id)
        highest = max(highest, seat_id)
           

print(set(range(48, highest + 1)) - seats)

# part 2 O(N^3)

with open("inp.txt") as inp:
    array = []
    for line in inp.readlines():
        array.append(int(line))
    for ind_x, x in enumerate(array):
        for ind_y, y in enumerate(array[ind_x+1:]):
            for z in array[ind_y+1:]:
                if x + y + z == 2020:
                    print(x, y, z)
                    print(x * y * z)

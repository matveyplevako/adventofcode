class Field:
    def __init__(self, field):
        self.field = field
        self.width = len(field[0])
        self.height = len(field[1])


    def __getitem__(self, ind):
        i, j = ind
        return self.field[i][j % self.width]
        

with open("inp.txt") as inp:
    field_array = []
    for line in inp.readlines():
        line = line.strip()
        field_array.append(line)


def find_trees(dj, di):
    field = Field(field_array)
    i, j = 0, 0
    trees = 0
    while i < len(field_array):
        if field[i, j] == "#":
            trees += 1
        i += di
        j += dj
    return trees

print(find_trees(1, 1)*find_trees(3, 1)*find_trees(5, 1)*find_trees(7, 1)*find_trees(1, 2))

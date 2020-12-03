
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

field = Field(field_array)
i, j = 0, 0
trees = 0
while i < len(field_array):
    if field[i, j] == "#":
        trees += 1
    i += 1
    j += 3

print(trees)

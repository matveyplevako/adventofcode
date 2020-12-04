# part1

need_fields = set("byr iyr eyr hgt hcl ecl pid".split())

def check_passprot(passp):
    line = ' '.join(passp).split()
    fields = set()
    for pair in line:
        l, r = pair.split(":")
        if l != "cid":
            fields.add(l)

    return fields ^ need_fields == set()

        

with open("input.txt") as inp:
    field_array = []
    valid = 0
    passprots = inp.readlines()
    passprots.append("\n")
    passp = []
    for i in range(len(passprots)):
        line = passprots[i].strip()
        if line:
            passp.append(line)
        else:
            valid += int(check_passprot(passp))
            passp = []
            

print(valid)

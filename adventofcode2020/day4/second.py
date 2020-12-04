# part2

need_fields = set("byr iyr eyr hgt hcl ecl pid".split())

def check_passprot(passp):
    line = ' '.join(passp).split()
    fields = set()
    for pair in line:
        l, r = pair.split(":")
        if l == "byr":
            if 1920 <= int(r) <= 2002:
                fields.add(l)
        elif l == "iyr":
            if 2010 <= int(r) <= 2020:
                fields.add(l)
        elif l == "eyr":
            if 2020 <= int(r) <= 2030:
                fields.add(l)
        elif l == "hgt":
            if r[-2:] == "cm":
                if 150 <= int(r[:-2]) <= 193:
                    fields.add(l)
            if r[-2:] == "in":
                if 59 <= int(r[:-2]) <= 76:
                    fields.add(l)
        elif l == "hcl":
            if r[0] == "#" and (r[1:].isalnum()):
                fields.add(l)
        elif l == "ecl":
            if r in "amb blu brn gry grn hzl oth".split():
                fields.add(l)
        elif l == "pid":
            if len(r) == 9 and r.isdigit():
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

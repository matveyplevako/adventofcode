from collections import defaultdict

ingrid_count = defaultdict(lambda: defaultdict(int))
can_contain = {}
ingrids = set()
ingrid_list = list()

with open('input.txt') as inp:
    for line in inp.readlines():
        ingrid, allergens = line.strip().split("(contains ")
        ingrid = ingrid.split()
        ingrid_list.append(set(ingrid))
        allergens = allergens[:-1].split(", ")
        for allergen in allergens:
            for ing in ingrid:
                ingrid_count[allergen][ing] += 1
                ingrids.add(ing)



while ingrid_count:
    for allergen in can_contain:
        ingrid_count.pop(allergen, None)
    for allergen in ingrid_count:
        for ingrid in can_contain.values():
            ingrid_count[allergen].pop(ingrid, None)

        values = list(ingrid_count[allergen].values())
        if values:
            c = max(values)
            if values.count(c) == 1:
                can_contain[allergen] = max(ingrid_count[allergen], key=ingrid_count[allergen].get)

true_ingridients = ingrids - set(can_contain.values())

count = 0
for ing in ingrid_list:
    count += len(ing & true_ingridients)

print(count)


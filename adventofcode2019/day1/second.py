with open("input.txt") as inp:
    text = inp.readlines()
    nums = list(map(int, text))


def get_fuel_for_mass(mass):
    return mass // 3 - 2

total = 0
for mass in nums:
    total_mass_for_spacecraft = 0
    while (fuel := get_fuel_for_mass(mass)) > 0:
        total_mass_for_spacecraft += fuel
        mass = fuel
    total += total_mass_for_spacecraft

with open("out2.txt", "w") as out:
    out.write(str(total) + '\n')

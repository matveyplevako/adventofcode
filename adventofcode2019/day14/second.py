from collections import defaultdict
from math import ceil
from bisect import bisect_left

# ELEM -> need dict
formulas = defaultdict(lambda: defaultdict(int))

# ELEM -> produce count
produce = {}

with open("input.txt") as inp:
    for line in inp.readlines():
        left_part, right_part = line.split(" => ")
        need_elements = left_part.split(",")
        num, left_element = right_part.split()
        left_element.strip()
        num = int(num)
        produce[left_element] = num
        for elements in need_elements:
            count, elem_need = elements.split()
            count = int(count)
            formulas[left_element][elem_need] = count


def how_many_ore_needs(need):
    while True:
        for element, element_count in need.items():
            if element != "ORE" and element_count > 0:
                elem = element
                elem_need_count = element_count
                break
        else:
            break

        need_upper_elements = ceil(elem_need_count / produce[elem])
        for formulas_elem in formulas[elem]:
            need[formulas_elem] = need[formulas_elem] + need_upper_elements * formulas[elem][formulas_elem]

        need[elem] -= need_upper_elements * produce[elem]
    return need["ORE"]


def calc(fuel):
    need = defaultdict(int)
    need["FUEL"] = fuel
    return how_many_ore_needs(need)


def binary_search(x, lo, hi):
    a = type('a', (), {"__getitem__": lambda self, fuel: calc(fuel)})()
    pos = bisect_left(a, x, lo, hi)
    return pos



def main():
    have_ore = 1000000000000
    print(binary_search(have_ore, 0, have_ore) - 1)


if __name__ == '__main__':
    main()

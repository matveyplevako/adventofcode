from collections import defaultdict


def check_lines(desk, numbers):
    for line in desk:
        if set(line).issubset(set(numbers)):
            return True

    for i in range(5):
        nums = set()
        for j in range(5):
            nums.add(desk[j][i])
        if nums.issubset(set(numbers)):
            return True


def check_answer(desk, numbers):
    s = 0
    for line in desk:
        s += sum(map(int, set(line) - set(numbers)))
    return s * int(numbers[-1])


def main():
    with open("input.txt") as inp:
        lines = inp.readlines()
        numbers = lines[0].strip().split(",")

        desks = []
        desk = []
        for row in lines[2:]:
            row = row.strip()
            if not row:
                desks.append(desk)
                desk = []
            else:
                desk.append(row.split())
        desks.append(desk)

    for number_ind in range(len(numbers)):
        current_numbers = numbers[:number_ind + 1]
        for desk in desks:
            ready = check_lines(desk, current_numbers)
            if ready:
                print(check_answer(desk, current_numbers))
                return


if __name__ == '__main__':
    main()





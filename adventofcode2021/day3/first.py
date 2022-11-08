from collections import defaultdict

ones_position = defaultdict(lambda: 0)

with open("input.txt") as inp:
    lines = inp.readlines()
    for bits in lines:
        for ind, bit in enumerate(bits):
            if bit == '1':
                ones_position[ind] += 1
    half_size = len(lines) // 2
    number = []
    for i in range(len(ones_position)):
        if ones_position[i] > half_size:
            number.append('1')
        else:
            number.append('0')
    gamma = int(''.join(number), 2)

    number = ['1' if x == '0' else '0' for x in number]
    epsilon = int(''.join(number), 2)

    print(gamma * epsilon)

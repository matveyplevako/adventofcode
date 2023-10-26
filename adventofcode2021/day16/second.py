from functools import reduce
from operator import mul


def bin_to_hex(binary):
    return hex(int(binary, 2))[2:]


def hex_to_bin(hex_num):
    return bin(int(hex_num, 16))[2:]


def bin_to_int(binary):
    return int(binary, 2)


def pad_leading_zeros(packet):
    if len(packet) % 4:
        packet = "0" * (4 - len(packet) % 4) + packet
    return packet


def raw_parse_packet(packet):
    packet_bin = hex_to_bin(packet)
    packet_bin = pad_leading_zeros(packet_bin)
    return packet_bin


def literal_value_operation(packet):
    number = ""
    for i in range(0, len(packet), 5):
        cut = packet[i:i + 5]
        number += cut[1:]
        if cut[0] == "0":
            return bin_to_int(number), packet[i + 5:]


def operator(op, packet):
    length_type_id = packet[0]
    numbers = []
    if length_type_id == "0":
        length = bin_to_int(packet[1:16])
        _packet = packet[16:16 + length]
        packet = packet[16 + length:]
        while _packet:
            number, _packet = execute_paket(_packet)
            numbers.append(number)
    else:
        number = bin_to_int(packet[1:12])
        packet = packet[12:]
        for i in range(number):
            number, packet = execute_paket(packet)
            numbers.append(number)

    number = 0
    if op == 0:
        number = sum(numbers)
    elif op == 1:
        number = reduce(mul, numbers)
    elif op == 2:
        number = min(numbers)
    elif op == 3:
        number = max(numbers)
    elif op == 5:
        number = numbers[0] > numbers[1]
    elif op == 6:
        number = numbers[0] < numbers[1]
    elif op == 7:
        number = numbers[0] == numbers[1]

    return int(number), packet


def execute_paket(packet):
    version = bin_to_int(packet[:3])
    op = bin_to_int(packet[3:6])
    packet = packet[6:]
    if op == 4:
        return literal_value_operation(packet)
    else:
        return operator(op, packet)


def main():
    with open("input.txt") as inp:
        for i, line in enumerate(inp.readlines()):
            line = line.strip()

    packet = raw_parse_packet(line)
    print(execute_paket(packet)[0])


if __name__ == '__main__':
    main()

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
            return packet[i + 5:]


def operator(packet):
    version = 0
    length_type_id = packet[0]
    if length_type_id == "0":
        length = bin_to_int(packet[1:16])
        _packet = packet[16:16 + length]
        packet = packet[16 + length:]
        while _packet:
            _version, _packet = execute_paket(_packet)
            version += _version
    else:
        number = bin_to_int(packet[1:12])
        packet = packet[12:]
        for i in range(number):
            _version, packet = execute_paket(packet)
            version += _version
    return version, packet


def execute_paket(packet):
    version = bin_to_int(packet[:3])
    op = bin_to_int(packet[3:6])
    packet = packet[6:]
    if op == 4:
        return version, literal_value_operation(packet)
    else:
        _version, packet = operator(packet)
        return version + _version, packet


def main():
    with open("input.txt") as inp:
        for i, line in enumerate(inp.readlines()):
            line = line.strip()

    packet = raw_parse_packet(line)
    print(execute_paket(packet)[0])


if __name__ == '__main__':
    main()

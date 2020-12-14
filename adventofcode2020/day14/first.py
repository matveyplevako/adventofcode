mem = {}

def apply_mask(mask, num):
    new_num = list(num)
    if len(new_num) < len(mask):
        new_num = ["0"] * (len(mask) - len(new_num)) + new_num
    for ind, bit in enumerate(mask):
        if bit != "X":
            new_num[ind] = bit
    return new_num


with open("input.txt") as inp:
    mask = inp.readline().strip().split(" = ")[1]
    for line in inp.readlines():
        address, value = line.strip().split(" = ")
        if address == "mask":
            mask = value
        else:
            address = int(address[4:-1])
            new_num = ''.join(apply_mask(mask, bin(int(value))[2:]))
            with_mask = int(new_num, 2)
            mem[address] = with_mask

        
print(sum(mem.values()))
            

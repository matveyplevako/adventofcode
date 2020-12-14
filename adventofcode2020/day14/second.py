mem = {}

def generate_all_masks(mask, ind, num):
    if ind < len(mask):
        if mask[ind] == "X":
            new_mask = mask[:ind] + "2" + mask[ind + 1:]
            val_0 = generate_all_masks(new_mask, ind + 1, num)
            new_mask = mask[:ind] + "1" + mask[ind + 1:]
            val_1 = generate_all_masks(new_mask, ind + 1, num)
            return val_0 + val_1
        else:
            return generate_all_masks(mask, ind+1, num)
    else:
        return [apply_mask(mask, num)]




def apply_mask(mask, num):
    new_num = list(num)
    if len(new_num) < len(mask):
        new_num = ["0"] * (len(mask) - len(new_num)) + new_num
    for ind, bit in enumerate(mask):
        if bit == "1":
            new_num[ind] = bit
        if bit == "2":
            new_num[ind] = "0"
    
    return int(''.join(new_num), 2)


with open("input.txt") as inp:
    mask = inp.readline().strip().split(" = ")[1]
    for line in inp.readlines():
        address, value = line.strip().split(" = ")
        if address == "mask":
            mask = value
        else:
            address = address[4:-1]
            for with_mask in generate_all_masks(mask, 0, bin(int(address))[2:]):
                mem[with_mask] = int(value)


print(sum(mem.values()))
 

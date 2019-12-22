LENGTH = 10007

deck = list(range(LENGTH))

with open("input.txt") as inp:
    for instruction in inp.readlines():
        if "new" in instruction:
            deck = deck[::-1]
        if "cut" in instruction:
            cut = int(instruction.split()[-1])
            deck = deck[cut:] + deck[:cut]
        if "increment" in instruction:
            inc = int(instruction.split()[-1])
            new_deck = [-1] * LENGTH
            for ind, elem in enumerate(deck):
                pos = (ind * inc) % LENGTH
                new_deck[pos] = elem
            assert -1 not in new_deck
            deck = new_deck

print(deck.index(2019))

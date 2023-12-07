from collections import Counter


class Card:
    def __init__(self, card, pos, bid):
        self.card = card
        self.pos = pos
        self.bid = bid

    def __lt__(self, other):
        if self.pos != other.pos:
            return self.pos < other.pos
        return lt_compare_cards(self.card, other.card)


def find_comb(card):
    c = Counter(card)
    if len(c.values()) == 1:
        return 7
    if set(c.values()) == {4, 1}:
        return 6
    if set(c.values()) == {3, 2}:
        return 5
    if 3 in c.values():
        return 4
    if list(c.values()).count(2) == 2:
        return 3
    if 2 in c.values():
        return 2
    return 1


def lt_compare_cards(c1, c2):
    c_m = "AKQJT98765432"
    for i in range(len(c1)):
        c1i, c2i = c_m.index(c1[i]), c_m.index(c2[i])
        if c1i != c2i:
            return c1i > c2i


def main():
    cards = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            card, bid = line.split()
            cards.append(Card(card, find_comb(card), int(bid)))
    ans = 0
    for ind, x in enumerate(sorted(cards)):
        ans += (ind + 1) * x.bid
    print(ans)


if __name__ == '__main__':
    main()

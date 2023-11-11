import functools
import itertools


@functools.cache
def count_rec(p1, p2, p1s, p2s):
    w1 = w2 = 0
    for d1, d2, d3 in itertools.product((1, 2, 3), repeat=3):
        p1_new = (p1 - 1 + d1 + d2 + d3) % 10 + 1
        p1s_new = p1s + p1_new
        if p1s_new >= 21:
            w1 += 1
        else:
            w2_new, w1_new = count_rec(p2, p1_new, p2s, p1s_new)
            w1 += w1_new
            w2 += w2_new
    return w1, w2


def main():
    player_pos = {}
    with open("input.txt") as inp:
        player_pos[0] = int(inp.readline().split()[-1])
        player_pos[1] = int(inp.readline().split()[-1])

    print(count_rec(player_pos[0], player_pos[1], 0, 0))


if __name__ == '__main__':
    main()

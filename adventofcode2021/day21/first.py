class Dice:
    def __init__(self):
        self.side = 1
        self.roll_count = 0

    def get_sum_3_rolls(self):
        return sum(self.roll() for _ in range(3))

    def roll(self):
        roll_res = self.side
        self.side += 1
        self.roll_count += 1
        if self.side > 100:
            self.side = 1
        return roll_res


def main():
    player_pos = {}
    with open("input.txt") as inp:
        player_pos[0] = int(inp.readline().split()[-1]) - 1
        player_pos[1] = int(inp.readline().split()[-1]) - 1

    player_score = {0: 0, 1: 0}

    turn = 0
    d = Dice()
    while all(map(lambda x: x < 1000, player_score.values())):
        player_pos[turn] = (player_pos[turn] + d.get_sum_3_rolls()) % 10
        player_score[turn] += (player_pos[turn] + 1)
        turn = (turn + 1) % 2

    if player_score[0] < 1000:
        lost = 0
    else:
        lost = 1

    print(player_score[lost] * d.roll_count)


if __name__ == '__main__':
    main()

def main():
    s = 0
    with open("input.txt") as inp:
        for line in inp.readlines():
            game, colors = line.split(":")
            game_id = int(game.split()[1])
            possible = True
            for b_set in colors.split(', '):
                for b in b_set.split('; '):
                    color = b.split()[-1]
                    value = int(b.split()[0])
                    if color == "blue":
                        if value > 14:
                            possible = False
                    elif color == "red":
                        if value > 12:
                            possible = False
                    else:
                        if value > 13:
                            possible = False
            if possible:
                s += game_id
    print(s)


if __name__ == '__main__':
    main()

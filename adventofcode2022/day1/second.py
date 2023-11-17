def main():
    with open("input.txt") as inp:
        inp = inp.read()
        elves = inp.split('\n\n')
    elves = [sum(map(int, elf.split('\n'))) for elf in elves]
    print(sum(sorted(elves)[-3:]))


if __name__ == '__main__':
    main()

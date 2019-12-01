with open("input.txt") as inp:
    text = inp.readlines()
    nums = list(map(int, text))

ans = sum([mass // 3 - 2 for mass in nums])

with open("out1.txt", "w") as out:
    out.write(str(ans) + '\n')

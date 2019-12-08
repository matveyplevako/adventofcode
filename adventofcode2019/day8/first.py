from collections import defaultdict

with open("input.txt") as inp:
    digits = inp.read().strip()

W, H = 25, 6

zeros = None
answer = None

for frame_start in range(0, len(digits), W * H):
    frame = digits[frame_start:frame_start + W * H]
    for h in range(H):
        for w in range(W):
            if zeros is None or frame.count('0') < zeros:
                zeros = frame.count('0')
                answer = frame.count('1') * frame.count('2')

print(answer)

with open("out1.txt", "w") as out:
    out.write(str(answer) + '\n')

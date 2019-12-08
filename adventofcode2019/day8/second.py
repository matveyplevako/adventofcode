from collections import defaultdict

with open("input.txt") as inp:
    digits = inp.read().strip()

W, H = 25, 6

pixels = defaultdict(dict)

for frame_start in range(0, len(digits), W * H):
    frame = digits[frame_start:frame_start + W * H]
    for h in range(H):
        for w in range(W):
            if pixels[h].get(w, -1) == -1 and frame[h * W + w] != '2':
                pixels[h][w] = frame[h * W + w]


for i in range(H):
    for j in range(W):
        print('.' if pixels[i][j] == '1' else ' ', end='')
    print()

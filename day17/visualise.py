import sys
from PIL import Image, ImageDraw

scale = 8

color_map = {
    ' ': (235, 210, 160),
    '.': (235, 215, 160),
    '~': (30, 144, 255),
    '|': (100, 205, 170),
    '#': (140, 110, 40)
}

grid = list(map(lambda l: l.rstrip('\n'), open("viz_filled.txt")))

w, h = len(grid[0]), len(grid)

im = Image.new('RGB', (w * scale, h * scale))
dr = ImageDraw.Draw(im)

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        dr.rectangle([(j * 8, i * 8), ((j + 1) * scale - 1, (i + 1) * scale - 1)], fill=color_map[cell])

im.save('day17_visualized.png')

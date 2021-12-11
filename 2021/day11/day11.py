#!/usr/bin/env python

import os
import sys

import numpy as np

f = open(os.path.join(sys.path[0], "input11.txt"))
input = f.read()

grid = []

for line in input.splitlines():
    grid.append([int(x) for x in line])
grid = np.array(grid)

neighbors = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]


def flash(grid):
    tracker = np.zeros_like(grid)
    while len(np.argwhere(grid > 9)) > 0:
        flashes = np.argwhere(grid > 9)
        for x, y in flashes:
            grid[x, y] = 0
            tracker[x, y] = 1
            for dx, dy in neighbors:
                if (
                    0 <= dx + x < 10
                    and 0 <= dy + y < 10
                    and tracker[dx + x, dy + y] == 0
                ):
                    grid[dx + x, dy + y] += 1
    return len(np.argwhere(grid == 0))


total = 0
round = 0

for _ in range(344):
    round += 1
    grid = grid + 1
    flashed = flash(grid)
    if round <= 100:

        total += flashed
    if flashed == 100 :
        break

print("Part 1:", total)
print("Part 2:", round)

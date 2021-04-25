#!/usr/bin/env python

import numpy as np

size = 300

grid = np.zeros(shape=(size, size))
grid = grid.astype(int)

serial = 4842

for x in range(1, size + 1):
    for y in range(1, size + 1):
        rackID = x + 10
        power = rackID * y
        power += serial
        power *= rackID
        power = (power // 100) % 10
        power = int(power) - 5
        grid[x - 1][y - 1] = power

bestx = 0
besty = 0
bestpower = 0
bestsize = 0

for s in range(1, 16):
    for y in range(size - s + 1):
        for x in range(size - s + 1):
            newpower = grid[x : x + s, y : y + s].sum()
            if newpower > bestpower:
                bestpower = newpower
                bestx = x + 1
                besty = y + 1
                bestsize = s

print(bestx, besty, bestsize, bestpower)

#!/usr/bin/env python

import os
import sys
import numpy as np

f = open(os.path.join(sys.path[0], "input14.txt"))
input = f.read()

test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

data = []
for line in test.splitlines():
    points = line.split(" -> ")
    collection = []
    for p in points:
        (x, y) = p.split(",")
        collection.append([int(x), int(y)])
    for e, val in enumerate(collection[1:], start=1):
        xx = sorted([collection[e - 1][0], collection[e][0]])
        yy = sorted([collection[e - 1][1], collection[e][1]])
        for x in range(xx[0], xx[1] + 1):
            for y in range(yy[0], yy[1] + 1):
                data.append([x, y])

data = np.array(data)

xoffset = np.min(data[:, 0])

grid = np.zeros(
    (
        np.max(data[:, 1]) + 1,
        np.max(data[:, 0]) - xoffset + 1,
    ),
    int,
)

for x, y in data:
    gridx = x - np.min(data[:, 0])
    gridy = y
    grid[gridy, gridx] = 2

# print(grid)


def stuck(grid, x, y):
    if grid[y + 1, x] != 0 and grid[y + 1, x - 1] != 0 and grid[y + 1, x + 1]:
        return True
    return False


def sand(grid, x, y):
    None


curx = 500 - xoffset
cury = 0
dimy, dimx = np.shape(grid)


def drop(grid, x, y):
    if grid[y + 1, x] == 0:
        return x, y + 1
    elif grid[y + 1, x - 1] == 0:
        return x - 1, y + 1
    elif grid[y + 1, x + 1] == 0:
        return x + 1, y + 1
    return x, y


for _ in range(25):
    nextx, nexty = drop(grid, curx, cury)
    #    print("outer", curx, cury)
    while (
        (nextx != curx or nexty != cury)
        and nextx >= 0
        and nextx < dimx
        and nexty < dimy
    ):
        curx, cury = nextx, nexty
        nextx, nexty = drop(grid, curx, cury)
    #        print("inner", nextx, nexty)
    if nextx >= 0:
        grid[nexty, nextx] = 1
    else:
        break
    curx = 500 - xoffset
    cury = 0
#    print(grid)

print(np.sum(grid == 1))

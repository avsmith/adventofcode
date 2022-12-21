#!/usr/bin/env python

import os
import sys
import numpy as np

f = open(os.path.join(sys.path[0], "input14.txt"))
input = f.read()

test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def parse_input(text):
    data = []
    for line in text.splitlines():
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
    return np.array(data)


def make_grid(text, part2=False):
    data = parse_input(text)
    xo = np.min(data[:, 0])
    height = np.max(data[:, 1]) + 1 + 2 * part2
    width = np.max(data[:, 0]) - xo + 1 + 2 * height * part2

    if part2:
        xo -= height * part2

    grid = np.zeros(
        (
            height,
            width,
        ),
        int,
    )

    for x, y in data:
        gridx = x - np.min(data[:, 0]) + height * part2
        gridy = y
        grid[gridy, gridx] = 2

    if part2:
        grid[-1, :] = 2

    return grid, xo


grid, xoffset = make_grid(input)

curx = 500 - xoffset
cury = 0
dimy, dimx = np.shape(grid)


def drop(g, x, y):
    if g[y + 1, x] == 0:
        return x, y + 1
    elif g[y + 1, x - 1] == 0:
        return x - 1, y + 1
    elif g[y + 1, x + 1] == 0:
        return x + 1, y + 1
    return x, y


def print_grid(g):
    count = 1
    for row in g:
        for item in row:
            if item == 2:
                print("#", sep="", end="")

            elif item == 1:
                print("o", sep="", end="")
            else:
                print(".", sep="", end="")
        print(" ", count, sep="", end="\n")
        count += 1

    print("", sep="", end="\n")


for _ in range(6000):
    nextx, nexty = drop(grid, curx, cury)
    #    print("outer", curx, cury)
    while (
        (nextx != curx or nexty != cury)
        and nextx >= 0
        and nextx < dimx
        and nexty < dimy - 1
    ):
        curx, cury = nextx, nexty
        nextx, nexty = drop(grid, curx, cury)
    #        print("inner", nextx, nexty)
    if nextx >= 0 and nexty <= dimy - 2:
        grid[nexty, nextx] = 1
    else:
        break
    curx = 500 - xoffset
    cury = 0
    # print_grid(grid)

print_grid(grid)
print("Part1:", np.sum(grid == 1))
# Answer 805

g2, xoff = make_grid(input, True)


curx = 500 - xoff
cury = 0
dimy, dimx = np.shape(g2)

for _ in range(1000000):
    nextx, nexty = drop(g2, curx, cury)
    #    print("outer", curx, cury)
    while (
        (nextx != curx or nexty != cury)
        and nextx >= 0
        and nextx < dimx
        and nexty < dimy - 1
    ):
        curx, cury = nextx, nexty
        nextx, nexty = drop(g2, curx, cury)
    #        print("inner", nextx, nexty)
    if nextx >= 0 and nexty <= dimy - 2:
        g2[nexty, nextx] = 1
    else:
        break
    curx = 500 - xoff
    cury = 0

print("Part2:", np.sum(g2 == 1))
# Answer 25161

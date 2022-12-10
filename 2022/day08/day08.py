#!/usr/bin/env python

import sys
import os

import numpy as np


f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()

test = """30373
25512
65332
33549
35390
"""


grid = []

for line in input.splitlines():
    grid.append([int(x) for x in line])

grid = np.array(grid)


def visible_trees(g):
    z = np.zeros_like(g)
    x, y = np.shape(z)
    z[(0, x - 1), :] = 1
    z[:, (0, y - 1)] = 1

    for xpos in range(1, x - 1):
        for ypos in range(1, y - 1):
            tree = g[xpos, ypos]
            visible = np.any(
                [
                    np.all(g[:xpos, ypos] < tree),
                    np.all(g[xpos + 1 :, ypos] < tree),
                    np.all(g[xpos, :ypos] < tree),
                    np.all(g[xpos, ypos + 1 :] < tree),
                ]
            )
            if visible:
                z[xpos, ypos] = 1
    return np.sum(z)


def tree_score(g):
    z = np.zeros_like(g)
    x, y = np.shape(z)
    for xpos in range(1, x - 1):
        for ypos in range(1, y - 1):
            tree = g[xpos, ypos]
            left = 1
            for y1 in range(ypos - 1, 0, -1):
                if g[xpos, y1] < tree:
                    left += 1
                else:
                    break
            left = min(left, ypos)
            right = 1
            for y2 in range(ypos + 1, y):
                if g[xpos, y2] < tree:
                    right += 1
                else:
                    break
            right = min(right, y - ypos - 1)
            up = 1
            for x1 in range(xpos - 1, 0, -1):
                if g[x1, ypos] < tree:
                    up += 1
                else:
                    break
            up = min(up, xpos)
            down = 1
            for x2 in range(xpos + 1, x):
                if g[x2, ypos] < tree:
                    down += 1
                else:
                    break
            down = min(down, x - xpos - 1)
            z[xpos, ypos] = up * left * right * down
    return np.max(z)


print("Part1:", visible_trees(grid))
print("Part2:", tree_score(grid))

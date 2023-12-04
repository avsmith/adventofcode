#!/usr/bin/env python

import os
import sys

import numpy as np

f = open(os.path.join(sys.path[0], "input13.txt"))
input = f.read()

positions = []
folds = []

for line in input.splitlines():
    if "," in line:
        pos = [int(x) for x in line.split(",")]
        positions.append(pos)
    if "=" in line:
        axis, value = line.split(" ")[2].split("=")
        folds.append([axis, int(value)])

positions = np.array(positions)


def make_grid(xy):
    xmax, ymax = np.amax(xy, axis=0)
    grid = np.zeros((ymax + 1, xmax + 1), dtype="i")
    for x, y in xy:
        grid[y, x] = 1
    return grid


def print_grid(grid):
    print(
        *["".join(map(str, row)).replace("1", "#").replace("0", " ") for row in grid],
        sep="\n"
    )


grid = make_grid(positions)
part1 = 0

for i, fold in enumerate(folds):
    xmax, ymax = np.amax(positions, axis=0)
    if fold[0] == "x":
        axis = fold[1]
        left = grid[:, :axis]
        right = grid[:, axis + 1 :]
        xneed = np.shape(left)[1] - np.shape(right)[1]
        if xneed > 0:
            ydim = np.shape(grid)[0]
            xpadding = np.zeros((ydim, xneed))
            right = np.append(right, xpadding, axis=1)
        right_flip = np.flip(right, axis=1)
        newgrid = np.where((left + right_flip) > 0, 1, 0)
    elif fold[0] == "y":
        axis = fold[1]
        top = grid[:axis, :]
        bottom = grid[axis + 1 :, :]
        yneed = np.shape(top)[0] - np.shape(bottom)[0]
        if yneed > 0:
            xdim = np.shape(grid)[1]
            ypadding = np.zeros((yneed, xdim))
            bottom = np.append(bottom, ypadding, axis=0)
        bottom_flip = np.flip(bottom, axis=0)
        newgrid = np.where((top + bottom_flip) > 0, 1, 0)

    grid = newgrid
    if i == 0:
        part1 = sum(sum(grid))

print("Part 1:", part1)
print()
print("Part 2:", "\n")
print_grid(grid)

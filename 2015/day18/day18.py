#!/usr/bin/env python

import os
import sys
import numpy as np

testinput = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

f = open(os.path.join(sys.path[0], "input18.txt"))
input = f.read()

grid = [[1 if i == "#" else 0 for i in row] for row in input.splitlines()]
grid2 = grid


def neighbors(array, stuck=False):
    nrows = len(array)
    ncols = len(array[0])
    new = [[0 for i in range(ncols)] for j in range(nrows)]
    if stuck:
        array = light_corners(array)
        new = light_corners(new)
    for i in range(nrows):
        for j in range(ncols):
            current = array[i][j]
            lit = 0
            for ii in range(max(i - 1, 0), min(i + 2, nrows)):
                for jj in range(max(j - 1, 0), min(j + 2, ncols)):
                    lit += array[ii][jj]
            neighbor = lit - current
            if current == 1 and (neighbor == 2 or neighbor == 3):
                new[i][j] = 1
            elif current == 0 and neighbor == 3:
                new[i][j] = 1
    return new


def light_corners(array):
    array[0][0] = 1
    array[-1][0] = 1
    array[0][-1] = 1
    array[-1][-1] = 1
    return array


for i in range(100):
    grid = neighbors(grid)
for i in range(100):
    grid2 = neighbors(grid2, stuck=True)

print("Part 1:", np.sum(grid))
print("Part 2:", np.sum(grid2))

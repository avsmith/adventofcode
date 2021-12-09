#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read()

grid = []

for line in input.splitlines():
    grid.append([int(x) for x in line])


def low_points(grid):
    low = []
    for i in range(len(grid)):
        for j, value in enumerate(grid[i]):
            neighbors = []
            if i != 0 or j != len(grid[i]) - 1 or i != len(grid) - 1 or j != 0:
                if i != 0:
                    neighbors.append(grid[i - 1][j])
                if j != len(grid[i]) - 1:
                    neighbors.append(grid[i][j + 1])
                if i != len(grid) - 1:
                    neighbors.append(grid[i + 1][j])
                if j != 0:
                    neighbors.append(grid[i][j - 1])
            else:
                neighbors = [
                    grid[i - 1][j],
                    grid[i][j + 1],
                    grid[i + 1][j],
                    grid[i][j - 1],
                ]
            test = [value < x for x in neighbors]
            if all(test):
                low.append([i, j])
    return low


def low_score(grid):
    points = low_points(grid)
    score = 0
    for p in points:
        score += grid[p[0]][p[1]] + 1
    return score


print("Part 1:", low_score(grid))
#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read()

grid = []

for line in input.splitlines():
    grid.append([int(x) for x in line])


def neighbor_values(grid, i, j):
    neighbors = []
    if i != 0 or j != len(grid[i]) - 1 or i != len(grid) - 1 or j != 0:
        if i != 0:
            neighbors.append([i - 1, j, grid[i - 1][j]])
        if j != len(grid[i]) - 1:
            neighbors.append([i, j + 1, grid[i][j + 1]])
        if i != len(grid) - 1:
            neighbors.append([i + 1, j, grid[i + 1][j]])
        if j != 0:
            neighbors.append([i, j - 1, grid[i][j - 1]])
    else:
        neighbors = [
            [i - 1, j, grid[i - 1][j]],
            [i, j + 1, grid[i][j + 1]],
            [i + 1, j, grid[i + 1][j]],
            [i, j - 1, grid[i][j - 1]],
        ]
    return neighbors


def low_points(grid):
    low = []
    for i in range(len(grid)):
        for j, value in enumerate(grid[i]):
            neighbors = neighbor_values(grid, i, j)
            test = [value < x[2] for x in neighbors]
            if all(test):
                low.append([i, j])
    return low


def low_score(grid):
    points = low_points(grid)
    score = 0
    for p in points:
        score += grid[p[0]][p[1]] + 1
    return score


def find_basin(grid, i, j):
    basin_values = [[i, j, grid[i][j]]]
    value = grid[i][j]
    neighbors = neighbor_values(grid, i, j)
    increasing = [x for x in neighbors if value < x[2] and x[2] != 9]
    if len(increasing) > 0:
        for details in increasing:
            basin_values.append(details)
        for new in increasing:
            increasing_neighbors = find_basin(grid, new[0], new[1])
            if len(increasing_neighbors) > 0:
                basin_values += increasing_neighbors
    # Make unique, due to multiple potential paths to increasing points
    basin_values = [list(x) for x in set(tuple(x) for x in basin_values)]
    return basin_values


def basin_sizes(grid):
    basins = []
    points = low_points(grid)
    for p in points:
        basins.append(len(find_basin(grid, p[0], p[1])))
    return basins


def basin_score(grid):
    size_values = basin_sizes(grid)
    size_values = sorted(size_values, reverse=True)
    score = size_values[0] * size_values[1] * size_values[2]
    return score


print("Part 1:", low_score(grid))
print("Part 2:", basin_score(grid))

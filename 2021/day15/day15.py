#!/usr/bin/env python

import sys
import os

import numpy as np
import networkx as nx

f = open(os.path.join(sys.path[0], "input15.txt"))
input = f.read()


grid = []

for line in input.splitlines():
    grid.append([int(x) for x in line])


def make_graph(grid):
    TmpG = nx.DiGraph()

    for ix, iy in np.ndindex(grid.shape):
        if ix > 0:
            TmpG.add_edge((ix - 1, iy), (ix, iy), weight=grid[(ix, iy)])

        if ix < grid.shape[0] - 1:
            TmpG.add_edge((ix + 1, iy), (ix, iy), weight=grid[(ix, iy)])

        if iy > 0:
            TmpG.add_edge((ix, iy - 1), (ix, iy), weight=grid[(ix, iy)])

        if iy < grid.shape[1] - 1:
            TmpG.add_edge((ix, iy + 1), (ix, iy), weight=grid[(ix, iy)])
    return TmpG


def roll_grid(grid, delta):
    newgrid = np.where(grid + delta > 9, grid + delta - 9, grid + delta)
    return newgrid


def expand_grid(grid, expand=1):
    horizontal_grid = np.copy(grid)
    for d in range(1, expand):
        horizontal_grid = np.append(horizontal_grid, roll_grid(grid, d), axis=1)
    vertical_grid = np.copy(horizontal_grid)
    for d in range(1, expand):
        vertical_grid = np.append(vertical_grid, roll_grid(horizontal_grid, d), axis=0)
    return vertical_grid


grid = np.array(grid)

G1 = make_graph(grid)
print(
    "Part 1:",
    nx.dijkstra_path_length(G1, (0, 0), (grid.shape[0] - 1, grid.shape[1] - 1)),
)

grid5 = expand_grid(grid, 5)
G5 = make_graph(grid5)
print(
    "Part 2:",
    nx.dijkstra_path_length(G5, (0, 0), (grid5.shape[0] - 1, grid5.shape[1] - 1)),
)

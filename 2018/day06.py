#!/usr/bin/env python

import numpy as np

with open("day06.txt", "r") as fh:
    lines = [line.strip().split(", ") for line in fh.readlines()]

for inner in lines:
    for index, string in enumerate(inner):
        inner[index] = int(string)

lines = [tuple(x) for x in lines]
# print(lines)

import sys

# lines = lines[0:2]
# lines = [(1,1),(1,5),(5,1),(5,5),(3,3)]
# lines = [(1, 1),
# (1, 6),
# (8, 3),
# (3, 4),
# (5, 5),
# (8, 9)]
X, Y = np.amax(lines, axis=0)
result = np.zeros((X, Y), dtype=int)


def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum(abs(nodes - node), axis=1)
    if len(np.argwhere(dist_2 == np.amin(dist_2))) > 1:
        return -1
    else:
        return np.argmin(dist_2)


def node_dist(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum(abs(nodes - node), axis=1)
    return sum(dist_2)


result2 = np.zeros((X, Y), dtype=int)
for x in range(X):
    for y in range(Y):
        result2[x, y] = node_dist([(x, y)], lines)

# print(result2)
print(len(np.argwhere(result2 < 10000)))

"""
from string import ascii_uppercase, ascii_lowercase
let = ascii_uppercase[0:6]
"""

# print(let)
for x in range(10):
    for y in range(10):
        result[x, y] = closest_node([(x, y)], lines)


border = np.copy(result)
border[1:-1, 1:-1] = -1
sums = []
total = 0
infinite = set()
for x in range(-1, len(lines)):
    matchlen = len(np.argwhere(result == x))
    sums.append(matchlen)
    total += matchlen
    if len(np.argwhere(border == x)) > 0:
        infinite.add(x)
# print(border)
# print(sums)
for x in range(-1, len(lines)):
    if x not in infinite:
        None
#    print(x, sums[x+1])

# print(X*Y)
# print(total)

#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()

data = []

for line in input.splitlines():
    sides = [int(x) for x in line.split()]
    data.append(sides)


def legal_triangle(sides):
    s = sorted(sides)
    if s[0] + s[1] > s[2]:
        return True
    return False


def part1(tri):
    triangles = 0
    for sides in data:
        if legal_triangle(sides):
            triangles += 1
    return triangles


def part2(tri):
    triangles = 0
    for i in range(0, len(tri), 3):
        for j in range(3):
            if legal_triangle([tri[i][j], tri[i + 1][j], tri[i + 2][j]]):
                triangles += 1
    return triangles


print("Part 1:", part1(data))
print("Part 2:", part2(data))

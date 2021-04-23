#!/usr/bin/env python

import os, sys

f = open(os.path.join(sys.path[0], "input03.txt"))
data = f.read()

houses = [[0, 0]]
santa = [[0, 0]]
robo = [[0, 0]]


def deliver_presents(h, m):
    (ns, ew) = h[-1]
    if move == "^":
        ns += 1
    if move == "v":
        ns -= 1
    if move == "<":
        ew -= 1
    if move == ">":
        ew += 1
    h.append([ns, ew])


for i in range(len(data)):
    move = data[i]
    deliver_presents(houses, move)
    if i % 2:
        deliver_presents(santa, move)
    else:
        deliver_presents(robo, move)

num_houses = len(set([tuple(h) for h in houses]))
print("Houses year 1:", num_houses)
num_houses_year2 = len(set([tuple(h) for h in santa + robo]))
print("Houses year 2:", num_houses_year2)

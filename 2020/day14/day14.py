#!/usr/bin/env python

import re
import numpy as np
import itertools

import os, sys

f = open(os.path.join(sys.path[0], "input14.txt"))
input = f.read()


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def reverse(string):
    string = string[::-1]
    return string


maskre = re.compile("mask = ([01X]+)")
memre = re.compile("mem\[(\d+)\] = (\d+)")

results = dict()
results2 = dict()

for line in input.splitlines():
    maskmatch = maskre.match(line)
    memmatch = memre.match(line)
    if maskmatch:
        maskloc = {"X": [], "0": [], "1": []}
        mask = maskmatch.group(1)
        for i in range(len(mask)):
            maskloc[reverse(mask)[i]].append(i)
    elif memmatch:
        (loc, val) = memmatch.groups()
        v = int(val)
        loc2 = int(loc)
        v2 = int(val)
        loc2 = int(loc)
        for i in maskloc["0"]:
            v = clear_bit(v, i)
        for i in maskloc["1"]:
            v = set_bit(v, i)
            loc2 = set_bit(loc2, i)
        combos = itertools.product([0, 1], repeat=len(maskloc["X"]))
        for c in combos:
            for bit, change in zip(c, maskloc["X"]):
                if bit == 0:
                    loc2 = clear_bit(loc2, change)
                elif bit == 1:
                    loc2 = set_bit(loc2, change)
                else:
                    raise Error("Something went wrong")
            results2[loc2] = v2
        results[loc] = v


print(np.sum(list(results.values())))
print(np.sum(list(results2.values())))

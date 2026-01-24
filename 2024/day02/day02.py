#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input02.txt"))
input = f.read()

good = 0


def safe(d):
    inc = all(i < j for i, j in zip(d, d[1:]))
    dec = all(i > j for i, j in zip(d, d[1:]))
    if inc or dec:
        if inc:
            mdiff = maxDiff(d)
        elif dec:
            mdiff = maxDiff(sorted(d))
        if mdiff <= 3:
            return True
        else:
            return False
    else:
        return False


def checkReports(l, part2=False):
    d = [int(ele) for ele in l.split()]
    if part2:
        for i in range(len(d)):
            subreport = list(d)
            del subreport[i]
            subsafe = safe(subreport)
            if subsafe:
                return subsafe

    else:
        return safe(d)


def maxDiff(a):
    diff_list = []

    for i in range(1, len(a)):
        diff_list.append(a[i] - a[i - 1])

    return max(diff_list)


good1 = 0
good2 = 0
for line in input.splitlines():
    if checkReports(line):
        good1 += 1
        good2 += 1
    elif checkReports(line, True):
        good2 += 1


print(f"Part 1: {good1}")
print(f"Part 1: {good2}")

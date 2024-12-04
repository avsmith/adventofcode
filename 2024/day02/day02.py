#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input02.txt"))
input = f.read()

good = 0


def safe(report):
    d = [int(ele) for ele in report.split()]
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


def maxDiff(a):
    diff_list = []

    for i in range(1, len(a)):
        diff_list.append(a[i] - a[i - 1])

    return max(diff_list)


good = 0
for line in input.splitlines():
    if safe(line):
        good += 1

print(good)

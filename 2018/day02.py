#!/usr/bin/env python

import collections
import timeit
import numpy as np


def sortchar(words):
    return "".join(sorted(list(words)))


def twothree(w):
    d = collections.defaultdict(int)
    two = False
    three = False
    for c in w:
        d[c] += 1
    for char in d:
        if d[char] == 2:
            two = True
        if d[char] == 3:
            three = True
    return [two, three]


with open("day02.txt", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]

ctest = [twothree(line) for line in lines]

result = [sum(i) for i in zip(*ctest)]

# Part 1 Answer
print(result[0] * result[1])


def commonword(w1, w2):
    u = zip(w1, w2)
    y = []
    for i, j in u:
        if i == j:
            y.append(j)
    return "".join(y)


def parttwo():
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            w = commonword(lines[i], lines[j])
            if len(lines[i]) - len(w) == 1:
                True


def parttwolin():
    d = set()
    for s in lines:
        for i in range(len(s)):
            new_str = "".join((s[:i], "_", s[i + 1 :]))
            if new_str in d:
                print("".join(n for n in new_str if n != "_"))
                return
            d.add(new_str)


# Part 2 Answer
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        w = commonword(lines[i], lines[j])
        if len(lines[i]) - len(w) == 1:
            print(w)

# print (timeit.timeit(stmt=parttwo, number=10))
# print (timeit.timeit(stmt=parttwolin, number = 10))

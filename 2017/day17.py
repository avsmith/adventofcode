#!/usr/bin/env python

from collections import deque


def spin(insert, step):
    spinlock = deque([0])
    for i in range(1, insert + 1):
        spinlock.rotate(-step)
        spinlock.append(i)
    return spinlock


spin1 = spin(2017, 316)
print(spin1[0])
spin2 = spin(50000000, 316)
print(spin2[spin2.index(0) + 1])

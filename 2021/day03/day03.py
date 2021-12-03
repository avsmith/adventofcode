#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()

data = [int(x, 2) for x in input.splitlines()]


def bit_set(list, bit):
    count = 0
    for x in list:
        if x & (1 << bit):
            count += 1
    if count >= len(list)/2:
        return True


gamma = 0
epsilon = 0

for x in range(max(data).bit_length(), 0, -1):
    if bit_set(data, x-1):
        gamma ^= 2**(x-1)
    else:
        epsilon ^= 2**(x-1)

print("Part 1:", gamma*epsilon)


def oxygen(list, bit):
    if bit_set(list, bit):
        new = [x for x in list if x & (1 << bit)]
    else:
        new = [x for x in list if not x & (1 << bit)]
    return(new)


def co2(list, bit):
    if bit_set(list, bit):
        new = [x for x in list if not x & (1 << bit)]
    else:
        new = [x for x in list if x & (1 << bit)]
    return(new)


oxy = [int(x, 2) for x in input.splitlines()]
oxy_pos = max(oxy).bit_length() - 1

while len(oxy) > 1:
    oxy = oxygen(oxy, oxy_pos)
    oxy_pos -= 1

dioxy = [int(x, 2) for x in input.splitlines()]
dioxy_pos = max(dioxy).bit_length() - 1

while len(dioxy) > 1:
    dioxy = co2(dioxy, dioxy_pos)
    dioxy_pos -= 1

print("Part 2:", oxy[0]*dioxy[0])

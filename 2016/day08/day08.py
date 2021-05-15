#!/usr/bin/env python


import os
import sys
import numpy as np


np.set_printoptions(linewidth=120)
a = np.zeros((6, 50), dtype=np.int)

# print(a)
# a[0:2,0:3] = 1
# rect 3x2
# print(a)

# rotate column x=1 by 1
# a[:,1] =np.roll(a[:,1],1)
# print(a)
# rotate row y=0 by 4
# a[0,:] =np.roll(a[0,:],4)
# print(a)
# rotate column x=1 by 1
# a[:,1] =np.roll(a[:,1],1)
# print(a)

# print(np.sum(a))

f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()

for line in input.splitlines():
    items = line.split()
    #    print(line)
    if len(items) == 2:
        wide = int(items[1][: len(items[1]) - 2])
        tall = int(items[1][-1])
        a[0:tall, 0:wide] = 1
    else:

        axis = int(items[2][items[2].find("=") + 1 :])
        amount = int(items[4])
        if items[1] == "row":
            a[axis, :] = np.roll(a[axis, :], amount)
        elif items[1] == "column":
            a[:, axis] = np.roll(a[:, axis], amount)

print("Part 1:", np.sum(a))
print("Part 2: (read it)")
for r in a:
    l = ""
    for i in range(len(r)):
        if r[i] == 0:
            l += " "
        else:
            l += "#"
    print(l)

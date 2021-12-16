#!/usr/bin/env python

import sys
import os

import numpy as np

f = open(os.path.join(sys.path[0], "input15.txt"))
input = f.read()


grid = []

for line in input.splitlines():
    grid.append([int(x) for x in line])

def minCost(cost):
    mincost = np.zeros_like(cost, dtype= 'i')
    cost = np.array(cost)
#    print(mincost)
    for _ in range(3):
        for i in range(1,len(cost)):
            mincost[0,i] = mincost[0,i-1] + cost[0,i]
        for i in range(1, len(cost[0])):
            mincost[i,0] = mincost[i-1,0] + cost[i,0]
        for i in range(1, len(cost[0])):
            for j in range(1, len(cost)):
                mincost[i,j] = min(mincost[i-1,j], mincost[i,j-1]) + cost[i,j]
    return mincost[-1][-1]

print(minCost(grid))

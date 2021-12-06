#!/usr/bin/env python

from collections import defaultdict

test = "3,4,3,1,2"
initial = "5,4,3,5,1,1,2,1,2,1,3,2,3,4,5,1,2,4,3,2,5,1,4,2,1,1,2,5,4,4,4,1,5,4,5,2,1,2,5,5,4,1,3,1,4,2,4,2,5,1,3,5,3,2,3,1,1,4,5,2,4,3,1,5,5,1,3,1,3,2,2,4,1,3,4,3,3,4,1,3,4,3,4,5,2,1,1,1,4,5,5,1,1,3,2,4,1,2,2,2,4,1,2,5,5,1,4,5,2,4,2,1,5,4,1,3,4,1,2,3,1,5,1,3,4,5,4,1,4,3,3,3,5,5,1,1,5,1,5,5,1,5,2,1,5,1,2,3,5,5,1,3,3,1,5,3,4,3,4,3,2,5,2,1,2,5,1,1,1,1,5,1,1,4,3,3,5,1,1,1,4,4,1,3,3,5,5,4,3,2,1,2,2,3,4,1,5,4,3,1,1,5,1,4,2,3,2,2,3,4,1,3,4,1,4,3,4,3,1,3,3,1,1,4,1,1,1,4,5,3,1,1,2,5,2,5,1,5,3,3,1,3,5,5,1,5,4,3,1,5,1,1,5,5,1,1,2,5,5,5,1,1,3,2,2,3,4,5,5,2,5,4,2,1,5,1,4,4,5,4,4,1,2,1,1,2,3,5,5,1,3,1,4,2,3,3,1,4,1,1"

starting = [int(x) for x in initial.split(",")]


def lanternfish_count(start, days=80):
    fish = defaultdict(int)

    for c in starting:
        fish[c] += 1

    for i in range(days):
        newfish = defaultdict(int)
        for j in range(9):
            if (j >= 1 and j <= 6) or j == 8:
                newfish[j-1] = fish[j]
            elif j == 0:
                newfish[6] += fish[0]
                newfish[8] = fish[0]
            elif j == 7:
                newfish[6] += fish[7]
        fish = newfish

    totalfish = 0
    for i in range(9):
        totalfish += fish[i]
    return(totalfish)


print("Part 1:", lanternfish_count(starting))
print("Part 1:", lanternfish_count(starting, 256))

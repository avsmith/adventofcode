#!/usr/bin/env python

import os
import sys
from collections import defaultdict

testdata = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""


f = open(os.path.join(sys.path[0], "input14.txt"))
data = f.read()


class Reindeer:
    def __init__(self, name, speed, endurance, rest):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.rest = rest

    def __repr__(self):
        return f"{self.name}: {self.speed} km/s for {self.endurance} sec, rest {self.rest} sec."


team = list()


def distance_traveled(d, t):
    speed = d.speed
    endurance = d.endurance
    rest = d.rest
    fullcycle = endurance + rest
    complete = t // fullcycle
    remaining = t % fullcycle
    totaltime = complete * speed * endurance + min(endurance, remaining) * speed
    return totaltime


for line in data.splitlines():
    items = line.split(" ")
    deer = Reindeer(items[0], int(items[3]), int(items[6]), int(items[13]))
    team.append(deer)


def furthest(team, time=2503):
    dist = None
    for d in team:
        travelled = distance_traveled(d, time)
        if dist is None or travelled > dist:
            dist = travelled
    return dist


def scoring(team, time=2503):
    scores = [0] * len(team)
    for t in range(1, time + 1):
        positions = list()
        for d in team:
            pos = distance_traveled(d, t)
            positions.append(pos)
        leader = [i for i, x in enumerate(positions) if x == max(positions)]
        for i in leader:
            scores[i] += 1
    return max(scores)


print("Part 1:", furthest(team))
print("Part 2:", scoring(team))

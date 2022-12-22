#!/usr/bin/env python

import os
import sys
import re

f = open(os.path.join(sys.path[0], "input15.txt"))
input = f.read()

test = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Sensor:
    def __init__(self, sx, sy, bx, by, addsensor=False):
        self.sensor = [sx, sy]
        self.beacon = [bx, by]
        self.dist = manhattan(*self.sensor, *self.beacon)
        self.nosensor = []
        if addsensor:
            for xx in range(sx - self.dist, sx + self.dist + 1):
                for yy in range(sy - self.dist, sy + self.dist + 1):
                    if (
                        manhattan(*self.sensor, xx, yy) <= self.dist
                        and manhattan(*self.sensor, xx, yy) != 0
                    ):
                        self.nosensor.append([int(xx), int(yy)])

    def __str__(self):
        return f"Sensor = {self.sensor[0]},{self.sensor[1]}; Beacon = {self.beacon[0]},{self.beacon[1]}; Distance = {self.dist}; Clear  = {self.nosensor}"


sensors = []

for line in test.splitlines():
    sensx, sensy, beacx, beacy = [int(s) for s in re.findall(r"\b\d+\b", line)]
    sensors.append(Sensor(sensx, sensy, beacx, beacy, True))

target = 10
open_sites = set([tuple(x) for s in sensors for x in s.nosensor if x[0] == target])

# sensor_locations = set([tuple(s.sensor) for s in sensors if s.sensor[0] == target])

print(len(open_sites))

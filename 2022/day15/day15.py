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
    def __init__(self, sx, sy, bx, by):
        self.sensor = [sx, sy]
        self.beacon = [bx, by]
        self.dist = manhattan(*self.sensor, *self.beacon)
        self.targets = list()

    def checktarget(self, target):
        sx, sy = self.sensor
        bx, by = self.beacon

        for xx in range(sx - self.dist, sx + self.dist + 1):
            if (
                manhattan(*self.sensor, xx, target) <= self.dist
                and manhattan(*self.sensor, xx, target) != 0
            ):
                self.targets.append([int(xx), int(target)])
            else:
                None

    def __str__(self):
        if self.addsensor:
            return f"Sensor = {self.sensor[0]},{self.sensor[1]}; Beacon = {self.beacon[0]},{self.beacon[1]}; Distance = {self.dist}; Clear  = {self.nosensor}"
        else:
            return f"Sensor = {self.sensor[0]},{self.sensor[1]}; Beacon = {self.beacon[0]},{self.beacon[1]}; Distance = {self.dist}"


sensors = []

target = 10

for line in test.splitlines():
    sensx, sensy, beacx, beacy = [int(s) for s in re.findall(r"\b\d+\b", line)]
    sens = Sensor(sensx, sensy, beacx, beacy)
    sens.checktarget(target)
    sensors.append(sens)

target_sites = set([tuple(x) for s in sensors for x in s.targets if x[1] == target])

sensor_locations = set([tuple(s.sensor) for s in sensors if s.sensor[1] == target])
beacon_locations = set([tuple(s.beacon) for s in sensors if s.beacon[1] == target])

print("Part1:", len(target_sites - sensor_locations - beacon_locations))

# for s in sensors:
#    print(s)
#    print(s.targets)

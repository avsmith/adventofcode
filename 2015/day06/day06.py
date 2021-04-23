#!/usr/bin/env python

import os, sys
import re

f = open(os.path.join(sys.path[0], "input06.txt"))
data = f.read()
txt = data.splitlines()

lights = [[0] * 1000 for _ in range(1000)]
lights2 = [[0] * 1000 for _ in range(1000)]


for instruct in txt:
    m = re.match("(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", instruct)
    (action, x1, y1, x2, y2) = m.groups()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == "toggle":
                lights[x][y] = lights[x][y] ^ 1
                lights2[x][y] += 2
            elif action == "turn on":
                lights[x][y] = 1
                lights2[x][y] += 1
            elif action == "turn off":
                lights[x][y] = 0
                if lights2[x][y] > 0:
                    lights2[x][y] -= 1


def count_lights(l):
    on = 0
    for x in range(1000):
        for y in range(1000):
            on += l[x][y]
    return on


print(count_lights(lights))
print(count_lights(lights2))

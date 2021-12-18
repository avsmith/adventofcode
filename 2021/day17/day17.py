#!/usr/bin/env python

input = "target area: x=240..292, y=-90..-57"


def hit_target(x, y, xmin=240, xmax=292, ymin=-90, ymax=-57):
    xpos = 0
    ypos = 0
    maxy = ypos
    while xpos <= xmax and ypos >= ymin:
        xpos += x
        ypos += y
        if ypos > maxy:
            maxy = ypos
        if xmin <= xpos <= xmax and ymin <= ypos <= ymax:
            return maxy
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        y -= 1
    return None


hits = []

ranges = input[13:].split(", ")
xdata = ranges[0][2:]
xdata = [int(x) for x in xdata.split("..")]
ydata = ranges[1][2:]
ydata = [int(y) for y in ydata.split("..")]

for xvel in range(1, xdata[1] + 1):
    for yvel in range(ydata[0], 100):
        highest = hit_target(xvel, yvel, xdata[0], xdata[1], ydata[0], ydata[1])
        if highest is not None:
            hits.append([xvel, yvel, highest])

print("Part 1:", sorted([x[2] for x in hits])[-1])
print("Part 2:", len(hits))

#!/usr/bin/env python

import os, sys
import re

f = open(os.path.join(sys.path[0], "input05.txt"))
data = f.read()
codes = data.splitlines()


def find_seat(txt):
    row = "0b"
    col = "0b"
    for c in txt:
        if c == "B":
            row += "1"
        elif c == "F":
            row += "0"
        elif c == "R":
            col += "1"
        elif c == "L":
            col += "0"
    return int(row, 2) * 8 + int(col, 2)


max_seat = 0
plane = []

for code in codes:
    seat_id = find_seat(code)
    plane.append(seat_id)
    if seat_id > max_seat:
        max_seat = seat_id

print(max_seat)
print(list(set(list(range(min(plane), max(plane) + 1))) - set(plane))[0])

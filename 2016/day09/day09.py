#!/usr/bin/env python


import os
import sys

f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read().rstrip()


def count_expanded(text, part2=False):
    start = text.find("(")
    if start >= 0:
        xpos = text.find("x")
        end = text.find(")")
        lentarget = int(text[start + 1 : xpos])
        repeats = int(text[xpos + 1 : end])
        remaining = text[end + lentarget + 1 :]
        if part2:
            target = text[end + 1 : end + lentarget + 1]
            lentarget = count_expanded(target, part2)
        nchars = start + lentarget * repeats + count_expanded(remaining, part2)
    else:
        nchars = len(text)
    return nchars


print("Part 1:", count_expanded(input))
print("Part 2:", count_expanded(input, True))

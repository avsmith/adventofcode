#!/usr/bin/env python


import os
import sys

f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read()
input = input.rstrip()


def count_expanded(text, part2=False):
    nchars = 0
    start = text.find("(")
    if start >= 0:
        xpos = text.find("x")
        end = text.find(")")
        chars = int(text[start + 1 : xpos])
        repeats = int(text[xpos + 1 : end])
        remain = text[end + chars + 1 :]
        target = text[end + 1 : end + chars + 1]
        if part2 and target.find(")"):
            chars = count_expanded(target, part2)
        nchars += start + chars * repeats + count_expanded(remain, part2)
        return nchars
    else:
        nchars += len(text)
        return nchars
    return nchars


print("Part 1:", count_expanded(input))
print("Part 2:", count_expanded(input, True))

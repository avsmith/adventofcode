#!/usr/bin/env python


import os
import sys
import re


f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read()

number_re = re.compile("\((\d+)x(\d+)\)")


def expand_text(text):
    nchars = 0
    while len(text) > 0:
        m = number_re.search(text)
        if m is None:
            #            return new + text
            return nchars + len(text)
        else:
            start = m.start()
            chars = m.group(1)
            repeats = m.group(2)
            length = 3 + len(repeats) + len(chars)
            testchars = text[start + int(length) : start + int(length) + int(chars)]
            nchars += len(text[:start] + testchars * int(repeats))
            text = text[start + int(length) + int(chars) :]
    return nchars


print("Part 1:", expand_text(input))

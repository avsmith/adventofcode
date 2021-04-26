#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()


def encode_string(s):
    new = ""
    for c in s:
        if c == '"':
            new += '\\"'
        elif c == "\\":
            new += "\\\\"
        else:
            new += c
    return '"' + new + '"'


length = 0
length2 = 0

for string in input.splitlines():
    decoded_string = bytes(string[1:-1], "ascii").decode("unicode_escape")
    length += len(string) - len(decoded_string)
    decode2 = bytes(string, "ascii").decode("unicode_escape")
    encoded_string = string.replace('"', '\\"')
    encoded_string2 = encode_string(string)
    length2 += len(encoded_string2) - len(string)

print(f"Part 1 answer: {length}")
print(f"Part 2 answer: {length2}")

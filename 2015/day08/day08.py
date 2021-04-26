#!/usr/bin/env python

import os, sys
import numpy as np
import itertools

f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()


length = 0
length2 = 0

for string in input.splitlines():
    decoded_string = bytes(string[1:-1], "ascii").decode("unicode_escape")
    length += len(string) - len(decoded_string)
    decode2 = bytes(string, "ascii").decode("unicode_escape")
    encoded_string = string.encode("ascii", "ignore")
#  print(len(string), len(decoded_string),len(encoded_string))
#  print(string, decoded_string, encoded_string)


print(f"Part 1 answer: {length}")

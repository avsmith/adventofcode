#!/usr/bin/env python3

import os
import sys


def get_digits(text, substitute = False):
	nums = ''.join(c for c in text if c.isdigit())
	return int(nums[0] + nums[-1])

f = open(os.path.join(sys.path[0], "input01.txt"))
input = f.read()

part1 = [get_digits(x, False) for x in input.splitlines()]

print("Part 1:", sum(part1))

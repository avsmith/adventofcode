#!/usr/bin/env python3

import os
import sys

# For part 2, crazy substitute due to overlapping patterns
number_dict = {
	'one': 'o1e',
	'two': 't2o',
	'three': 't3e',
	'four' : 'f4r',
	'five': 'f5e',
	'six': 's6x',
	'seven': 's7n',
	'eight': 'e8t',
	'nine': 'n9e',
}

def replace_words(s):
	for k,v in number_dict.items():
		s = s.replace(k,v)
	return(s)
	
def get_digits(text):
	nums = ''.join(c for c in text if c.isdigit())
	reduced = nums[0] + nums[-1]
	return(int(reduced))

f = open(os.path.join(sys.path[0], "input01.txt"))
input = f.read()

part1 = [get_digits(x) for x in input.splitlines()]
part2 = [get_digits(replace_words(x)) for x in input.splitlines()]

print("Part 1:", sum(part1))
print("Part 2:", sum(part2))

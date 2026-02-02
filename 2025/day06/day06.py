#!/usr/bin/env python3

import math
from pathlib import Path

testdata = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

inputtext = Path("input06.txt").read_text()

matrix = [
	[int(tok) if tok.isdigit() else tok
	 for tok in line.split()]
	for line in inputtext.splitlines()
	if line.strip()
]


transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

value = 0

for form in transposed_matrix:
	if form[-1] == '*':
		value += math.prod(form[0:-1])
	else:
		value += sum(form[0:-1])

print("Part1:",value)

m = inputtext.splitlines()

indices = [i for i, c in enumerate(m[-1]) if c == "*" or c == "+"] 

indices.append(len(m[-1])+1)
digits = len(m)
full_nums = []

for i in range(len(indices[:-1])):
	positions = list(range(indices[i+1]-2, indices[i]-1,-1))
	nums = [''] * (indices[i+1]-indices[i]-1)
	for idx, p in enumerate(positions):
		for j in range(len(m)-1):
			nums[idx] += m[j][p]
	nums = [int(x) if x else 0 for x in nums]
	nums.append(m[-1][indices[i]])
	full_nums.append(nums)

value2 = 0
for form in full_nums:
	if form[-1] == '*':
		value2 += math.prod(form[0:-1])
	else:
		value2 += sum(form[0:-1])
print("Part2:", value2)


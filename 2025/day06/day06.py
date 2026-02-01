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

print(value)
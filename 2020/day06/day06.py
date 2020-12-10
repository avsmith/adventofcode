#!/usr/bin/env python

import os, sys
#import re
import string

letter_set = set(string.ascii_lowercase)


f = open(os.path.join(sys.path[0], 'input06.txt'))
data = f.read()
sets = data.split("\n\n")

size = 0 
size2 = 0
for s in sets:
	dset = set(s)
	size += len(dset.intersection(letter_set))
	
	splits = s.splitlines()
	for x in range(len(splits)):
		if x == 0:
			common_set = set(splits[x])
		else:
			common_set = common_set.intersection(set(splits[x]))
	size2 += len(common_set)	

print(size)
print(size2)	

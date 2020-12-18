#!/usr/bin/env python

import re
import numpy as np

import os, sys

f = open(os.path.join(sys.path[0], 'input14.txt'))
input = f.read()

def set_bit(value, bit):
  return value | (1<<bit)

def clear_bit(value, bit):
  return value & ~(1<<bit)

#input = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
#mem[8] = 11
#mem[7] = 101
#mem[8] = 0
#'''

maskre = re.compile('mask = ([01X]+)')
memre = re.compile("mem\[(\d+)\] = (\d+)")


results = dict()
results2 = dict()

for line in input.splitlines():
  maskmatch = maskre.match(line)
  memmatch = memre.match(line)
  maskloc = {'X':[], '0':[], '1':[]}
  if maskmatch:
    mask = maskmatch.group(1)
    for i in range(len(mask)):
      maskloc[mask[i]].append(i)
    print(maskloc)
  elif memmatch:
    (loc, val) = memmatch.groups()
    v = int(val);
    for i in range(len(mask)):
      if mask[-(i+1)] == '0':
        v = clear_bit(v, i)
      elif mask[-(i+1)] == '1':
        v = set_bit(v, i)
    results[loc] = v
# part 2 loop
#    v2 = int(val)
#    loc2 = int(loc)
#    locations = []
#    for i in range(len(mask)):
#      if mask[-(i+1)] == '1':
#        loc2 = set_bit(loc2, i)
#      elif mask[-(i+1)] == 'X':
#        locations.append(i)
#    print(locations) 


print(np.sum(list(results.values())))
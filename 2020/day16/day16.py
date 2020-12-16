#!/usr/bin/env python

import re
import os, sys

testinput = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''


f = open(os.path.join(sys.path[0], 'input16.txt'))
input = f.read()

(params, ticket, nearby_tix) = input.split("\n\n")

param_set = set()

paramre = re.compile("^[^:]+: (\d+)-(\d+) or (\d+)-(\d+)") 

for param in params.splitlines():
  parammatch = paramre.match(param)
  (x_min, x_max, y_min, y_max) = parammatch.groups()
  param_set.update(range(int(x_min),int(x_max)+1))
  param_set.update(range(int(y_min),int(y_max)+1))
  
ticketre = re.compile("\d+")
ticketnums = [int(t) for t in ticketre.findall(ticket)]

error_rate = 0 
for nearby in nearby_tix.splitlines():
  nearby_nums = [int(t) for t in ticketre.findall(nearby)]
  for near in nearby_nums:
    if near not in param_set:
      error_rate += near

print(error_rate)

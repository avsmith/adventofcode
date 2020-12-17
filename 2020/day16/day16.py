#!/usr/bin/env python

import re
import os, sys
import numpy as np
import itertools

f = open(os.path.join(sys.path[0], 'input16.txt'))
input = f.read()

(params, ticket, nearby_tix) = input.split("\n\n")

param_dict = dict()

paramre = re.compile("^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)") 
departre = re.compile("departure ")

for param in params.splitlines():
  parammatch = paramre.match(param)
  (ticket_category, x_min, x_max, y_min, y_max) = parammatch.groups()
  param_dict[ticket_category] =  list(range(int(x_min),int(x_max)+1)) + list(range(int(y_min),int(y_max)+1))
  
ticketre = re.compile("\d+")
ticketnums = [int(t) for t in ticketre.findall(ticket)]

error_rate = 0 
ticket_rules = [[] for _ in range(len(ticketnums))]

for nearby in nearby_tix.splitlines():
  nearby_nums = [int(t) for t in ticketre.findall(nearby)]
  invalid_nums =  np.setdiff1d(nearby_nums,list(itertools.chain.from_iterable(param_dict.values())))
  if len(invalid_nums) > 0:
    error_rate += sum(invalid_nums)
  else:
    for i in range(len(nearby_nums)):
      possible_values = [list(param_dict.keys())[j] for j, elem in enumerate(list(param_dict.values())) if nearby_nums[i] in elem]
      if len(ticket_rules[i]) == 0:
        ticket_rules[i] = possible_values
      else:
        ticket_rules[i] = list(set(possible_values) & set(ticket_rules[i]))

while any(len(elem) > 1 for elem in ticket_rules):
  determined_values = set(list(itertools.chain.from_iterable([ticket_rules[i] for i, elem in enumerate(ticket_rules) if len(ticket_rules[i]) == 1])))
  for i in range(len(ticket_rules)): 
    if len(ticket_rules[i]) > 1:
      ticket_rules[i] = [rule for rule in ticket_rules[i] if rule not in determined_values]

depart_fields = [i for i, elem in enumerate(ticket_rules) if departre.match(elem[0])]

# Part 1
print(error_rate)
# Part 2
print(np.prod([ticketnums[i] for i in depart_fields]))


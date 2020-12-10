#!/usr/bin/env python

import os, sys
from itertools import  chain, combinations

f = open(os.path.join(sys.path[0], 'input10.txt'))
d = f.read()

jolt_input = [0] + sorted( [int(x) for x in d.splitlines()])


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
  
def legal_set_counts(input_array_set):
  if(len(input_array_set)) <= 2:
    set_count = 1
  else:
    first_item = input_array_set.pop(0)
    last_item = input_array_set.pop()
    possible_subsets = powerset(input_array_set)
    set_count = 0
    for subset in possible_subsets:
      set_count += check_legal_set([first_item] + sorted(list(subset)) + [last_item] )
  return(set_count)

def check_legal_set(input_set):
  for i in range(len(input_set)-1):
    if input_set[i+1] - input_set[i] > 3:
      return False
  return True

def multiplyList(integer_list) :
    # Multiply elements one by one
    result = 1
    for x in integer_list:
         result = result * x 
    return result 

step_counts = dict()

jolt_input_split = []
jolt_subset_by_one = []
for i in range(len(jolt_input)):
  if i == 0 or jolt_input[i] - jolt_input[i-1] == 1:
    jolt_subset_by_one.append(jolt_input[i])
  elif jolt_input[i] - jolt_input[i-1] == 3:
    jolt_input_split.append(jolt_subset_by_one)
    jolt_subset_by_one = [jolt_input[i]]

jolt_input_split.append(jolt_subset_by_one)


for i in range(len(jolt_input)-1):
  jolt_step = jolt_input[i+1]-jolt_input[i]
  if jolt_step in step_counts:
    step_counts[jolt_step] += 1
  else:
    step_counts[jolt_step] = 1

print(f"Answer 1: {step_counts[1]*(step_counts[3]+1)}")

number_legal_sets = [legal_set_counts(x) for x in jolt_input_split]

second_answer = 1
for x in number_legal_sets:
  second_answer *= x

print(f"Answer 2: {second_answer}")

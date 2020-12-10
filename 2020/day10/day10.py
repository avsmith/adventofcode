#!/usr/bin/env python

import os, sys
from itertools import  chain, combinations

f = open(os.path.join(sys.path[0], 'input10.txt'))
d = f.read()

srted = [0] + sorted( [int(x) for x in d.splitlines()])


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
  
def legal_set_counts(candidates):
  if(len(candidates)) <= 2:
    set_count = 1
  else:
    start = candidates.pop(0)
    end = candidates.pop()
    pset = powerset(candidates)
    set_count = 0
    for p in pset:
      set_count += legal_set([start] + sorted(list(p)) + [end] )
#  print(set_count)
  return(set_count)

def legal_set(values):
  for i in range(len(values)-1):
    if values[i+1] - values[i] > 3:
      return False
  return True

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

cnts = dict()

srt_splt = []
tracker = []
for i in range(len(srted)):
  if i == 0 or srted[i] - srted[i-1] == 1:
    tracker.append(srted[i])
  elif srted[i] - srted[i-1] == 3:
    srt_splt.append(tracker)
    tracker = [srted[i]]
srt_splt.append(tracker)


for i in range(len(srted)-1):
  dif = srted[i+1]-srted[i]
  if dif in cnts:
    cnts[dif] += 1
  else:
    cnts[dif] = 1

print(cnts[1]*(cnts[3]+1))

legal_sets = [legal_set_counts(x) for x in srt_splt]
val = 1
for x in legal_sets:
  val *= x
print(val)

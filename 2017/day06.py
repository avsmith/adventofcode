#!/usr/bin/env python

testbanks = [0,2,7,0]
input = '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'

banks = [int(i) for i in input.split()]
#banks = testbanks
def bankkey(keys):
  return('-'.join([str(i) for i in keys]))

def findmax(keys):
  res = dict()
  res['pos'] = 0
  res['max'] = keys[0]
  
  for i in range(1,len(keys)):
    if keys[i] > res['max']:
      res['pos'] = i
      res['max'] = keys[i]
  return(res)

def incbanks(keys):
  maxinfo = findmax(keys)
  keys[maxinfo['pos']] = 0
  pos = (maxinfo['pos'] + 1) % len(keys)
  for i in range(maxinfo['max']):
    keys[pos] += 1
    pos = (pos + 1) % len(keys)
  return(keys)
  
def loop_dist(lst):
  positions = [i for i, x in enumerate(lst) if x == lst[-1]]
  return(positions[1]- positions[0])

seen = [bankkey(banks)]

while len(seen) == len(set(seen)):
  banks = incbanks(banks)
  seen.append(bankkey(banks))  
print('Star1 answer: {}'.format(len(set(seen))))
  
print('Star2 answer: {}'.format(loop_dist(seen)))

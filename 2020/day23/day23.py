#!/usr/bin/env python

from collections import deque


input = '327465189'
#input = '327465189'

cups = [int(x) for x in input]
cups2 = [int(x) for x in input]


#class Node:
#    def __init__(self, val):
#        self.val = val
#        self.next = None


def play_cups(starting, n=100):
  cuptracker = starting
  for i in range(n):
    first = cuptracker[0]
    slice = cuptracker[1:4]
    # Extract as deque for easy rotation
    tail = deque(cuptracker[4:])
    for i in range(first-1,first-(1+len(starting)),-1):
      i = i % 10
      if i == 0:
        continue
      try:
        insert_point = tail.index(i)
        tail.rotate(-insert_point)
        rotated = list(tail.copy())
        inserted = [rotated[0]] + slice + rotated[1:]
        inque = deque(inserted)
        inque.rotate(insert_point)
        newbegin = list(inque.copy())
        break
      except ValueError:
        pass
    cuptracker = newbegin + [first]
  return(cuptracker)





game1 = deque(play_cups(cups))
game1.rotate(-game1.index(1))
game1 = list(game1)
part1 = ''.join([str(x) for x in game1[1:]])
print(part1)

#print(play_cups_part2([int(x) for x in input]))
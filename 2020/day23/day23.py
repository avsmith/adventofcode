#!/usr/bin/env python

from collections import deque

input = '327465189'

cups1 = [int(x) for x in input]
cups2 = [int(x) for x in input]


class Cup:
  def __init__(self, val):
    self.val = val
    self.next = None

def play_cups(starting, n=100):
  cuptracker = starting
  for i in range(n):
    first = cuptracker[0]
    slice = cuptracker[1:4]
    # Extract as deque for easy rotation
    # Probably overdone
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


game1 = deque(play_cups(cups1))
game1.rotate(-game1.index(1))
game1 = list(game1)
part1 = ''.join([str(x) for x in game1[1:]])
print(part1)

# Brute force approach above was WAY too slow for part 2
# Linked lists was the way forward
def play_cups_part2(starting, rounds=int(1e7), size=int(1e6)):
  cups = {}
  for c in range(1, size + 1):
    cups[c] = Cup(c)

  for x, y in zip(starting, starting[1:]):
    cups[x].next = cups[y]

  if len(starting) == size:
    cups[int(starting[-1])].next = cups[int(starting[0])]
  else:
    cups[int(starting[-1])].next = cups[len(starting) + 1]
    for i in range(len(starting) + 1, size):
      cups[i].next = cups[i + 1]
    cups[size].next = cups[int(starting[0])]

  lead = cups[int(starting[0])]
  for _ in range(rounds):
    slice_start = lead.next
    slice_end = lead.next.next.next

    vals = [slice_start.val, slice_start.next.val, slice_end.val]
    goal = lead.val - 1 if lead.val > 1 else size
    while goal in vals:
      goal -= 1
      if goal == 0:
        goal = size

    lead.next = slice_end.next
    slice_end.next = cups[goal].next
    cups[goal].next = slice_start

    lead = lead.next
  return(cups[1].next.val, cups[1].next.next.val)

  for _ in range(int(1e7)):
    rem_start = head.next
    rem_end = head.next.next.next

    vals = [rem_start.val, rem_start.next.val, rem_end.val]
    goal = head.val - 1 if head.val > 1 else N
    while goal in vals:
      goal -= 1
      if goal == 0:
        goal = N

    head.next = rem_end.next
    rem_end.next = nodes[goal].next
    nodes[goal].next = rem_start

    head = head.next

  a, b = nodes[1].next.val, nodes[1].next.next.val


next, nextnext = play_cups_part2([int(x) for x in input])

part2 = next*nextnext
print(part2)
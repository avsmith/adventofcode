#!/usr/bin/env python

import numpy as np

import os, sys

f = open(os.path.join(sys.path[0], 'input11.txt'))
input = f.read()

seatplan = []

for line in input.splitlines():
  # Convention: Empty seat is -1, Floor is 0, Occupied seat is 1
  # Odd convention perhaps
  row = [-1 if x == 'L' else 0 for x in line ]
  seatplan.append(row)

seatplan= np.array(seatplan)

max_r = len(seatplan)
max_c = len(seatplan[0])

def occupied_neighbors(i, j, seatplan, max_dist=1):
  ones = 0
  curstate = seatplan[i,j]
# Move in all 8 directions
  for x, y in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
    try:
      for d in range(1,max_dist+1):
        di = i+x*d
        dj = j+y*d
        # Prevent looping to other side
        if di < 0 or dj < 0:
          continue
        elif seatplan[di][dj] == 0:
          continue
        else:
          if seatplan[di][dj] == 1:
            ones +=1
          break
    except IndexError: 
        pass
  return(ones)

def change_seats(seatplan, max_dist=1, max_viewed_seats=4):
  seatchart = seatplan.copy()
  standup = []
  sitdown = []
  # Checking all possible in grid
  # Note: only checking spots with seats didn't speed
  for r in range(max_r):
    for c in range(max_c):
      if seatchart[r][c] != 0:
        occupied = occupied_neighbors(r, c, seatchart, max_dist)
        if seatchart[r][c] == -1 and occupied == 0:
          sitdown.append([r,c])
        elif seatchart[r][c] == 1 and occupied >= max_viewed_seats:
          standup.append([r,c])
  for seat in sitdown:
    seatchart[seat[0]][seat[1]] = 1
  for seat in standup:
    seatchart[seat[0]][seat[1]] = -1
  return(seatchart)

def find_final_seats(seatplan, max_dist=1, max_viewed_seats=4):
  curseats = seatplan.copy()
  nextseats = change_seats(seatplan, max_dist, max_viewed_seats)
  while not np.array_equal(curseats, nextseats):
    curseats = nextseats.copy()
    nextseats = change_seats(curseats, max_dist, max_viewed_seats)
  return(len(np.where(curseats==1)[0]))

part1 = find_final_seats(seatplan)
print(part1)
part2 = find_final_seats(seatplan, len(seatplan[0]), 5)
print(part2)


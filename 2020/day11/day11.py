#!/usr/bin/env python

import numpy as np

input = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''

import os, sys

f = open(os.path.join(sys.path[0], 'input11.txt'))
input = f.read()

seatplan = []

for line in input.splitlines():
  row = [-1 if x == 'L' else 0 for x in line ]
  seatplan.append(row)

seatplan= np.array(seatplan)
#seatlocs = np.asarray(np.where(np.array(seatplan)!=0)).T.tolist()

#print(seatlocs)



max_r = len(seatplan)
max_c = len(seatplan[0])

def occupied_neighbors(i, j, seatplan):
  curstate = seatplan[i,j]
  neighbors = seatplan[max(i-1,0):min(i+2,max_r), max(j-1,0):min(j+2,max_c)]
  ones = len(np.where(neighbors==1)[0])
  if curstate == 1:
    return(ones - 1)
  else:
    return(ones)


def change_seats(seatplan):
  seatchart = seatplan.copy()
  standup = []
  sitdown = []
  for r in range(max_r):
    for c in range(max_c):
      if seatchart[r][c] != 0:
        occupied = occupied_neighbors(r,c, seatchart)
        if seatchart[r][c] == -1 and occupied == 0:
          sitdown.append([r,c])
        elif seatchart[r][c] == 1 and occupied >= 4:
          standup.append([r,c])
  for seat in sitdown:
    seatchart[seat[0]][seat[1]] = 1
  for seat in standup:
    seatchart[seat[0]][seat[1]] = -1
  return(seatchart)


def find_final_seats(seatplan):
  curseats = seatplan.copy()
  nextseats = change_seats(seatplan)
  while not np.array_equal(curseats, nextseats):
    curseats = nextseats.copy()
    nextseats = change_seats(curseats)
  return(len(np.where(curseats==1)[0]))

part1 = find_final_seats(seatplan)
print(part1)
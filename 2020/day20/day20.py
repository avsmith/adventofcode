#!/usr/bin/env python

import os, sys
import numpy as np
from itertools import chain
from collections import deque
import re
import copy


def reverse_bits(num):
  return(int('0b' + format(num, '#012b')[2:][::-1],2))

def rotate_list(l,n):
  return(l[-n:] + l[:-n]) 

def corner_details(tilenum, orient):
  tile_sides = copy.deepcopy(tile_bag[tilenum][orient])
  for i in range(len(tile_sides)):
    possible = rotate_list(tile_sides, i)
    if side_counts[possible[0]] ==  1 and side_counts[possible[3]] == 1:
      tile_text = tile_print(tile_bag[tilenum]['tile'], orient, -i)
      return([[tilenum], possible, [i], [orient],tile_text])
  raise Exeception("Not possible") 

def find_tile(searchnum, sourcetile, desired_side):
  searchnum = reverse_bits(searchnum)
  for tilenum in tile_bag:
    if tilenum == sourcetile:
      continue
    else:
      for orient in ['counter','clock']:
        if searchnum in set(tile_bag[tilenum][orient]):
          tile_sides = copy.deepcopy(tile_bag[tilenum][orient])
          for i in range(len(tile_sides)):
            possible = rotate_list(tile_sides,i)
            if possible[desired_side] == searchnum:
              tile_text = tile_print(tile_bag[tilenum]['tile'], orient, -i)
              return([[tilenum], possible, [i], [orient],tile_text])
  raise Exception("Not possible")

def tile_print(tile, orient, rotate):
  if orient == 'clock':
    reoriented_tile = np.rot90(tile,rotate)
  elif orient == 'counter':
    reoriented_tile = np.rot90(np.transpose(tile),rotate)
  ret = list(map(''.join, reoriented_tile[1:-1,1:-1]))
  return(ret)

f = open(os.path.join(sys.path[0], 'input20.txt'))
input = f.read()

tiles = input.split('\n\n')
tile_bag = dict()

for tile in tiles:
  lines = tile.splitlines()
  tilenum = lines[0][5:9]
  s1 = lines[1].replace('#','1').replace('.','0')
  s1 = int('0b'+s1, 2)
  s2 = ''.join([x[9] for x in lines[1:]]).replace('#','1').replace('.','0')
  s2 = int('0b'+ s2, 2)
  s3 = lines[10][::-1].replace('#','1').replace('.','0')
  s3 = int('0b'+ s3, 2)
  s4 = ''.join([x[0] for x in lines[1:]])[::-1].replace('#','1').replace('.','0')
  s4 = int('0b'+ s4, 2)
  clockwise = [s1,s2,s3,s4]
  counter = [reverse_bits(x) for x in reversed(clockwise)]
  tile_bag[tilenum] = {'clock': clockwise, 'counter': counter}
  t = np.array([list(word) for word in lines[1:]])
  tile_bag[tilenum]['tile'] = t

side_counts = dict()

for tilenum, tile in tile_bag.items():
  for x in tile['clock']:
    if x in side_counts.keys():
      side_counts[x] += 1
      side_counts[reverse_bits(x)] += 1
    else:
      side_counts[x] = 1
      side_counts[reverse_bits(x)] = 1

for tilenum in tile_bag:
  if len([side_counts[x] for x in tile_bag[tilenum]['clock'] if side_counts[x]==1]) == 2:
    tile_bag[tilenum]['type'] = 'corner'
  elif len([side_counts[x] for x in tile_bag[tilenum]['clock'] if side_counts[x]==1]) == 1:
    tile_bag[tilenum]['type'] = 'side'
  elif len([side_counts[x] for x in tile_bag[tilenum]['clock'] if side_counts[x]==1]) == 0:
    tile_bag[tilenum]['type'] = 'middle'
  for num in tile_bag[tilenum]['clock']:
    if num == reverse_bits(num):
      print(f"Tile {tilenum} has ambigous side")

corner_tiles = [int(x) for x in tile_bag if tile_bag[x]['type']=='corner']

print(np.prod(corner_tiles))

testcornernum = '1951'
cornernum = str(corner_tiles[0])
orient = 'counter'
side_size = int(len(tile_bag)**0.5)
all_tiles = []
tile_text = []


for i in range(side_size):
  for j in range(side_size):
    if i == 0 and j == 0:
      current_tile = corner_details(cornernum, orient)
      all_tiles.append(current_tile)
      tile_text = current_tile[4]
    else:
      if j == 0:
        pos = (i-1)*side_size
        current_tile= find_tile(all_tiles[pos][1][2], all_tiles[pos][0][0], 0)
        all_tiles.append(current_tile)
        current_tile_text = current_tile[4]
        tile_text.extend(current_tile_text)
      else:
        pos = i*side_size + j 
        current_tile = find_tile(all_tiles[pos-1][1][1],all_tiles[pos-1][0][0],3)
        all_tiles.append(current_tile)
        current_tile_text = current_tile[4]
        rows = len(current_tile_text)
        for k in range(rows):
          tile_text[k + i*(rows)] = tile_text[k + i*(rows)] + current_tile_text[k]

#print('\n'.join(tile_text))
mon1 = '..................#.'
monstre1 = re.compile(mon1)
mon2 = '#....##....##....###'
monstre2 = re.compile(mon2)
mon3 = '.#..#..#..#..#..#...'
monstre3 = re.compile(mon3)
monster = '\n'.join([mon1, mon2, mon3])
print(monster)

count = 0;
for i in range(4):
  t = np.array([list(word) for word in tile_text])
  tr = list(map(''.join,np.rot90(t,i)))
  for j in range(1,len(tr)-1):
    for match in monstre2.finditer(tr[j]):
      s = match.start()
      e = match.end()
#      print ('String match "%s" at %d:%d' % (tr[j][s:e], s, e))
      if monstre1.fullmatch(tr[j-1],s,e) and monstre3.fullmatch(tr[j+1],s,e):
        count += 1
  tt = list(map(''.join,np.rot90(np.transpose(t),i)))
  for j in range(1,len(tt)-1):
    for match in monstre2.finditer(tr[j]):
      s = match.start()
      e = match.end()
#      print ('String match "%s" at %d:%d' % (tr[j][s:e], s, e))
      if monstre1.fullmatch(tt[j-1],s,e) and monstre3.fullmatch(tt[j+1],s,e):
        count += 1

t = np.array([list(word) for word in tile_text])

tr = list(map(''.join,np.rot90(t,3)))
trj = '\n'.join(tr)
print(trj.count('#')-count*monster.count('#'))


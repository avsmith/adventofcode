#!/usr/bin/env python

import os, sys
import numpy as np

def reverse_bits(num):
  return(int('0b' + format(num, '#012b')[2:][::-1],2))

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

print(np.prod([int(x) for x in tile_bag if tile_bag[x]['type']=='corner']))


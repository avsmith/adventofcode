#!/usr/bin/env python

import re
import os, sys
from collections import defaultdict

movere = re.compile(r'(e|se|sw|w|nw|ne)')

testinput = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
'''

f = open(os.path.join(sys.path[0], 'input24.txt'))
input = f.read()

starttiles = defaultdict(lambda:1)

for line in input.splitlines():
  pos = 0+0j
  moves = movere.findall(line)
  for move in moves:
    if move == 'e':
      pos += 1
    elif move == 'se':
      pos += 1-1j
    elif move == 'sw':
      pos += 0-1j
    elif move == 'w':
      pos += -1
    elif move == 'nw':
      pos += -1+1j
    elif move == 'ne':
      pos += 1j
  starttiles[pos] *= -1


print(abs(sum([x for x in starttiles.values() if x == -1 ])))

#for part2

dirs = [1, 1-1j, 0-1j, -1, -1+1j, 1j]
seedtiles = [pos for pos, x in starttiles.items() if x == -1 ]


def find_neighbors(pos):
  neighbors = []
  for dir in dirs:
    neighbors.append(pos + dir)
  return(neighbors)

def flip_tiles(positions,n):
  for i in range(n):
    checktiles = set(positions)
    newtiles = []
    for pos in set(positions):
      checktiles.update(find_neighbors(pos))
    for tile in set(checktiles):
      blacks = [pos for pos in find_neighbors(tile) if pos in set(positions)]
      if tile in set(positions) and len(blacks) > 0 and len(blacks) < 3:
        newtiles.append(tile)
      elif tile not in set(positions) and len(blacks) == 2:
        newtiles.append(tile)
    print(i+1, len(newtiles))
    positions=newtiles
    
  return(positions)

r10 = flip_tiles(seedtiles, 100)
print(len(r10))

#print(len(flip_tiles(seedtiles)))
  
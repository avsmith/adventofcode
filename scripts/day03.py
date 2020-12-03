#!/usr/bin/env python

def reverse(string): 
  string = string[::-1] 
  return string 

f = open("data/input03.txt")
data = f.read()

testdata = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''

offset = 3

orig = data.splitlines()
length = len(orig[0])
array = [int(reverse(s.replace('#','1').replace('.','0')),2) for s in orig]

trees = 0 

def trees_hit(slope ,right = 3, down = 1, debug = False):
  trees = 0
  for y in range(0,len(slope),down):
    x = (y//down * right) % length 
    pos = slope[y] >> x
    trees +=  pos&1==1
    if(debug):
      line = orig[y]
      if line[x] == '#':
        newline = line[:x] + 'X' + line[x + 1:]
      else:
        newline = line[:x] + 'O' + line[x + 1:]
      print(line, newline)
  return(trees)

print("Part 1 answer:", trees_hit(array))
print("Part 2 answer:", trees_hit(array,1,1)* trees_hit(array,3,1) * trees_hit(array,5,1)* trees_hit(array,7,1)* trees_hit(array,1,2))



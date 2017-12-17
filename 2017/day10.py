#!/usr/bin/env python


sequence = [157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30]

def intseq(x):
  return [i for i in range(x)]


def subrev(x, n, pos):
  if(n + pos > len(x)):
    toreverse = x[pos:] + x[:n - (len(x)-pos)]
    reversed = toreverse[::-1]
    x = reversed[len(x)-pos:] + x[n - (len(x)-pos):pos] + reversed[:len(x)-pos]
  else:
    x = x[:pos] + x[pos:pos+n:][::-1] + x[pos+n:]
  return x

def checksum(x):
  return x[0] * x[1]

data = intseq(256)
cursor = 0 

for i in range(len(sequence)):
  length = int(sequence[i])
  skip = length + i
  data = subrev(data
  , length, cursor)
  cursor = (skip+cursor) % len(data)


print("Star 1 checksum: {}".format(checksum(data)))



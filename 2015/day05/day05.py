#!/usr/bin/env python

import os, sys
import re

f = open(os.path.join(sys.path[0], 'input05.txt'))
data = f.read()
kids = data.splitlines()

vowels = list('aeiou')
txtre = re.compile("(ab|cd|pq|xy)")

def three_vowels(s):
  v = 0
  for c in s:
    if c in vowels:
      v += 1
    if v >= 3:
      return 1
  return 0

def bad_text(s):
  m = txtre.search(s)
  if type(m) is type(None):
    return 1
  return 0

def duplicate_char(s):
  for i in range(1, len(s)):
    if s[i-1] == s[i]:
      return 1
  return 0

def repeated_pairs(s):
  for i in range(len(s)-3):
    pair = s[i:i+2]
    target = s[i+2:]
    m = re.search(pair, target)
    if type(m) is not type(None):
      return 1
  return 0

def spaced_letters(s):
  for i in range(len(s)-2):
    if s[i] == s[i+2]:
      return 1
  return(0)

nice = 0 
nice2 = 0

for t in kids:
  if spaced_letters(t) and repeated_pairs(t):
    nice2 += 1
  if not three_vowels(t):
    continue
  if not bad_text(t):
    continue
  if not duplicate_char(t):
    continue
  nice += 1
  
print(nice, nice2)

#!/usr/bin/env python

f = open('/Users/albert/Documents/Programming/gitwork/adventOfCode/2017/day09.txt','r')

text = f.read()

TESTDATA = '''\
{}
{{{}}}
{{},{}}
{{{},{},{{}}}}
{<a>,<a>,<a>,<a>}
{{<ab>},{<ab>},{<ab>},{<ab>}}
{{<!!>},{<!!>},{<!!>},{<!!>}},
{{<a!>},{<a!>},{<a!>},{<ab>}}
'''

import re

def bookmark():
  return False

# Match exclamation marks and following
p_exclaim = re.compile('!.')
# Match all characters between pairs of < and >
p_bracket = re.compile('<[^>]{0,}>')
# Match all commas
p_commas = re.compile(',{1,}')

cleaned = p_commas.sub('',p_bracket.sub('',p_exclaim.sub('',text)))

curscore = 1
runningscore = 0

split_cleaned = list(cleaned)

for i in range(len(split_cleaned)):
  curchar = split_cleaned[i]
  if curchar == '{':
    runningscore += curscore
    curscore += 1
  if curchar == '}':
    curscore -= 1
    
print("Answer star 1: {}".format(runningscore))
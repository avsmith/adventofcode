#!/usr/bin/env python

import os, sys
import pprint


f = open(os.path.join(sys.path[0], 'input08.txt'))
input = f.read()

testinput = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''

tracking = []

for rule in testinput.splitlines():
  (action, amount) = rule.split(' ')
  tracking.append({'action': action, 'amount': int(amount), 'visited': False})



def hand_held(tracker, loop=True):
  pos = 0;
  acc = 0
#  if loop is not True:
#    print('here we go')
  while True:
#    print(acc, tracker[pos])
    if loop is True and tracker[pos]['visited'] is True:
      return(acc)
    elif tracker[pos]['visited'] is True:
      raise RecursionError("Program in infinite loop")
    else:
      tracker[pos]['visited'] = True
      if tracker[pos]['action'] == 'jmp':
        pos += tracker[pos]['amount']
      elif tracker[pos]['action'] == 'acc':
        acc += tracker[pos]['amount']
        pos += 1
      elif  tracker[pos]['action'] == 'nop':
        pos += 1
      else:
        print('ERROR')

def fix_code(t):
  pprint.pprint(t)
  print('\n')
  for i in range(len(t)):
    print( t[i]['action'])
    if t[i]['action'] == 'jmp':
      t[i]['action'] = 'nop'
      pprint.pprint(t)
      print('\n')
      try:
        return(hand_held(t, False))
      except RecursionError:
        t[i]['action'] = 'jmp'
    elif t[i]['action'] == 'nop':
      t[i]['action'] = 'jmp'
      pprint.pprint(t)
      print('\n')
      try:
        return(hand_held(t, False))
      except RecursionError:
        t[i]['action'] = 'nop'

print(hand_held(tracking))
#print(fix_code(tracking))

#!/usr/bin/env python

import pyparsing
import os, sys

f = open(os.path.join(sys.path[0], 'input18.txt'))
input = f.read()


thecontent = pyparsing.Word(pyparsing.alphanums) | '*' | '+'
parens     = pyparsing.nestedExpr( '(', ')')

#res = parens.parseString("(5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)))")
#res = parens.parseString("(2 * 3 + (4 * 5))")
res = parens.parseString("(((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2)")
#res = parens.parseString("(5 + (8 * 3 + 9 + 3 * 4 * 3))")
print(res.asList())

def recursive_walk(l, curval=0, operand= '+'):
  for item in list(l):
    if isinstance(item, pyparsing.ParseResults):
      returnval = recursive_walk(item, curval=0)
      operation = f"{curval} {operand} {returnval}"
      curval = eval(operation)
    else:
      if item == '+':
#        print('plus')
        operand = '+'
      elif item == '*':
#        print('times')
        operand = '*'
      else:
        operation = f"{curval} {operand} {item}"
        curval = eval(operation)
  return(curval)

total = 0

for line in input.splitlines():
  parsed = parens.parseString('('+line+')')
  result = recursive_walk(parsed)
#  print(line, result)
  total += result

print(total)

from pyparsing import *
integer = pyparsing_common.signed_integer
varname = pyparsing_common.identifier 
arith_expr = infixNotation(integer | varname,
  [
  ('-', 1, opAssoc.RIGHT),
  (oneOf('+ -'), 2, opAssoc.LEFT),
  (oneOf('* /'), 2, opAssoc.LEFT),
  ])

arith_expr.runTests('''
  5+3*6
  (5+3)*6
  -2--11
  ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
  ''', fullDump=False)
RESULT = arith_expr.parseString('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2').asList()
print type(RESULT)
from pprint import pprint
pprint(RESULT)

#!/usr/bin/env python

import pyparsing
import os, sys

f = open(os.path.join(sys.path[0], 'input18.txt'))
input = f.read()

def recursive_math(l, curval=0, operand= '+'):
  for item in list(l):
    if isinstance(item, pyparsing.ParseResults):
      returnval = recursive_math(item)
      operation = f"{curval} {operand} {returnval}"
      curval = eval(operation)
    else:
      if item in ('+','*'):
        operand = item
      else:
        operation = f"{curval} {operand} {item}"
        curval = eval(operation)
  return(curval)

# Set up for part 1
parens = pyparsing.nestedExpr()

# Set up parsing for part 2
# Override precedence!
integer = pyparsing.pyparsing_common.signed_integer
arith_expr = pyparsing.infixNotation(integer,
  [
  ('-', 1, pyparsing.opAssoc.RIGHT),
  (pyparsing.oneOf('+ -'), 2, pyparsing.opAssoc.LEFT),
  (pyparsing.oneOf('* /'), 2, pyparsing.opAssoc.LEFT),
  ])

part1 = 0
part2 = 0

for line in input.splitlines():
  parsed1 = parens.parseString('('+line+')')
  result1 = recursive_math(parsed1)
  part1 += result1
  parsed2 = arith_expr.parseString(line)
  result2 = recursive_math(parsed2)
  part2 += result2

print(part1)
print(part2)

#!/usr/bin/env python

import hashlib
import re

inkey = 'yzbqklnj'

def mine_hash(code, num=1, leadzeros=5):
  hashre = re.compile(rf"^[0]{{{leadzeros},}}")

  while True:
    codenum = code + str(num)
    res = hashlib.md5(codenum.encode())
    result = res.hexdigest()
    if hashre.match(result):
      return(str(num), res.hexdigest())
    num += 1

print(mine_hash(inkey))
print(mine_hash(inkey,leadzeros=6))

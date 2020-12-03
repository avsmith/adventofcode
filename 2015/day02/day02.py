#!/usr/bin/env python

import os, sys
import re

f = open(os.path.join(sys.path[0], 'input02.txt'))
data = f.read()

array = data.splitlines()

paper = 0 
ribbon = 0 

for txt in array:
   m = re.match(r"(\d+)x(\d+)x(\d+)",txt)
   dims = [int(x) for x in m.groups()]
   dims.sort()
   paper += 3*dims[0]*dims[1] + 2*dims[0]*dims[2] + 2*dims[1]*dims[2] 
   ribbon += 2*(dims[0]+dims[1]) + dims[0]*dims[1]*dims[2]
   
print("Paper needed:", paper)
print("Ribbon needed:", ribbon)

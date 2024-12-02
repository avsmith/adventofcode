#!/usr/bin/env python

import os
import sys
import numpy as np

f = open(os.path.join(sys.path[0], "input01.txt"))
data = f.read()

datai = [[int(i) for i in x.split()] for x in data.splitlines()]


print(datai)
#print(datai[0,])
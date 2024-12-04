#!/usr/bin/env python

import os
import sys
import pandas as pd
import numpy as np

df = pd.read_csv(os.path.join(sys.path[0], "input01.txt"), names=['col1','col2'], sep='\s+')


for col in df:
    df[col] = df[col].sort_values(ignore_index=True)

df['abs'] = np.abs(df['col1']-df['col2'])

ans1 = sum(df['abs'])
print(f"Part 1 answer: {ans1}")

# Based on https://stackoverflow.com/questions/67169854/how-to-better-count-occurrences-of-a-list-in-another-list-and-then-list-the-resu

count_arr = np.bincount(df['col2'])
df['count'] = [count_arr[x] for x in df['col1']]
df['score'] = df['col1']*df['count']

ans2 = sum(df['score'])
print(f"Part 2 answer: {ans2}")
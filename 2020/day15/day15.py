#!/usr/bin/env python

input = '1,0,16,5,17,4'
values = [int(x) for x in input.split(',')]
count_dict = {}

pos = 0

for val in values:
  pos += 1
  count_dict[val] = {"pos": pos}

next_num = 0

while pos < 30000000:
  pos += 1
  if pos == 2020 or pos == 30000000:
    print(f"Turn: {pos} Number: {next_num}")
  if next_num in count_dict.keys():
    last_pos = count_dict[next_num]['pos']
#    print(last_pos, count_dict)
    
    count_dict[next_num] = {'pos': pos }
    next_num = pos - last_pos
  else:
    count_dict[next_num] ={"pos": pos}
    next_num = 0

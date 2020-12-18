#!/usr/bin/env python

time = int('1014511')
buses= '17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'


part1 = [int(x) for x in buses.split(',') if x != 'x']

wait = time
first_bus = 0

for bus in part1:
  bus_wait = bus - time % bus
  if bus_wait < wait:
    wait = bus_wait
    first_bus = bus

print(first_bus * wait)

part2 = [(i, int(x)) for i, x in enumerate(buses.split(',')) if x != 'x']

def find_time(indata):
  time, step = 0, 1
  for mins, bus_id in indata:
    while (time + mins) % bus_id != 0:
      time += step
    step *= bus_id
  return(time)

print(find_time(part2))
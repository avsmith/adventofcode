#!/usr/bin/env python

input = "1,0,16,5,17,4"
values = [int(x) for x in input.split(",")]
count_dict = {}

turn = 0

for val in values:
    turn += 1
    count_dict[val] = {"turn": turn}

next_num = 0

while turn < 30000000:
    turn += 1
    if turn == 2020 or turn == 30000000:
        print(f"Turn: {turn} Number: {next_num}")
    if next_num in count_dict.keys():
        last_turn = count_dict[next_num]["turn"]
        count_dict[next_num] = {"turn": turn}
        next_num = turn - last_turn
    else:
        count_dict[next_num] = {"turn": turn}
        next_num = 0

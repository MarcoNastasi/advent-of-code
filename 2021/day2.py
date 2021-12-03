#!/usr/bin/env python3

# Part 1

data = []
with open("day2_input.txt") as input:
    for line in input:
       linelist = line.split()
       data.append({"direction" : linelist[0], "value" : int(linelist[1])})

horizontal = 0
depth = 0

for entry in data:
    if entry["direction"] == "forward":
        horizontal = horizontal + entry["value"]
    elif entry["direction"] == "down":
        depth = depth + entry["value"]
    else:
        depth = depth - entry["value"]

print(depth*horizontal)

# Part 2
horizontal = 0
depth = 0
aim = 0

for entry in data:
    if entry["direction"] == "forward":
        horizontal = horizontal + entry["value"]
        depth = depth + aim * entry["value"]
    elif entry["direction"] == "down":
        aim = aim + entry["value"]
    else:
        aim = aim - entry["value"]

print(horizontal * depth)
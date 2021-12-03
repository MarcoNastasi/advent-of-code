#!/usr/bin/env python3

# Part 1

with open ('day1_input.txt') as input:
    report = input.read().splitlines()
counter = 0
for index, entry in enumerate(report):
    if int(entry) > int(report[index-1]) and index>0:
        counter = counter+1
print(f"The result for part 1 is: {counter}")

sumlist = []
for index, entry in enumerate(report):
    if index > 0 and index < len(report) -1:
        sum = int(report[index-1]) + int(entry) + int(report[index+1])
        sumlist.append(sum)

counter = 0
for index, entry in enumerate(sumlist):
    if int(entry) > int(sumlist[index-1]) and index>0:
        counter = counter+1
print(f"The result for part 2 is: {counter}")

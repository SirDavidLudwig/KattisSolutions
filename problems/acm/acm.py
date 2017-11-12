#!/usr/bin/python3
import re
import sys

attempts = {}
solved = []

total = 0

for line in sys.stdin:
    parts = line.strip().split(" ")
    if parts[0] == "-1":
        break
    if parts[1] in attempts:
        attempts[parts[1]] += 20
    else:
        attempts[parts[1]] = 0
    if parts[2] == "right":
        total += int(parts[0])
        solved.append(parts[1])

for p in solved:
    total += attempts[p]

print(len(solved), total)

from math import *
import sys

n = int(sys.stdin.readline())

printDays = 1
minDays = n
newMinDays = ceil(n / (2**printDays) + printDays)
while newMinDays < minDays:
	minDays = newMinDays
	printDays += 1
	newMinDays = ceil(n / (2**printDays) + printDays)

print(minDays)

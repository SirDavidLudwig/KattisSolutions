from math import factorial as fac
import sys

for line in sys.stdin:
	charSet = {}
	duplicates = 0
	for char in line.strip():
		if char in charSet:
			charSet[char] += 1
		else:
			charSet[char] = 1
	den = 1
	for char in charSet:
		den *= fac(charSet[char])
	print(fac(len(line)-1)//den)

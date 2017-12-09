from itertools import permutations
import sys

a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

minValues = [500, 500, 500]
minLeftover = sum(minValues)

for x in (a, b, c):
	for y in (i, j, k):
		li = a - x*i/y
		lj = b - x*j/y
		lk = c - x*k/y
		if li >= 0 and lj >= 0 and lk >= 0 and li+lj+lk < minLeftover:
			minValues = [li, lj, lk]
			minLeftover = li+lj+lk
print("%0.4f %0.4f %0.4f" % tuple(minValues))

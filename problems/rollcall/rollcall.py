import sys

names = {}
nameCount = {}

for name in sys.stdin:
	first, last = name.split()
	if last not in names:
		names[last] = []
	if first not in nameCount:
		nameCount[first] = 0
	names[last].append(first)
	nameCount[first] += 1

for lastName in sorted(names.keys()):
	for firstName in sorted(names[lastName]):
		print(firstName + ((" " + lastName) if nameCount[firstName] > 1 else ""))

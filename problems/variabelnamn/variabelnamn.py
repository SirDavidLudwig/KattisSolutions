import sys

variables = set()
start = {}

for x in range(int(sys.stdin.readline())):
	x = int(sys.stdin.readline())
	i = start.get(x, x)
	while i in variables:
		i += x
	start[x] = i + x
	variables.add(i)
	print(i)

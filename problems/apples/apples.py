import sys

r, c = map(int, sys.stdin.readline().split())

apples = [0]*c
groupIndex = [0]*c
groups = [[] for i in range(c)]

for i in range(r):
	line = sys.stdin.readline()
	for j in range(c):
		if line[j] == 'a':
			apples[j] += 1
		if line[j] == '#':
			groups[j].append((apples[j], i))
			apples[j] = 0
for j in range(c):
	groups[j].append((apples[j], r))

for i in range(r):
	for j in range(c):
		if i == groups[j][groupIndex[j]][1]:
			print('#', end="")
			groupIndex[j] += 1
		else:
			g = groups[j][groupIndex[j]]
			print("a" if i >= g[1]-g[0] else '.', end="")
	print("")

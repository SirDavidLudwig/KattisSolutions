import sys

r, c = map(int, sys.stdin.readline().split())

park = [0, 0, 0, 0, 0]
m = []
m.append(sys.stdin.readline().strip())
for i in range(1, r):
	m.append(sys.stdin.readline().strip())
	for j in range(1, c):
		s = m[i-1][j-1:j+1] + m[i][j-1:j+1]
		if '#' not in s:
			park[s.count('X')] += 1
for i in park:
	print(i)

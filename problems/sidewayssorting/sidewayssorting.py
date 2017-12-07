import sys

r, c = map(int, input().split())
while r and c:
	lines = [input().strip() for i in range(r)]
	rotatedLines = []
	for i in range(c):
		rotatedLines.append("".join([lines[j][i] for j in range(r)]))
	rotatedLines.sort(key=lambda s: s.lower())
	for i in range(r):
		print("".join([rotatedLines[j][i] for j in range(c)]))
	print()
	r, c = map(int, input().split())

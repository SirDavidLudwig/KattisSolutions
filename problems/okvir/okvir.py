import sys

def printBorder(width, height, offset, newLine = True):
	for i in range(offset, height+offset):
		for j in range(width):
			print(end=charMap[(j+i)&1])
		if i < height+offset-1:
			print()
	if newLine:
		print()

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())
charMap = ['#', '.']
printBorder(l+n+r, u, 0, True)
for i in range(u, m+u):
	printBorder(l, 1, i, False)
	print(end=input().strip())
	printBorder(r, 1, i+l+n, True)
printBorder(l+n+r, d, m+u, False)

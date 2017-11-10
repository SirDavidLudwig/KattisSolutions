import sys

line = sys.stdin.readline().strip()

n = len(line)
size = 2**n
x = y = 0

for i in range(n):
	size /= 2
	x += size * (int(line[i])&1)
	y += size * (int(line[i]) > 1)

print(n, int(x), int(y))

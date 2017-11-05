import sys

n = int(sys.stdin.readline())
s = 1
while n != 0:
	print("SET", s)
	result = [0]*n
	for i in range(n//2):
		result[i] = sys.stdin.readline().strip()
		result[n-1-i] = sys.stdin.readline().strip()
	if n & 1:
		result[n//2] = sys.stdin.readline().strip()
	n = int(sys.stdin.readline())
	s += 1
	for line in result:
		print(line)

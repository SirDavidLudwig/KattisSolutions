import sys

for i in range(int(sys.stdin.readline())):
	result = -1
	n = int(sys.stdin.readline())
	values = sorted(list(map(int, sys.stdin.readline().split(' '))))
	for j in range(1, n, 2):
		if values[j-1] != values[j]:
			result = values[j-1]
			break
	print("Case #" + str(i+1) + ':', (result if result != -1 else values[-1]))

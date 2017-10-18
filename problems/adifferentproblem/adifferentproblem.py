import sys
for line in sys.stdin:
	values = [int(i) for i in line.strip().split()]
	print(abs(values[0] - values[1]))
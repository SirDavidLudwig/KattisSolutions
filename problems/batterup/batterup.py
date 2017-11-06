import sys

sys.stdin.readline()
total = n = 0
for value in map(int, sys.stdin.readline().split()):
	if value != -1:
		n += 1
		total += value
print(total/n)

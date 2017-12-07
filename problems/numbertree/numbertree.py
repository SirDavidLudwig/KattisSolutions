import sys

parts = input().strip().split()
index = 0
if len(parts) == 2:
	for d in parts[1]:
		index = 2*index + 1 + (d == 'R')
print(2**(int(parts[0])+1)-1-index)

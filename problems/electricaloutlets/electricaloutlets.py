import sys

for i in range(int(input())):
	values = list(map(int, input().split()[1:]))
	print(sum(values) - len(values) + 1)

import sys

for i in range(int(input())):
	print(sum((int(n if n else '0')*60**j for j, n in enumerate(input().split(',')[::-1]))))

import sys

days = set()

for i in range(int(input())):
	d1, d2 = map(int, input().split())
	for j in range(d1, d2 + 1):
		days.add(j)

print(len(days))

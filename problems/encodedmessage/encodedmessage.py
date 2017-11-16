from math import sqrt
import sys

for i in range(int(input())):
	message = input().strip()
	square = int(sqrt(len(message)))
	for j in range(square - 1, -1, -1):
		for k in range(j, len(message), square):
			print(end=message[k])
	print()

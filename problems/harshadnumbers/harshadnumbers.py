import math
import sys

n = int(input())
while n % sum([int(i) for i in str(n)]) != 0:
	n += 1
print(n)

from math import *
import sys

def sumDigits(s):
	r = 0
	for char in str(s):
		r += int(char)
	return r

l = int(sys.stdin.readline())
d = int(sys.stdin.readline())
x = int(sys.stdin.readline())

n = l
while sumDigits(n) != x:
	n += 1

m = d
while sumDigits(m) != x:
	m -= 1

print(n)
print(m)

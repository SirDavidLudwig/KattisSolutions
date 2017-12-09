import sys

def convert(number, base):
	try:
		return int(number, base)
	except ValueError:
		return 0

for i in range(int(input())):
	n, v = input().split()
	print(n, convert(v, 8), convert(v, 10), convert(v, 16))

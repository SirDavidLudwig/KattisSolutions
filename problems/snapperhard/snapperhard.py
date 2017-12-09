import sys

for i in range(int(input())):
	n, k = map(int, input().split())
	print("Case #%d: %s" % (i+1, "ON" if k & 2**n-1 == 2**n-1 else "OFF"))

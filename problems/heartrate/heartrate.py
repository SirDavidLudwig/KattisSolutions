import sys

for i in range(int(input())):
	b, p = map(float, input().split())
	print("%.4f %.4f %.4f" % (60*(b-1)/p, 60*b/p, 60*(b+1)/p))

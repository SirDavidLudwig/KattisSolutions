import sys

r, c = map(int, sys.stdin.readline().split())
print("{0:.6f}".format(100*(r-c)**2/r**2))

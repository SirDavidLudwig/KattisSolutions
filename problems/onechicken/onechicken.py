import sys

p, c = map(int, sys.stdin.readline().split())

if p < c:
	print("Dr. Chaz will have {} piece{} of chicken left over!".format(c-p, 's'*(c-p != 1)))
else:
	print("Dr. Chaz needs {} more piece{} of chicken!".format(p-c, 's'*(p-c != 1)))

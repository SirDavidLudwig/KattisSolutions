from operator import *
import sys

a, b, c = map(int, sys.stdin.readline().split())

opSym = '+-*/'
ops = [add, sub, mul, truediv]
for i in range(4):
	if ops[i](a, b) == c:
		print("{}{}{}={}".format(a, opSym[i], b, c))
		sys.exit()
	elif ops[i](b, c) == a:
		print("{}={}{}{}".format(a, b, opSym[i], c))
		sys.exit()
